'''
Name: Jan Garong
Date: March 9th, 2019
'''

from __init__ import WorksCitedGenerator
from historyextract import HistoryExtract
import pandas as pd
import wx

class WCGSimple_Form(wx.Frame):

    def __init__(self):

        # setup window
        wx.Frame.__init__(self, None, wx.ID_ANY, "Works Cited Generator")
        panel = wx.Panel(self, wx.ID_ANY)

        # create layout
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # create textbox
        self.text_input = wx.TextCtrl(panel, size=(640, 400), style=wx.TE_MULTILINE)
        vbox.Add(self.text_input, wx.ALIGN_CENTER)

        # create buttons
        hbox.Add(1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.btn_csv = wx.Button(panel, -1, "Get CSV Metadata")
        #hbox.Add(self.btn_csv, wx.ALIGN_CENTER)
        hbox.Add(self.btn_csv,1, wx.EXPAND | wx.ALIGN_RIGHT | wx.ALL, 5)
        self.btn_wcs = wx.Button(panel, -1, "Get Works Cited Sheet")
        #hbox.Add(self.btn_wcs, wx.ALIGN_CENTER)
        vbox.Add(hbox)

        self.Fit()

    # create app
if __name__ == "__main__":

    # create app window
    app = wx.App()
    frame = WCGSimple_Form()

    # set dimensions and position
    frame.SetDimensions(0, 0, 640, 480)
    frame.Centre()

    # show and iterate
    frame.Show()
    app.MainLoop()