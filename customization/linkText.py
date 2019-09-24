#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx
from wx.lib.stattext import GenStaticText

from src.gui_utils import set_item_attr


class LinkText(GenStaticText):
    """
    一个简单的文字，主要定制了鼠标浮动和离开的表现效果，
    具体点击后的行为需要另外定制
    """

    def __init__(self, parent, ID=-1, label="", font_size=9,
                 background_color='white', font_color='blue5',
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.ALIGN_LEFT,
                 name="LinkText"):
        super(LinkText, self).__init__(parent, ID=ID, label=label,
                                       pos=pos, size=size,
                                       style=style,
                                       name=name)

        self.normal_font = wx.Font(font_size, wx.FONTFAMILY_DEFAULT,
                                   wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                                   False)
        self.underline_font = wx.Font(font_size, wx.FONTFAMILY_DEFAULT,
                                      wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                                      True)

        set_item_attr(self, {
            'background_color': background_color,
            'font': self.normal_font,
            'font_color': font_color
        })

        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseEnter)

    def OnMouseEnter(self, event):
        self.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        self.SetFont(self.underline_font)

        event.Skip()

    def OnMouseLeave(self, event):
        self.SetCursor(wx.NullCursor)
        self.SetFont(self.normal_font)
        event.Skip()
