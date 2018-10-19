#!/usr/bin/env python
# -*-coding:utf-8-*-

import wx
import wx.adv
from wx.adv import Wizard as wiz
from wx.adv import WizardPage, WizardPageSimple

#----------------------------------------------------------------------

def makePageTitle(wizPg, title):
    sizer = wx.BoxSizer(wx.VERTICAL)
    wizPg.SetSizer(sizer)
    title = wx.StaticText(wizPg, -1, title)
    title.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
    sizer.Add(wx.StaticLine(wizPg, -1), 0, wx.EXPAND|wx.ALL, 5)
    return sizer

#----------------------------------------------------------------------

class TitledPage(wx.adv.WizardPageSimple):
    def __init__(self, parent, title):
        WizardPageSimple.__init__(self, parent)
        self.sizer = makePageTitle(self, title)


#----------------------------------------------------------------------

class SkipNextPage(wx.adv.WizardPage):
    def __init__(self, parent, title):
        WizardPage.__init__(self, parent)
        self.next = self.prev = None
        self.sizer = makePageTitle(self, title)

        self.cb = wx.CheckBox(self, -1, "Skip next page")
        self.sizer.Add(self.cb, 0, wx.ALL, 5)

    def SetNext(self, next):
        self.next = next

    def SetPrev(self, prev):
        self.prev = prev


    # Classes derived from wxPyWizardPanel must override
    # GetNext and GetPrev, and may also override GetBitmap
    # as well as all those methods overridable by
    # wx.PyWindow.

    def GetNext(self):
        """If the checkbox is set then return the next page's next page"""
        if self.cb.GetValue():
            self.next.GetNext().SetPrev(self)
            return self.next.GetNext()
        else:
            self.next.GetNext().SetPrev(self.next)
            return self.next

    def GetPrev(self):
        return self.prev

#----------------------------------------------------------------------

class UseAltBitmapPage(WizardPage):
    def __init__(self, parent, title):
        WizardPage.__init__(self, parent)
        self.next = self.prev = None
        self.sizer = makePageTitle(self, title)

        self.sizer.Add(wx.StaticText(self, -1, "This page uses a different bitmap"),
                       0, wx.ALL, 5)

    def SetNext(self, next):
        self.next = next

    def SetPrev(self, prev):
        self.prev = prev

    def GetNext(self):
        return self.next

    def GetPrev(self):
        return self.prev

    def GetBitmap(self):
        # You usually wouldn't need to override this method
        # since you can set a non-default bitmap in the
        # wxWizardPageSimple constructor, but if you need to
        # dynamically change the bitmap based on the
        # contents of the wizard, or need to also change the
        # next/prev order then it can be done by overriding
        # GetBitmap.
        pass



class ChaoShengHuo(wx.Frame):
    """
    主面板
    """
    __instance = None  # 单例模式

    @classmethod
    def getInstance(cls):
        return cls.__instance if cls.__instance is not None else ChaoShengHuo()

    def __init__(self, *args, **kwargs):
        super(ChaoShengHuo, self).__init__(*args, **kwargs)
        ChaoShengHuo.__instance = self

        # Create the wizard and the pages
        wizard = wiz(self, -1, "Simple Wizard", )
        page1 = TitledPage(wizard, "Page 1")
        page2 = TitledPage(wizard, "Page 2")
        page3 = TitledPage(wizard, "Page 3")
        page4 = TitledPage(wizard, "Page 4")
        self.page1 = page1

        page1.sizer.Add(wx.StaticText(page1, -1, """
        This wizard is totally useless, but is meant to show how to
        chain simple wizard pages together in a non-dynamic manner.
        IOW, the order of the pages never changes, and so the
        wxWizardPageSimple class can easily be used for the pages."""))
        wizard.FitToPage(page1)
        page4.sizer.Add(wx.StaticText(page4, -1, "\nThis is the last page."))

        # Use the convenience Chain function to connect the pages
        WizardPageSimple.Chain(page1, page2)
        WizardPageSimple.Chain(page2, page3)
        WizardPageSimple.Chain(page3, page4)

        wizard.GetPageAreaSizer().Add(page1)
        if wizard.RunWizard(page1):
            print('end')
        else:
            print('cancel')


        self.Bind(wx.adv.EVT_WIZARD_PAGE_CHANGED, self.OnWizPageChanged)
        self.Bind(wx.adv.EVT_WIZARD_PAGE_CHANGING, self.OnWizPageChanging)
        self.Bind(wx.adv.EVT_WIZARD_CANCEL, self.OnWizCancel)

        self.box = wx.BoxSizer(wx.VERTICAL)


        self.Layout()



    def OnWizPageChanged(self, evt):
        if evt.GetDirection():
            dir = "forward"
        else:
            dir = "backward"

        page = evt.GetPage()


    def OnWizPageChanging(self, evt):
        if evt.GetDirection():
            dir = "forward"
        else:
            dir = "backward"

        page = evt.GetPage()


    def OnWizCancel(self, evt):
        page = evt.GetPage()

        # Show how to prevent cancelling of the wizard.  The
        # other events can be Veto'd too.
        if page is self.page1:
            wx.MessageBox("Cancelling on the first page has been prevented.", "Sorry")
            evt.Veto()


    def OnWizFinished(self, evt):
        pass




if __name__ == '__main__':
    class ChaoShengHuoApp(wx.App):
        def OnInit(self):
            self.name = "SingleApp-%s" % wx.GetUserId()
            self.instance = wx.SingleInstanceChecker(self.name)

            if self.instance.IsAnotherRunning():
                wx.MessageBox("已经有一个潮生活发票助手程序在运行了！", "Do not Panic")
                return False
            else:
                the_frame = ChaoShengHuo(None, -1)
                the_frame.Show(True)
                return True

    app = ChaoShengHuoApp()
    app.MainLoop()


