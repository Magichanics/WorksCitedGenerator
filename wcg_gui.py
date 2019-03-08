'''
Name: Jan Garong
Date: February 10th, 2019

based off of example: https://www.blog.pythonlibrary.org/2011/08/20/wxpython-new-widget-announced-xlsgrid/
'''
import pandas as pd

# GUI
import wx
import xlrd
from wx.lib.agw import xlsgrid as XG

class WCG_Form(wx.Frame):

    def __init__(self):

        # create new frame
        wx.Frame.__init__(self, None, wx.ID_ANY, "Works Cited Generator")
        panel = wx.Panel(self, wx.ID_ANY)

        # access csv file
        book = xlrd.open_workbook("assets/metadata.xml", formatting_info=1)
        sheetname = "Works Cited Metadata"
        sheet = book.sheet_by_name(sheetname)

        # determine dimensions
        rows, cols = sheet.nrows, sheet.ncols
        comments, texts = XG.ReadExcelCOM(filename, sheetname, rows, cols)

        xlsGrid = XG.XLSGrid(panel)
        xlsGrid.PopulateGrid(book, sheet, texts, comments)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(xlsGrid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = WCG_Form().Show()
    app.MainLoop()
