#!/usr/bin/env python3
# -*-coding:utf-8-*-

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(200, 100))

        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)


app = wx.App(False)
frame = MyFrame(None, "small editor")

app.MainLoop()
