#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx
import wx.lib.scrolledpanel as scroll


class AutoScrolledBottomPanel(scroll.ScrolledPanel):
    def __init__(self, parent, **kwargs):
        super(AutoScrolledBottomPanel, self).__init__(parent, **kwargs)

    def SetupScrolling(self, scroll_x=True, scroll_y=True, rate_x=20, rate_y=20,
                       scrollToBottom=True, scrollIntoView=True):
        """
        This function sets up the event handling necessary to handle
        scrolling properly. It should be called within the `__init__`
        function of any class that is derived from :class:`ScrolledPanel`,
        once the controls on the panel have been constructed and
        thus the size of the scrolling area can be determined.

        :param bool `scroll_x`: ``True`` to allow horizontal scrolling, ``False`` otherwise;
        :param bool `scroll_y`: ``True`` to allow vertical scrolling, ``False`` otherwise;
        :param int `rate_x`: the horizontal scroll increment;
        :param int `rate_y`: the vertical scroll increment;
        :param bool `scrollToTop`: ``True`` to scroll all way to the top, ``False`` otherwise;
        :param bool `scrollIntoView`: ``True`` to scroll a focused child into view, ``False`` otherwise.
        """

        self.scrollIntoView = scrollIntoView

        # The following is all that is needed to integrate the sizer and the scrolled window
        if not scroll_x: rate_x = 0
        if not scroll_y: rate_y = 0

        # Round up the virtual size to be a multiple of the scroll rate
        sizer = self.GetSizer()
        if sizer:
            w, h = sizer.GetMinSize()
            if rate_x:
                w += rate_x - (w % rate_x)
            if rate_y:
                h += rate_y - (h % rate_y)
            self.SetVirtualSize((w, h))
        self.SetScrollRate(rate_x, rate_y)
        wx.CallAfter(self._SetupAfter,
                     scrollToBottom)  # scroll back to top after initial events

    def _SetupAfter(self, scrollToBottom):
        self.SetVirtualSize(self.GetBestVirtualSize())
        size = self.GetBestVirtualSize()

        if scrollToBottom:
            self.Scroll(0, size[1])
