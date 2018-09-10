#!/usr/bin/env python3
# -*-coding:utf-8-*-

"""

add a menu.

"""

import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(200, 100))

        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.CreateStatusBar()  # 新建状态栏

        filemenu = wx.Menu()

        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")

        filemenu.AppendSeparator()

        filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()

        menuBar.Append(filemenu, "&File")

        self.SetMenuBar(menuBar)

        self.Show(True)


app = wx.App(False)
frame = MainWindow(None, "small editor")

app.MainLoop()
