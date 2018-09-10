#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx

class SketchWindow(wx.Window):
    def __init__(self, parent, ID):
        super(SketchWindow, self).__init__(parent, ID)

        self.SetBackgroundColour("White")

        self.color = "Black"

        self.thickness = 1

        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

        self.line = []
        self.curLine = []
        self.pos = (0,0)
        self.InitBuffer()

    def InitBuffer(self):
        size = self.GetClientSize()

        self.buffer = wx.EmptyBitmap(size.width, size.height)

        dc = wx.BufferedDC(None, self.buffer)

        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))

        dc.Clear()

        self.DrawLines(dc)

        self.reInitBuffer = False


if __name__