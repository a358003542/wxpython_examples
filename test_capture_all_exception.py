#!/usr/bin/env python
# -*-coding:utf-8-*-


import sys

import traceback

import wx


class Panel(wx.Panel):
    def __init__(self, parent):
        super(Panel, self).__init__(parent)

        button = wx.Button(self, label='抛异常')
        button.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, event):
        1 / 0


def MyExceptionHook(etype, value, trace):
    """
    etype exception type
    value exception message
    trace traceback header
    :param etype:
    :param value:
    :param trace:
    :return:
    """
    tmp = traceback.format_exception(etype, value, trace)

    exception = "".join(tmp)

    print(exception)


class DemoFrame(wx.Frame):
    def __init__(self):
        super(DemoFrame, self).__init__(None, -1, "test capture all excepiton", size=(600, 400))

        sys.excepthook = MyExceptionHook
        panel = Panel(self)


if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame()
    frame.Show()

    app.MainLoop()
