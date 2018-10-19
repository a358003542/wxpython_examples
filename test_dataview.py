#!/usr/bin/env python
# -*-coding:utf-8-*-



import wx
import wx.dataview as dv

import wx


class TestPanel(wx.Panel):
    def __init__(self, parent, **kwargs):
        wx.Panel.__init__(self, parent, -1, **kwargs)

        # create the listctrl
        self.dvlc = dvlc = dv.DataViewListCtrl(self, -1, size=(300,200))

        # Give it some columns.
        # The ID col we'll customize a bit:
        dvlc.AppendTextColumn('id', width=40)
        dvlc.AppendTextColumn('artist', width=170)
        dvlc.AppendTextColumn('title', width=260)
        dvlc.AppendTextColumn('genre', width=80)

        # Load the data. Each item (row) is added as a sequence of values
        # whose order matches the columns
        for itemvalues in [[1,2,3,4],[1,2,3,4],[12,3,3,3]]:
            dvlc.AppendItem(itemvalues)

        # Set the layout so the listctrl fills the panel
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.box.Add(dvlc, 0, wx.EXPAND)



class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(640, 480),style=wx.DEFAULT_FRAME_STYLE)

        self.panel = TestPanel(self, size=(640,400))

        self.Fit()







if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(None, "testing")

    frame.Show()

    app.MainLoop()