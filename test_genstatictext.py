#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx
import wx.lib.stattext as ST

app = wx.App(0)

frame = wx.Frame(None, -1, "wx.lib.stattext Test")
panel = wx.Panel(frame)

st1 = ST.GenStaticText(panel, -1, "This is an example of static text", (20, 10))

st2 = ST.GenStaticText(panel, -1, "Is this yellow?", (20, 70), (120, -1))
st2.SetBackgroundColour('Yellow')

ST.GenStaticText(panel, -1, "align center", (160, 70), (120, -1),
                 wx.ALIGN_CENTER)
ST.GenStaticText(panel, -1, "align right", (300, 70), (120, -1), wx.ALIGN_RIGHT)

frame.Show()
app.MainLoop()
