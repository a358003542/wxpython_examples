#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        self.box = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(panel, label='title')

        self.box.Add(self.title, 0, wx.EXPAND | wx.TOP | wx.LEFT, 20)

        fgs = wx.FlexGridSizer(3, 2, 9, 25)

        title = wx.StaticText(panel, label="Title")
        author = wx.StaticText(panel, label="Author")
        review = wx.StaticText(panel, label="Review")

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        fgs.AddMany([(title), (tc1, 1, wx.EXPAND),
                     (author), (tc2, 1, wx.EXPAND),
                     (review, 1, wx.EXPAND), (tc3, 1, wx.EXPAND),
                     ])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        self.box.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(self.box)


def main():
    app = wx.App()
    ex = Example(None, title='Review')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
