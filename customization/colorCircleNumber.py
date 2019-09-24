#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx


class ColorCircleNumber(wx.Panel):
    """
    绘制的数字序号①②③...
    """

    def __init__(self, parent, border_color='blue', font_color='white',
                 font_size=10, font_bold=False, color='blue',
                 label='1', **kwargs):
        super(ColorCircleNumber, self).__init__(parent=parent, **kwargs)
        self.parent = parent

        self.font_color = font_color
        self.border_color = border_color
        self.color = color
        self.label = label
        self.font_size = font_size
        self.font_bold = font_bold

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def change_color(self, color):
        self.color = color
        self.Refresh()

    def change_font_color(self, font_color):
        self.font_color = font_color
        self.Refresh()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        width, height = self.GetClientSize()
        radius = width / 2 - 1

        dc.SetBrush(wx.Brush(wx.Colour(self.color)))
        dc.SetPen(wx.Pen(wx.Colour(self.border_color)))
        dc.DrawCircle(width / 2, height / 2, radius)

        if self.font_bold:
            font = wx.Font(wx.FontInfo(self.font_size).Bold())
        else:
            font = wx.Font(wx.FontInfo(self.font_size))
        dc.SetFont(font)

        dc.SetTextForeground(wx.Colour(self.font_color))

        text_width, text_height = dc.GetTextExtent(self.label)

        dc.DrawText(self.label, width / 2 - text_width / 2,
                    height / 2 - text_height / 2)
