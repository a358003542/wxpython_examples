#!/usr/bin/env python
# -*-coding:utf-8-*-

import wx

import wx.lib.agw.gradientbutton as GB
import wx.lib.buttons as buttons


class MySimpleButton(buttons.GenButton):
    def __init__(self, parent, background_color='', font_color='black',
                 **kwargs):
        super(MySimpleButton, self).__init__(parent, **kwargs)

        self.background_color = background_color

        if background_color:
            self.SetBackgroundColour(wx.Colour(background_color))

        self.SetForegroundColour(font_color)


class MyGradientButton(GB.GradientButton):
    def __init__(self, parent, id=wx.ID_ANY, bitmap=None, label="", toolTip="",
                 color='buttonBack',
                 background_color='',
                 font_color='white', font_bold=True, font_size=9, radius=8,
                 pos=wx.DefaultPosition,
                 size=(95, 32), style=wx.NO_BORDER, align=wx.CENTER,
                 validator=wx.DefaultValidator,
                 name="gradientbutton"):
        super(MyGradientButton, self).__init__(parent, id=id, bitmap=bitmap,
                                               label=label, pos=pos,
                                               size=size, style=style,
                                               align=align, validator=validator,
                                               name=name)

        self.radius = radius
        self.color = color
        self.background_color = background_color

        buttonFont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)

        if font_bold:
            buttonFont.SetWeight(wx.FONTWEIGHT_BOLD)
        if font_size:
            buttonFont.SetPointSize(font_size)

        self.SetFont(buttonFont)
        self.SetForegroundColour(font_color)

        self.SetTopStartColour(wx.Colour(color))
        self.SetBottomStartColour(wx.Colour(color))

        self.SetPressedTopColour(wx.Colour(color))
        self.SetPressedBottomColour(wx.Colour(color))

        self.SetTopEndColour(wx.Colour(color))
        self.SetBottomEndColour(wx.Colour(color))

        if background_color:
            self.SetBackgroundColour(wx.Colour(background_color))

        if toolTip:
            self.SetToolTip(toolTip)

    def Disable(self):
        """
        disables the button.

        :note: Overridden from :class:`wx.Control`.
        """

        wx.Control.Enable(self, False)
        self.change_color('gray')

        self.Refresh()

    def Enable(self, enable=True):
        """
        Enables/disables the button.

        :param `enable`: ``True`` to enable the button, ``False`` to disable it.

        :note: Overridden from :class:`wx.Control`.
        """

        wx.Control.Enable(self, enable)
        self.change_color(self.color)
        self.Refresh()

    def change_color(self, color):
        self.SetTopStartColour(wx.Colour(color))
        self.SetBottomStartColour(wx.Colour(color))

        self.SetPressedTopColour(wx.Colour(color))
        self.SetPressedBottomColour(wx.Colour(color))

        self.SetTopEndColour(wx.Colour(color))
        self.SetBottomEndColour(wx.Colour(color))

        self.Refresh()

    def change_font_color(self, font_color):
        self.font_color = font_color
        self.SetForegroundColour(font_color)
        self.Refresh()

    def change_background_color(self, background_color):
        self.background_color = background_color
        self.SetBackgroundColour(wx.Colour(background_color))
        self.Refresh()

    def OnPaint(self, event):
        """
        Handles the ``wx.EVT_PAINT`` event for :class:`GradientButton`.

        :param `event`: a :class:`PaintEvent` event to be processed.
        """

        dc = wx.BufferedPaintDC(self)
        gc = wx.GraphicsContext.Create(dc)

        if self.background_color:
            dc.SetBackground(wx.Brush(self.background_color))
        else:
            dc.SetBackground(wx.Brush(self.GetParent().GetBackgroundColour()))
        dc.Clear()

        clientRect = self.GetClientRect()
        gradientRect = wx.Rect(*clientRect)
        capture = wx.Window.GetCapture()

        x, y, width, height = clientRect

        gradientRect.SetHeight(gradientRect.GetHeight() / 2 + (
        (capture == self and [1] or [0])[0]))
        if capture != self:
            if self._mouseAction == GB.HOVER:
                topStart, topEnd = self.LightColour(self._topStartColour,
                                                    5), self.LightColour(
                    self._topEndColour, 5)
            else:
                topStart, topEnd = self._topStartColour, self._topEndColour

            rc1 = wx.Rect(x, y, width, height / 2)
            path1 = self.GetPath(gc, rc1, self.radius)
            br1 = gc.CreateLinearGradientBrush(x, y, x, y + height / 2,
                                               topStart, topEnd)
            gc.SetBrush(br1)
            gc.FillPath(path1)  # draw main

            path4 = gc.CreatePath()
            path4.AddRectangle(x, y + height / 2 - 8, width, 8)
            path4.CloseSubpath()
            gc.SetBrush(br1)
            gc.FillPath(path4)

        else:

            rc1 = wx.Rect(x, y, width, height)
            path1 = self.GetPath(gc, rc1, 8)
            gc.SetPen(wx.Pen(self._pressedTopColour))
            gc.SetBrush(wx.Brush(self._pressedTopColour))
            gc.FillPath(path1)

        gradientRect.Offset((0, gradientRect.GetHeight()))

        if capture != self:

            if self._mouseAction == GB.HOVER:
                bottomStart, bottomEnd = self.LightColour(
                    self._bottomStartColour, 5), self.LightColour(
                    self._bottomEndColour, 5)
            else:
                bottomStart, bottomEnd = self._bottomStartColour, self._bottomEndColour

            rc3 = wx.Rect(x, y + height / 2, width, height / 2)
            path3 = self.GetPath(gc, rc3, self.radius)
            br3 = gc.CreateLinearGradientBrush(x, y + height / 2, x, y + height,
                                               bottomStart, bottomEnd)
            gc.SetBrush(br3)
            gc.FillPath(path3)  # draw main

            path4 = gc.CreatePath()
            path4.AddRectangle(x, y + height / 2, width, 8)
            path4.CloseSubpath()
            gc.SetBrush(br3)
            gc.FillPath(path4)

            shadowOffset = 0
        else:

            rc2 = wx.Rect(x + 1, gradientRect.height / 2, gradientRect.width,
                          gradientRect.height)
            path2 = self.GetPath(gc, rc2, self.radius)
            gc.SetPen(wx.Pen(self._pressedBottomColour))
            gc.SetBrush(wx.Brush(self._pressedBottomColour))
            gc.FillPath(path2)
            shadowOffset = 1

        font = gc.CreateFont(self.GetFont(), self.GetForegroundColour())
        gc.SetFont(font)
        label = self.GetLabel()
        tw, th = gc.GetTextExtent(label)

        if self._bitmap:
            bw, bh = self._bitmap.GetWidth(), self._bitmap.GetHeight()
        else:
            bw = bh = 0

        if self._alignment == wx.CENTER:
            pos_x = (
                                width - bw - tw) / 2 + shadowOffset  # adjust for bitmap and text to centre
            if self._bitmap:
                pos_y = (height - bh) / 2 + shadowOffset
                gc.DrawBitmap(self._bitmap, pos_x, pos_y, bw,
                              bh)  # draw bitmap if available
                pos_x = pos_x + 2  # extra spacing from bitmap
        elif self._alignment == wx.LEFT:
            pos_x = 3  # adjust for bitmap and text to left
            if self._bitmap:
                pos_y = (height - bh) / 2 + shadowOffset
                gc.DrawBitmap(self._bitmap, pos_x, pos_y, bw,
                              bh)  # draw bitmap if available
                pos_x = pos_x + 3  # extra spacing from bitmap

        gc.DrawText(label, pos_x + bw + shadowOffset,
                    (height - th) / 2 + shadowOffset)

    def LightColour(self, colour, percent):
        """
        重载行为为增加灰度
        Return light contrast of `colour`. The colour returned is from the scale of
        `colour` ==> black.

        :param `colour`: the input colour to be brightened;
        :param `percent`: determines how light the colour will be. `percent` = 100
         returns white, `percent` = 0 returns `colour`.
        """

        end_colour = wx.BLACK
        rd = end_colour.Red() - colour.Red()
        gd = end_colour.Green() - colour.Green()
        bd = end_colour.Blue() - colour.Blue()
        high = 100

        # We take the percent way of the colour from colour -. black
        i = percent
        r = colour.Red() + ((i * rd * 100) / high) / 100
        g = colour.Green() + ((i * gd * 100) / high) / 100
        b = colour.Blue() + ((i * bd * 100) / high) / 100
        a = colour.Alpha()

        return wx.Colour(int(r), int(g), int(b), int(a))
