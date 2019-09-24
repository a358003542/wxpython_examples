#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx
import wx.lib.agw.pycollapsiblepane as PCP


class MyGTKExpander(PCP.GTKExpander):
    """
    A :class:`GTKExpander` allows the user to hide or show its child by clicking on an expander
    triangle.
    """

    def __init__(self, parent, id=wx.ID_ANY, label="", expander_color='black',
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.NO_BORDER):

        super(MyGTKExpander, self).__init__(parent, id=id, label=label, pos=pos,
                                            size=size, style=style)
        self.expander_color = expander_color

    def OnDrawGTKExpander(self, dc):
        """
        Draws the :class:`GTKExpander` triangle.

        :param `dc`: an instance of :class:`wx.DC`.
        """

        size = self.GetSize()
        label = self._parent.GetBtnLabel()
        triangleWidth, triangleHeight = self._parent.GetExpanderDimensions()
        textWidth, textHeight, descent, externalLeading = dc.GetFullTextExtent(
            label, self.GetFont())

        brush = wx.Brush()
        brush.SetColour(self.expander_color)
        dc.SetBrush(brush)
        pen = wx.Pen()
        pen.SetColour(self.expander_color)
        dc.SetPen(pen)

        if self._parent.IsCollapsed():
            startX, startY = triangleWidth // 2, size.y - triangleHeight - 1 - descent
            pt1 = wx.Point(startX, startY)
            pt2 = wx.Point(startX, size.y - 1 - descent)
            pt3 = wx.Point(startX + triangleWidth,
                           size.y - triangleHeight // 2 - 1 - descent)
        else:

            startX, startY = 0, size.y - triangleWidth - descent - 1
            pt1 = wx.Point(startX, startY)
            pt2 = wx.Point(startX + triangleHeight, startY)
            pt3 = wx.Point(startX + triangleHeight // 2, size.y - descent - 1)

        dc.DrawPolygon([pt1, pt2, pt3])

    def OnDrawGTKText(self, dc):
        """
        Draws the :class:`GTKExpander` text label.

        :param `dc`: an instance of :class:`wx.DC`.
        """

        size = self.GetSize()
        label = self._parent.GetBtnLabel()
        triangleWidth, triangleHeight = self._parent.GetExpanderDimensions()
        textWidth, textHeight, descent, externalLeading = dc.GetFullTextExtent(
            label, self.GetFont())
        dc.SetFont(self.GetFont())
        dc.SetTextForeground(self.expander_color)

        startX, startY = 2 * triangleHeight + 1, size.y - textHeight
        dc.DrawText(label, startX, startY)


class MyPyCollapsiblePane(PCP.PyCollapsiblePane):
    """
    :class:`PyCollapsiblePane` is a container with an embedded button-like control which
    can be used by the user to collapse or expand the pane's contents.
    """

    def __init__(self, parent, id=wx.ID_ANY, label="", expander_color='black',
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, agwStyle=wx.CP_DEFAULT_STYLE,
                 validator=wx.DefaultValidator, name="PyCollapsiblePane"):

        wx.Panel.__init__(self, parent, id, pos, size, style, name)

        self._pButton = self._pStaticLine = self._pPane = self._sz = None
        self._strLabel = label
        self._bCollapsed = True
        self._agwStyle = agwStyle

        self._pPane = wx.Panel(self, style=wx.TAB_TRAVERSAL | wx.NO_BORDER)
        self._pPane.Hide()

        if self.HasAGWFlag(PCP.CP_USE_STATICBOX):
            # Use a StaticBox instead of a StaticLine, and the button's
            # position will be handled separately so don't put it in the sizer
            self._pStaticBox = wx.StaticBox(self)
            self.SetButton(wx.Button(self, wx.ID_ANY, self.GetLabel(),
                                     style=wx.BU_EXACTFIT))
            self._sz = wx.BoxSizer(wx.VERTICAL)
            self._sz.Add((1, 1))  # spacer, size will be reset later
            self._contentSizer = wx.StaticBoxSizer(self._pStaticBox,
                                                   wx.VERTICAL)
            self._contentSizer.Add((1, 1))  # spacer, size will be reset later
            self._contentSizer.Add(self._pPane, 1, wx.EXPAND)
            self._sz.Add(self._contentSizer, 1, wx.EXPAND)

            if self.HasAGWFlag(
                    PCP.CP_USE_STATICBOX) and 'wxMSW' in wx.PlatformInfo:
                # This hack is needed on Windows because wxMSW clears the
                # CLIP_SIBLINGS style from all sibling controls that overlap the
                # static box, so the box ends up overdrawing the button since we
                # have the button overlapping the box. This hack will ensure that
                # the button is refreshed after every time that the box is drawn.
                # This adds a little flicker but it is not too bad compared to
                # others.
                def paint(evt):
                    def updateBtn():
                        if self and self._pButton:
                            self._pButton.Refresh()
                            self._pButton.Update()

                    wx.CallAfter(updateBtn)
                    evt.Skip()

                self._pStaticBox.Bind(wx.EVT_PAINT, paint)

        elif self.HasAGWFlag(PCP.CP_GTK_EXPANDER):
            self._sz = wx.BoxSizer(wx.HORIZONTAL)
            self.SetExpanderDimensions(3, 6)
            self.SetButton(MyGTKExpander(self, wx.ID_ANY, self.GetLabel(),
                                         expander_color=expander_color))
            self._sz.Add(self._pButton, 0, wx.LEFT | wx.TOP | wx.BOTTOM,
                         self.GetBorder())

            self._pButton.Bind(wx.EVT_PAINT, self.OnDrawGTKStyle)
            self._pButton.Bind(wx.EVT_LEFT_DOWN, self.OnButton)
            if wx.Platform == "__WXMSW__":
                self._pButton.Bind(wx.EVT_LEFT_DCLICK, self.OnButton)

        else:
            # create children and lay them out using a wx.BoxSizer
            # (so that we automatically get RTL features)
            self.SetButton(wx.Button(self, wx.ID_ANY, self.GetLabel(),
                                     style=wx.BU_EXACTFIT))
            self._pStaticLine = wx.StaticLine(self, wx.ID_ANY)

            if self.HasAGWFlag(PCP.CP_LINE_ABOVE):
                # put the static line above the button
                self._sz = wx.BoxSizer(wx.VERTICAL)
                self._sz.Add(self._pStaticLine, 0, wx.ALL | wx.GROW,
                             self.GetBorder())
                self._sz.Add(self._pButton, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM,
                             self.GetBorder())
            else:
                # arrange the static line and the button horizontally
                self._sz = wx.BoxSizer(wx.HORIZONTAL)
                self._sz.Add(self._pButton, 0, wx.LEFT | wx.TOP | wx.BOTTOM,
                             self.GetBorder())
                self._sz.Add(self._pStaticLine, 1,
                             wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT,
                             self.GetBorder())

        self.Bind(wx.EVT_SIZE, self.OnSize)
