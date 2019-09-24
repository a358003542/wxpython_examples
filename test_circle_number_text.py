#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx

from customization.colorCircleNumber import ColorCircleNumber


class DemoPanel(wx.Panel):
    """
    This will be the first notebook tab
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """"""

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        box = wx.BoxSizer(wx.VERTICAL)

        line_one = wx.StaticLine(self)

        text1 = ColorCircleNumber(self, label='2', size=(22, 22),
                                  color='#39AAFF', border_color='#39AAFF',
                                  font_color='white')

        text2 = ColorCircleNumber(self, label='2', size=(22, 22),
                                  border_color='#39aaff', font_color='gray',
                                  color='white')

        box.Add(line_one, 0, wx.EXPAND, 0)
        box.Add(text1, 0)
        box.Add(text2, 0)
        self.SetSizer(box)

        self.Layout()


########################################################################


class DemoFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "test color static line",
                          size=(600, 400)
                          )
        self.panel = DemoPanel(self)

        self.Layout()


if __name__ == "__main__":
    app = wx.App()
    frame = DemoFrame()
    frame.Show()
    app.MainLoop()
