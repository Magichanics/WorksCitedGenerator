'''
Name: Magichanics
Date: February 6th, 2019
'''

from docx import Document
from docx.shared import Pt
from docx.text.parfmt import ParagraphFormat

class WorksCited:

    # sets font to Times New Roman, 12
    def set_font(self):
        style = self.document.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(12)

    # initialize works cited page
    def __init__(self):

        self.document = Document()

        # create title page
        self.set_font()
        p.style = self.document.styles['Normal']
        p.format = self.document.format['']
        p = self.document.add_paragraph("Works Cited")
