'''
Name: Jan Garong
Date: March 8th, 2019

based off of example: https://www.blog.pythonlibrary.org/2011/08/20/wxpython-new-widget-announced-xlsgrid/


------------------------------------------------------------------------------------------------------------------------

Note: please modify zlsgrid.py at line 1975

if not current == None:
    col_width = int(round(float(default_width)*current/256.0))
else:
    col_width = 20

------------------------------------------------------------------------------------------------------------------------
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
        book = xlrd.open_workbook("assets/metadata.xls", formatting_info=1)

        # obtain sheet and sheet name
        sheetname = book.sheet_names()[0]
        sheet = book.sheet_by_name(book.sheet_names()[0])

        # determine dimensions
        rows, cols = sheet.nrows, sheet.ncols
        comments, texts = XG.ReadExcelCOM("assets/metadata.xls", sheetname, rows, cols)

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
