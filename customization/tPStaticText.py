#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx

import wx
from wx.lib.stattext import GenStaticText

BUFFERED = 0
if wx.Platform == "__WXMAC__":
    try:
        from Carbon.Appearance import kThemeBrushDialogBackgroundActive
    except ImportError:
        kThemeBrushDialogBackgroundActive = 1


class TPStaticText(GenStaticText):
    """
    带颜色的文本 在原GenStaticText
    - 加入了一个简陋的 delta_point 参数来简单位移下文本位置的起始位置
    - 加入了delta_linespace变量 可以简单调节行间距
    """

    def __init__(self, parent, delta_point=(0, 0), delta_linespace=0, style=0,
                 **kwargs):
        style |= wx.TRANSPARENT_WINDOW  # 透明文本核心语句
        super(TPStaticText, self).__init__(parent=parent, style=style, **kwargs)

        self.parent = parent

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)  # 透明文本核心语句
        self.delta_point = delta_point
        self.delta_linespace = delta_linespace

        self.Bind(wx.EVT_PAINT, self.OnPaint)  # 具体绘图从GenStaticText来稍作变动

    def change_point(self, point):
        self.delta_point = point
        self.Refresh()

    def OnPaint(self, event):
        """
        Handles the ``wx.EVT_PAINT`` for :class:`GenStaticText`.

        :param `event`: a :class:`wx.PaintEvent` event to be processed.
        """

        if BUFFERED:
            dc = wx.BufferedPaintDC(self)
        else:
            dc = wx.PaintDC(self)
        width, height = self.GetClientSize()
        if not width or not height:
            return

        if BUFFERED:
            clr = self.GetBackgroundColour()
            if wx.Platform == "__WXMAC__" and clr == self.defBackClr:
                # if colour is still the default then use the theme's  background on Mac
                themeColour = wx.MacThemeColour(
                    kThemeBrushDialogBackgroundActive)
                backBrush = wx.Brush(themeColour)
            else:
                backBrush = wx.Brush(clr, wx.BRUSHSTYLE_SOLID)
            dc.SetBackground(backBrush)
            dc.Clear()

        if self.IsEnabled():
            dc.SetTextForeground(self.GetForegroundColour())
        else:
            dc.SetTextForeground(
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))

        dc.SetFont(self.GetFont())
        label = self.GetLabel()
        style = self.GetWindowStyleFlag()
        x = y = 0
        for line in label.split('\n'):
            if line == '':
                w, h = self.GetTextExtent('W')  # empty lines have height too
            else:
                w, h = self.GetTextExtent(line)

            if style & wx.ALIGN_RIGHT:
                x = width - w
            if style & wx.ALIGN_CENTER:
                x = (width - w) / 2

            dc.DrawText(line, x + self.delta_point[0],
                        y + self.delta_point[1])  # 加入额外的位置调节参数
            y = y + h + self.delta_linespace  # 下次的起点y 上一次的y 加上 上一行的h+额外的linespace调节
