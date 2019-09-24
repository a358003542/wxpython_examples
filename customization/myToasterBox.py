#!/usr/bin/env python
# -*-coding:utf-8-*-

import wx
import wx.lib.agw.toasterbox as TB


class MyToasterBox(TB.ToasterBox):
    def __init__(self, parent, message='', background_color='white',
                 font_color='black',
                 tbstyle=TB.TB_SIMPLE,
                 windowstyle=TB.TB_DEFAULT_STYLE,
                 closingstyle=TB.TB_ONTIME,
                 scrollType=TB.TB_SCR_TYPE_FADE):
        super(MyToasterBox, self).__init__(parent, tbstyle=tbstyle,
                                           windowstyle=windowstyle,
                                           closingstyle=closingstyle,
                                           scrollType=scrollType)
        self.parent = parent

        self.SetPopupBackgroundColour(background_color)

        self.SetPopupTextColour(font_color)

        self.SetPopupText(message)

        self.CenterOnParent()

    def CenterOnParent(self, direction=wx.BOTH):
        """
        Centres the window on its parent (if any). If the :class:`ToasterBox` parent is ``None``,
        it calls :meth:`~ToasterBox.CenterOnScreen`.

        :param `direction`: specifies the direction for the centering. May be ``wx.HORIZONTAL``,
         ``wx.VERTICAL`` or ``wx.BOTH``.

        :note: This methods provides for a way to center :class:`ToasterBox` over their parents instead of the
         entire screen. If there is no parent, then behaviour is the same as :meth:`~ToasterBox.CenterOnScreen`.

        :see: :meth:`~ToasterBox.CenterOnScreen`.
        """

        if not self._parent:
            self.CenterOnScreen(direction)
            return

        parent = self._parent
        screenrect = parent.GetScreenRect()
        toast_width, toast_height = self._popupsize
        x, y = screenrect.GetX(), screenrect.GetY()
        width, height = screenrect.GetWidth(), screenrect.GetHeight()

        if direction == wx.VERTICAL:
            pos = wx.Point(x, (y + (height / 2) - (toast_height / 2)))
        elif direction == wx.HORIZONTAL:
            pos = wx.Point((x + (width / 2) - (toast_width / 2)), y)
        else:
            pos = wx.Point((x + (width / 2) - (toast_width / 2)),
                           (y + (height / 2) - (toast_height / 2)))

        self.SetPopupPosition(pos)

    def CenterOnScreen(self, direction=wx.BOTH):
        """
        Centres the :class:`ToasterBox` on screen.

        :param `direction`: specifies the direction for the centering. May be ``wx.HORIZONTAL``,
         ``wx.VERTICAL`` or ``wx.BOTH``.

        :see: :meth:`~ToasterBox.CenterOnParent`.
        """

        screenSize = wx.GetDisplaySize()
        toast_width, toast_height = self._popupsize
        width, height = screenSize.GetWidth(), screenSize.GetHeight()

        if direction == wx.VERTICAL:
            pos = wx.Point(0, (height / 2) - (toast_height / 2))
        elif direction == wx.HORIZONTAL:
            pos = wx.Point((width / 2) - (toast_width / 2), 0)
        else:
            pos = wx.Point((width / 2) - (toast_width / 2),
                           (height / 2) - (toast_height / 2))

        self.SetPopupPosition(pos)
