#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx


class ColorCircle(wx.Panel):
    """
    带颜色的圆形
    """

    def __init__(self, parent, color='black', **kwargs):
        super(ColorCircle, self).__init__(parent=parent, **kwargs)
        self.parent = parent

        self.color = color

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        width, height = self.GetClientSize()
        radius = width / 2 - 1
        dc.SetPen(wx.Pen(wx.Colour(self.color)))

        dc.SetBrush(wx.Brush(wx.Colour(self.color)))

        dc.DrawCircle(width / 2, height / 2, radius)
