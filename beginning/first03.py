#!/usr/bin/env python3
# -*-coding:utf-8-*-

"""

添加事件

"""


import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(200, 100))

        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.CreateStatusBar()  # 新建状态栏

        filemenu = wx.Menu()

        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")

        filemenu.AppendSeparator()

        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()

        menuBar.Append(filemenu, "&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True) # 关闭本窗体


app = wx.App(False)
frame = MainWindow(None, "small editor")

app.MainLoop()
