#!/usr/bin/env python
# -*-coding:utf-8-*-

import wx
import wx.lib.agw.hyperlink as hl


class MyHyperLink(hl.HyperLinkCtrl):
    def __init__(self, parent, id=-1, label="", color='gold5',
                 background_color='white', pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, name="staticText", URL=""):
        super(MyHyperLink, self).__init__(parent, id=id, label=label, pos=pos,
                                          size=size, style=style, name=name,
                                          URL=URL)

        self.color = color

        self.SetBackgroundColour(background_color)
        self.SetForegroundColour(self.color)

        self.SetColours(self.color, self.color, self.color)
        self.EnableRollover(True)
        self.SetUnderlines(False, False, True)
        self.UpdateLink()
