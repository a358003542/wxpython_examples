#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx

from wx.lib.agw import ultimatelistctrl as ULC


class MyListCtrl(ULC.UltimateListCtrl):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0, agwStyle=ULC.ULC_VRULES |
                                   ULC.ULC_HRULES |
                                   ULC.ULC_REPORT |
                                   ULC.ULC_HAS_VARIABLE_ROW_HEIGHT |
                                   ULC.ULC_SINGLE_SEL |
                                   ULC.ULC_BORDER_SELECT
                 ,
                 validator=wx.DefaultValidator, name="UltimateListCtrl"):
        ULC.UltimateListCtrl.__init__(self, parent, id=id, pos=pos, size=size,
                                      style=style, agwStyle=agwStyle,
                                      validator=validator, name=name)

        width_name = 200
        width_code = 230
        width_type = 120
        width_slv = 60
        width_unit = 60
        width_price = 120
        width_operation = 150

        col_name = ULC.UltimateListItem()
        col_name._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_WIDTH
        col_name._text = "科目名称"
        col_name._width = width_name
        self.InsertColumnInfo(0, col_name)

        col_code = ULC.UltimateListItem()
        col_code._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_WIDTH
        col_code._text = "税收分类编码"
        col_code._width = width_code
        self.InsertColumnInfo(1, col_code)

        col_type = ULC.UltimateListItem()
        col_type._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_WIDTH
        col_type._text = "规格"
        col_type._width = width_type
        self.InsertColumnInfo(2, col_type)

        col_slv = ULC.UltimateListItem()
        col_slv._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_WIDTH
        col_slv._text = "税率"
        col_slv._width = width_slv
        self.InsertColumnInfo(3, col_slv)

        col_unit = ULC.UltimateListItem()
        col_unit._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_WIDTH
        col_unit._text = "单位"
        col_unit._width = width_unit
        self.InsertColumnInfo(4, col_unit)

        col_price = ULC.UltimateListItem()
        col_price._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_WIDTH
        col_price._text = "单价"
        col_price._width = width_price
        self.InsertColumnInfo(5, col_price)

        col_operation = ULC.UltimateListItem()
        col_operation._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_WIDTH
        col_operation._text = "操作"
        col_operation._width = width_operation
        self.InsertColumnInfo(6, col_operation)

        panel1 = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        self.button1 = wx.Button(panel1, -1, "检测名字", size=(100, 32))
        self.button2 = wx.Button(panel1, -1, "删除", size=(50, 32))
        box.Add(self.button1, 0, wx.EXPAND, 0)
        box.Add(self.button2, 0, wx.EXPAND, 0)
        panel1.SetSizerAndFit(box)
        panel1.Layout()

        self.InsertStringItem(0, "")

        textctrl1 = wx.TextCtrl(self, size=(width_name, -1), style=wx.NO_BORDER)
        textctrl2 = wx.TextCtrl(self, size=(width_code, -1), style=wx.NO_BORDER)
        textctrl3 = wx.TextCtrl(self, size=(width_type, -1), style=wx.NO_BORDER)
        textctrl4 = wx.TextCtrl(self, size=(width_slv, -1), style=wx.NO_BORDER)
        textctrl5 = wx.TextCtrl(self, size=(width_unit, -1), style=wx.NO_BORDER)
        textctrl6 = wx.TextCtrl(self, size=(width_price, -1),
                                style=wx.NO_BORDER)

        self.SetItemWindow(0, 0, textctrl1)
        self.SetItemWindow(0, 1, textctrl2)
        self.SetItemWindow(0, 2, textctrl3)
        self.SetItemWindow(0, 3, textctrl4)
        self.SetItemWindow(0, 4, textctrl5)
        self.SetItemWindow(0, 5, textctrl6)
        self.SetItemWindow(0, 6, panel1)


class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.ulc = MyListCtrl(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.ulc, 1, wx.EXPAND)
        self.SetSizer(sizer)


########################################################################
class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="MvP UltimateListCtrl Demo")
        panel = TestPanel(self)
        self.Show()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App()
    frame = TestFrame()
    app.MainLoop()
