#!/usr/bin/env python
# -*-coding:utf-8-*-


import wx
import wx.lib.agw.labelbook as LB
from wx.lib.agw.labelbook import FlatBookBase, INB_LEFT, INB_RIGHT, INB_BORDER, \
    INB_USE_PIN_BUTTON, INB_TOP, INB_BOTTOM, \
    INB_BOLD_TAB_SELECTION, INB_FIT_BUTTON, INB_SHOW_ONLY_IMAGES, ArtManager, \
    INB_SHOW_ONLY_TEXT


class ImageContainer(LB.ImageContainer):
    """
    Base class for :class:`FlatImageBook` image container.
    """

    def __init__(self, parent, id=wx.ID_ANY, text_padding=20,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=0, agwStyle=0, name="ImageContainer"):
        super(ImageContainer, self).__init__(parent, id=id, pos=pos, size=size,
                                             style=style, agwStyle=agwStyle,
                                             name=name)

        self.text_padding = text_padding

    def OnPaint(self, event):
        """
        Handles the ``wx.EVT_PAINT`` event for :class:`wx.ImageContainer`.

        :param `event`: a :class:`PaintEvent` event to be processed.
        """

        dc = wx.BufferedPaintDC(self)
        style = self.GetParent().GetAGWWindowStyleFlag()

        backBrush = wx.WHITE_BRUSH
        if style & INB_BORDER:
            borderPen = wx.Pen(
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DSHADOW))
        else:
            borderPen = wx.TRANSPARENT_PEN

        size = self.GetSize()

        # Background
        dc.SetBrush(backBrush)

        borderPen.SetWidth(1)
        dc.SetPen(borderPen)
        dc.DrawRectangle(0, 0, size.x, size.y)
        bUsePin = (style & INB_USE_PIN_BUTTON and [True] or [False])[0]

        if bUsePin:

            # Draw the pin button
            clientRect = self.GetClientRect()
            pinRect = wx.Rect(clientRect.GetX() + clientRect.GetWidth() - 20, 2,
                              20, 20)
            self.DrawPin(dc, pinRect, not self._bCollapsed)

            if self._bCollapsed:
                return

        borderPen = wx.BLACK_PEN
        borderPen.SetWidth(1)
        dc.SetPen(borderPen)
        dc.DrawLine(0, size.y, size.x, size.y)
        dc.DrawPoint(0, size.y)

        clientSize = 0
        bUseYcoord = (style & INB_RIGHT or style & INB_LEFT)

        if bUseYcoord:
            clientSize = size.GetHeight()
        else:
            clientSize = size.GetWidth()

        # We reserver 20 pixels for the 'pin' button

        # The drawing of the images start position. This is
        # depenedent of the style, especially when Pin button
        # style is requested

        if bUsePin:
            if style & INB_TOP or style & INB_BOTTOM:
                pos = (style & INB_BORDER and [0] or [1])[0]
            else:
                pos = (style & INB_BORDER and [20] or [21])[0]
        else:
            pos = (style & INB_BORDER and [0] or [1])[0]

        nPadding = self.text_padding  # Pad text with 2 pixels on the left and right
        nTextPaddingLeft = 2

        count = 0
        normalFont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        boldFont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        boldFont.SetWeight(wx.BOLD)

        for i in range(len(self._pagesInfoVec)):

            count = count + 1

            # incase the 'fit button' style is applied, we set the rectangle width to the
            # text width plus padding
            # Incase the style IS applied, but the style is either LEFT or RIGHT
            # we ignore it
            dc.SetFont(normalFont)

            if style & INB_BOLD_TAB_SELECTION and self._nIndex == i:
                dc.SetFont(boldFont)

            textWidth, textHeight = dc.GetTextExtent(
                self._pagesInfoVec[i].GetCaption())

            # Default values for the surrounding rectangle
            # around a button
            rectWidth = self._nImgSize * 2  # To avoid the rectangle to 'touch' the borders
            rectHeight = self._nImgSize * 2

            # In case the style requires non-fixed button (fit to text)
            # recalc the rectangle width
            if style & INB_FIT_BUTTON and \
                    not ((style & INB_LEFT) or (style & INB_RIGHT)) and \
                    not self._pagesInfoVec[i].GetCaption() == "" and \
                    not (style & INB_SHOW_ONLY_IMAGES):

                rectWidth = ((textWidth + nPadding * 2) > rectWidth and [
                    nPadding * 2 + textWidth] or [rectWidth])[0]

                # Make the width an even number
                if rectWidth % 2 != 0:
                    rectWidth += 1

            # Check that we have enough space to draw the button
            # If Pin button is used, consider its space as well (applicable for top/botton style)
            # since in the left/right, its size is already considered in 'pos'
            pinBtnSize = (bUsePin and [20] or [0])[0]

            if pos + rectWidth + pinBtnSize > clientSize:
                break

            # Calculate the button rectangle
            modRectWidth = ((style & INB_LEFT or style & INB_RIGHT) and [
                rectWidth - 2] or [rectWidth])[0]
            modRectHeight = ((style & INB_LEFT or style & INB_RIGHT) and [
                rectHeight] or [rectHeight - 2])[0]

            if bUseYcoord:
                buttonRect = wx.Rect(1, pos, modRectWidth, modRectHeight)
            else:
                buttonRect = wx.Rect(pos, 1, modRectWidth, modRectHeight)

            # Check if we need to draw a rectangle around the button
            if self._nIndex == i:

                # Set the colours
                penColour = wx.SystemSettings.GetColour(
                    wx.SYS_COLOUR_ACTIVECAPTION)
                brushColour = ArtManager.Get().LightColour(
                    wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION),
                    75)

                dc.SetPen(wx.Pen(penColour))
                dc.SetBrush(wx.Brush(brushColour))

                # Fix the surrounding of the rect if border is set
                if style & INB_BORDER:

                    if style & INB_TOP or style & INB_BOTTOM:
                        buttonRect = wx.Rect(buttonRect.x + 1, buttonRect.y,
                                             buttonRect.width - 1,
                                             buttonRect.height)
                    else:
                        buttonRect = wx.Rect(buttonRect.x, buttonRect.y + 1,
                                             buttonRect.width,
                                             buttonRect.height - 1)

                dc.DrawRectangle(buttonRect)

            if self._nHoveredImgIdx == i:

                # Set the colours
                penColour = wx.SystemSettings.GetColour(
                    wx.SYS_COLOUR_ACTIVECAPTION)
                brushColour = ArtManager.Get().LightColour(
                    wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION),
                    90)

                dc.SetPen(wx.Pen(penColour))
                dc.SetBrush(wx.Brush(brushColour))

                # Fix the surrounding of the rect if border is set
                if style & INB_BORDER:

                    if style & INB_TOP or style & INB_BOTTOM:
                        buttonRect = wx.Rect(buttonRect.x + 1, buttonRect.y,
                                             buttonRect.width - 1,
                                             buttonRect.height)
                    else:
                        buttonRect = wx.Rect(buttonRect.x, buttonRect.y + 1,
                                             buttonRect.width,
                                             buttonRect.height - 1)

                dc.DrawRectangle(buttonRect)

            if bUseYcoord:
                rect = wx.Rect(0, pos, rectWidth, rectWidth)
            else:
                rect = wx.Rect(pos, 0, rectWidth, rectWidth)

            # Incase user set both flags:
            # INB_SHOW_ONLY_TEXT and INB_SHOW_ONLY_IMAGES
            # We override them to display both

            if style & INB_SHOW_ONLY_TEXT and style & INB_SHOW_ONLY_IMAGES:
                style ^= INB_SHOW_ONLY_TEXT
                style ^= INB_SHOW_ONLY_IMAGES
                self.GetParent().SetAGWWindowStyleFlag(style)

            # Draw the caption and text
            imgTopPadding = 10
            if not style & INB_SHOW_ONLY_TEXT and self._pagesInfoVec[
                i].GetImageIndex() != -1:

                if bUseYcoord:

                    imgXcoord = self._nImgSize / 2
                    imgYcoord = (style & INB_SHOW_ONLY_IMAGES and [
                        pos + self._nImgSize / 2] or [pos + imgTopPadding])[
                        0]

                else:

                    imgXcoord = pos + (rectWidth / 2) - (self._nImgSize / 2)
                    imgYcoord = (style & INB_SHOW_ONLY_IMAGES and [
                        self._nImgSize / 2] or [imgTopPadding])[0]

                self._ImageList.Draw(self._pagesInfoVec[i].GetImageIndex(), dc,
                                     imgXcoord, imgYcoord,
                                     wx.IMAGELIST_DRAW_TRANSPARENT, True)

            # Draw the text
            if not style & INB_SHOW_ONLY_IMAGES and not self._pagesInfoVec[
                                                            i].GetCaption() == "":

                if style & INB_BOLD_TAB_SELECTION and self._nIndex == i:
                    dc.SetFont(boldFont)
                else:
                    dc.SetFont(normalFont)

                # Check if the text can fit the size of the rectangle,
                # if not truncate it
                fixedText = self._pagesInfoVec[i].GetCaption()
                if not style & INB_FIT_BUTTON or (
                        style & INB_LEFT or (style & INB_RIGHT)):
                    fixedText = self.FixTextSize(dc, self._pagesInfoVec[
                        i].GetCaption(), self._nImgSize * 2 - 4)

                    # Update the length of the text
                    textWidth, textHeight = dc.GetTextExtent(fixedText)

                if bUseYcoord:

                    textOffsetX = ((rectWidth - textWidth) / 2)
                    textOffsetY = (not style & INB_SHOW_ONLY_TEXT and [
                        pos + self._nImgSize + imgTopPadding + 3] or \
                                   [pos + ((
                                                       self._nImgSize * 2 - textHeight) / 2)])[
                        0]

                else:

                    textOffsetX = (
                                              rectWidth - textWidth) / 2 + pos + nTextPaddingLeft
                    textOffsetY = (not style & INB_SHOW_ONLY_TEXT and [
                        self._nImgSize + imgTopPadding + 3] or \
                                   [((self._nImgSize * 2 - textHeight) / 2)])[0]

                dc.SetTextForeground(
                    wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
                dc.DrawText(fixedText, textOffsetX, textOffsetY)

            # Update the page info
            self._pagesInfoVec[i].SetPosition(buttonRect.GetPosition())
            self._pagesInfoVec[i].SetSize(buttonRect.GetSize())

            pos += rectWidth

        # Update all buttons that can not fit into the screen as non-visible
        for ii in range(count, len(self._pagesInfoVec)):
            self._pagesInfoVec[ii].SetPosition(wx.Point(-1, -1))

        # Draw the pin button
        if bUsePin:
            clientRect = self.GetClientRect()
            pinRect = wx.Rect(clientRect.GetX() + clientRect.GetWidth() - 20, 2,
                              20, 20)
            self.DrawPin(dc, pinRect, not self._bCollapsed)


class FlatImageBook(FlatBookBase):
    """
    Default implementation of the image book, it is like a :class:`Notebook`, except that
    images are used to control the different pages. This container is usually used
    for configuration dialogs etc.

    :note: Currently, this control works properly for images of size 32x32 and bigger.
    """

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0, agwStyle=0, name="FlatImageBook"):
        """
        Default class constructor.

        :param `parent`: parent window. Must not be ``None``;
        :param `id`: window identifier. A value of -1 indicates a default value;
        :param `pos`: the control position. A value of (-1, -1) indicates a default position,
         chosen by either the windowing system or wxPython, depending on platform;
        :param `size`: the control size. A value of (-1, -1) indicates a default size,
         chosen by either the windowing system or wxPython, depending on platform;
        :param `style`: the underlying :class:`Panel` window style;
        :param `agwStyle`: the AGW-specific window style. This can be a combination of the
         following bits:

         =========================== =========== ==================================================
         Window Styles               Hex Value   Description
         =========================== =========== ==================================================
         ``INB_BOTTOM``                      0x1 Place labels below the page area. Available only for :class:`FlatImageBook`.
         ``INB_LEFT``                        0x2 Place labels on the left side. Available only for :class:`FlatImageBook`.
         ``INB_RIGHT``                       0x4 Place labels on the right side.
         ``INB_TOP``                         0x8 Place labels above the page area.
         ``INB_BORDER``                     0x10 Draws a border around :class:`LabelBook` or :class:`FlatImageBook`.
         ``INB_SHOW_ONLY_TEXT``             0x20 Shows only text labels and no images. Available only for :class:`LabelBook`.
         ``INB_SHOW_ONLY_IMAGES``           0x40 Shows only tab images and no label texts. Available only for :class:`LabelBook`.
         ``INB_FIT_BUTTON``                 0x80 Displays a pin button to show/hide the book control.
         ``INB_DRAW_SHADOW``               0x100 Draw shadows below the book tabs. Available only for :class:`LabelBook`.
         ``INB_USE_PIN_BUTTON``            0x200 Displays a pin button to show/hide the book control.
         ``INB_GRADIENT_BACKGROUND``       0x400 Draws a gradient shading on the tabs background. Available only for :class:`LabelBook`.
         ``INB_WEB_HILITE``                0x800 On mouse hovering, tabs behave like html hyperlinks. Available only for :class:`LabelBook`.
         ``INB_NO_RESIZE``                0x1000 Don't allow resizing of the tab area.
         ``INB_FIT_LABELTEXT``            0x2000 Will fit the tab area to the longest text (or text+image if you have images) in all the tabs.
         ``INB_BOLD_TAB_SELECTION``       0x4000 Show the selected tab text using a bold font.
         =========================== =========== ==================================================

        :param `name`: the window name.
        """

        FlatBookBase.__init__(self, parent, id, pos, size, style, agwStyle,
                              name)

        self._pages = self.CreateImageContainer()

        if agwStyle & INB_LEFT or agwStyle & INB_RIGHT:
            self._mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        else:
            self._mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(self._mainSizer)

        # Add the tab container to the sizer
        self._mainSizer.Add(self._pages, 0, wx.EXPAND | wx.BOTTOM, 0)

        if agwStyle & INB_LEFT or agwStyle & INB_RIGHT:
            self._pages.SetSizeHints(self._pages.GetImageSize() * 2, -1)
        else:
            self._pages.SetSizeHints(-1, self._pages.GetImageSize() * 2)

        self._mainSizer.Layout()

    def CreateImageContainer(self):
        """ Creates the image container class for :class:`FlatImageBook`. """

        return ImageContainer(self, wx.ID_ANY,
                              agwStyle=self.GetAGWWindowStyleFlag())


class MyNotebook(FlatImageBook):
    """
    自定义的通用页面切换
    """

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0, agwStyle=LB.INB_TOP |
                                   LB.INB_SHOW_ONLY_TEXT |
                                   LB.INB_FIT_BUTTON |
                                   LB.INB_BOLD_TAB_SELECTION,
                 name="FlatImageBook"):
        super(MyNotebook, self).__init__(parent, id=id,
                                         pos=pos,
                                         size=size,
                                         style=style, agwStyle=agwStyle,
                                         name=name)
