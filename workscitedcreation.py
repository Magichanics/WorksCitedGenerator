'''
Name: Magichanics
Date: February 6th, 2019

Some notes:
Works Cited (centered)
Margin is 0.5
Author, "Title" Publisher, (Year, Month Day), URL

'''

from docx import Document
from docx.shared import Pt
from docx.text.parfmt import ParagraphFormat
from docx.enum.text import WD_LINE_SPACING
from docx.enum.text import WD_ALIGN_PARAGRAPH
import datetime

class WorksCited:

    # month integers to month names
    to_month = {'01': 'January',
                '02': 'February',
                '03': 'March',
                '04': 'April',
                '05': 'May',
                '06': 'June',
                '07': 'July',
                '08': 'August',
                '09': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December'}

    def time_to_string(self, datetime_input):

        # convert to list
        date_string = datetime_input.strftime("%Y-%m-%d")
        date_lst = date_string.split('-')

        # use dictionary to get name
        date_lst[1] = to_month[date_lst[1]]

        # get rid of trailing zeros
        date_lst[2] = str(int(date_lst[2]))

        # combine them together (use regex please)
        return '(' + date_lst[0] + ', ' + date_lst[1] + ' ' + date_lst[2] + ')'


    # add a new citation (needs name, date of publication/date of access, url, author/publisher)
    def add_citation(self):
        p = self.document.add_paragraph('Author, "Title", ')
        p.add_run('Publisher').italic = True
        p.add_run(' Date, URL')

    # sets font to Times New Roman, 12
    def set_font(self):
        style = self.document.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(12)

    # save document
    def save(self):
        self.document.save('WorksCited.docx')

    # initialize works cited page
    def __init__(self):

        self.document = Document()

        # create title page
        self.set_font()
        p = self.document.add_paragraph("Works Cited")
        p.style = self.document.styles['Normal']
        p.line_spacing_rule = WD_LINE_SPACING.DOUBLE
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
