#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx


class MyMessageDialog(wx.MessageDialog):
    """
    进行了一些基本的中文化工作
    """

    def __init__(self, parent, message, caption=None, *args, **kwargs):
        super(MyMessageDialog, self).__init__(parent, message, caption=caption,
                                              *args, **kwargs)

        self.SetOKCancelLabels("好的", "取消")

        self.CenterOnScreen()
