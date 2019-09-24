#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx

from customization.myfancytext import StaticFancyText

test_str1 = '<font family="fixed" weight="bold" color="dark green" size="30">1</font><font family="fixed" color="gray" size="20" weight="bold" >/3</font>'

test_str2 = '<font color="blue" >○ </font><font>打开</font><font color="red">发票填开</font><font>窗口</font>'

test_str = ('<font style="italic" family="swiss" color="red" weight="bold" >'
            'some  |<sup>23</sup> <angle/>text<sub>with <angle/> subscript</sub>'
            '</font> some other text')

explain_text = '<font color="blue5" >○ </font><font size="11">打开</font><font color="note-font" size="11">发票填开</font><font size="11">窗口\n</font><font color="blue5" >○ </font><font size="11">找到“</font><font color="note-font" size="11">货物或应税劳务、服务名称</font><font size="11">”填写框\n</font><font color="blue5" >○ </font><font size="11">单击填写框出现的按钮，进入税收分类编码页</font>'


class DemoPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.box = wx.BoxSizer(wx.VERTICAL)

        text1 = StaticFancyText(self, -1, test_str1)

        text2 = StaticFancyText(self, -1, test_str2)

        text3 = StaticFancyText(self, -1, explain_text)

        self.box.Add(text1)

        self.box.Add(text2)

        self.box.Add(text3)

        self.SetSizer(self.box)


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
