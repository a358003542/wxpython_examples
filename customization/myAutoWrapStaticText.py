#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx

from wx.lib.stattext import GenStaticText
from src.gui.customization.wordwrap import wordwrap_chinese


class MyAutoWrapStaicText(GenStaticText):
    """
    1. 增加更好的中文支持
    2. 增加size选项
    """

    def __init__(self, parent, **kwargs):
        """
        Defsult class constructor.

        :param wx.Window parent: a subclass of :class:`wx.Window`, must not be ``None``;
        :param string `label`: the :class:`AutoWrapStaticText` text label.
        """

        super(MyAutoWrapStaicText, self).__init__(parent, -1, **kwargs)

        self.label = self.GetLabel()

        # colBg = wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK)
        # self.SetBackgroundColour(colBg)
        # self.SetOwnForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))

        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        """
        Handles the ``wx.EVT_SIZE`` event for :class:`AutoWrapStaticText`.

        :param `event`: a :class:`wx.SizeEvent` event to be processed.
        """

        event.Skip()
        self.Wrap(event.GetSize().width)

    def Wrap(self, width):
        """
        This functions wraps the controls label so that each of its lines becomes at
        most `width` pixels wide if possible (the lines are broken at words boundaries
        so it might not be the case if words are too long).

        If `width` is negative, no wrapping is done.

        :param integer `width`: the maximum available width for the text, in pixels.

        :note: Note that this `width` is not necessarily the total width of the control,
         since a few pixels for the border (depending on the controls border style) may be added.
        """

        if width < 0:
            return

        self.Freeze()

        dc = wx.ClientDC(self)
        dc.SetFont(self.GetFont())
        text = wordwrap_chinese(self.label, width, dc)
        self.SetLabel(text, wrapped=True)

        self.Thaw()

    def SetLabel(self, label, wrapped=False):
        """
        Sets the :class:`AutoWrapStaticText` label.

        All "&" characters in the label are special and indicate that the following character is
        a mnemonic for this control and can be used to activate it from the keyboard (typically
        by using ``Alt`` key in combination with it). To insert a literal ampersand character, you
        need to double it, i.e. use "&&". If this behaviour is undesirable, use :meth:`~Control.SetLabelText` instead.

        :param string `label`: the new :class:`AutoWrapStaticText` text label;
        :param bool `wrapped`: ``True`` if this method was called by the developer using :meth:`~AutoWrapStaticText.SetLabel`,
         ``False`` if it comes from the :meth:`~AutoWrapStaticText.OnSize` event handler.

        :note: Reimplemented from :class:`wx.Control`.
        """

        if not wrapped:
            self.label = label

        GenStaticText.SetLabel(self, label)
