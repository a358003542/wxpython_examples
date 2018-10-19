#!/usr/bin/env python
# -*-coding:utf-8-*-



import random
import wx


class TabPanel(wx.Panel):
    def __init__(self, parent):
        super(TabPanel, self).__init__(parent)


        self.colors = colors = ['red', 'blue', 'gray', 'yellow', 'green']

        self.SetBackgroundColour(random.choice(colors))

        button = wx.Button(self, label='press')
        button.Bind(wx.EVT_BUTTON, self.handle_button)

        box = wx.BoxSizer(wx.VERTICAL)

        box.Add(button, 0, wx.ALL, 0)

        self.SetSizer(box)
    def handle_button(self,  event):
        color = random.choice(self.colors)
        print(color)
        self.SetBackgroundColour(color)
        self.Refresh()

class TwoNotebook(wx.Notebook):
    def __init__(self, parent):
        super(TwoNotebook, self).__init__(parent)

        tab1 = TabPanel(self)
        self.AddPage(tab1, "Tab1")

        tab2 = TabPanel(self)

        self.AddPage(tab2, "Tab2")



class DemoPanel(wx.Panel):
    def __init__(self, parent):
        super(DemoPanel, self).__init__(parent)

        notebook = TwoNotebook(self)

        box = wx.BoxSizer(wx.VERTICAL)

        box.Add(notebook,1,wx.ALL|wx.EXPAND, 5)

        self.SetSizer(box)



class DemoFrame(wx.Frame):
    def __init__(self):
        super(DemoFrame, self).__init__(None, -1, "test two notebook", size=(600,400))
        panel = DemoPanel(self)


        self.Layout()

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame()
    frame.Show()

    app.MainLoop()