#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx
import wx.lib.colourdb


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(400, 300))
        # show the selected colour in this panel
        self.panel = wx.Panel(self)

        self.box = wx.BoxSizer(wx.VERTICAL)

        self.panel.SetSizer(self.box)

        wx.lib.colourdb.updateColourDB()
        # create a colour list from the colourdb database
        colour_list = wx.lib.colourdb.getColourList()
        self.colour_info_list = wx.lib.colourdb.getColourInfoList()

        for item in self.colour_info_list:
            print(item[0], ("#%02X%02X%02X" % tuple(item[1:])))

        # create a choice widget
        self.choice = wx.Choice(self.panel, -1, choices=colour_list)

        self.text = wx.StaticText(self.panel, label='')

        self.box.Add(self.choice)
        self.box.Add(self.text)

        # select item 0 (first item) in choice list to show
        self.choice.SetSelection(0)
        # set the current frame colour to the choice
        self.SetBackgroundColour(self.choice.GetStringSelection())
        # bind the checkbox events to an action
        self.choice.Bind(wx.EVT_CHOICE, self.OnChoice)

    def OnChoice(self, event):
        bgcolour = self.choice.GetStringSelection()

        # change colour of the panel to the selected colour ...
        self.panel.SetBackgroundColour(bgcolour)

        self.text.SetLabel("#%02X%02X%02X" % tuple(
            self.colour_info_list[self.choice.GetSelection()][1:]))

        self.panel.Refresh()
        # show the selected colour in the frame title
        self.SetTitle(bgcolour.lower())


app = wx.App()
frame = MyFrame(None, 'Select a colour')
frame.Show()
app.MainLoop()
