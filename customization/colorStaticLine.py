#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx


class ColorStaticLine(wx.Panel):
    """
    带颜色的线段
    """

    def __init__(self, parent, color='black', mode='hline', **kwargs):
        super(ColorStaticLine, self).__init__(parent=parent, **kwargs)
        self.parent = parent

        self.color = color
        self.mode = mode

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        width, height = self.GetClientSize()

        dc.SetPen(wx.Pen(wx.Colour(self.color)))

        if self.mode == 'hline':
            dc.DrawLine(0, 0, width, 0)
        elif self.mode == 'vline':
            dc.DrawLine(0, 0, 0, height)
