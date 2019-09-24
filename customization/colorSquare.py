#!/usr/bin/env python
# -*-coding:utf-8-*-

import wx


class ColorSquare(wx.Panel):
    """
    带颜色的方块
    """

    def __init__(self, parent, color='black', **kwargs):
        super(ColorSquare, self).__init__(parent=parent, **kwargs)
        self.parent = parent

        self.color = color

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        width, height = self.GetClientSize()

        dc.SetPen(wx.Pen(wx.Colour(self.color)))

        dc.SetBrush(wx.Brush(wx.Colour(self.color)))

        dc.DrawRectangle(0, 0, width, height)
