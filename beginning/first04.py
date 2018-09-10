#!/usr/bin/env python3
# -*-coding:utf-8-*-

"""

打开文件

"""

import os


import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 600))

        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        self.CreateStatusBar()  # 新建状态栏

        filemenu = wx.Menu()

        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "打开一个文件")

        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")

        filemenu.AppendSeparator()

        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()

        menuBar.Append(filemenu, "&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)


        self.Show(True)

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True) # 关闭本窗体

    def OnOpen(self,e):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


app = wx.App(False)
frame = MainWindow(None, "small editor")

app.MainLoop()
