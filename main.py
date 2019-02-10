'''
Name: Magichanics
Date: January 31st, 2019
'''

from citeurl import CiteURL
from doccreation import WorksCited

class WorksCitedGenerator:

    def get_attributes(self):

        # get citation object (better than redownloading websites per attribute)
        self.url_df['CiteURL_obj'] = self.url_df['url'].apply(lambda x: CiteURL(x))

        # apply attributes
        self.url_df['timestamp_publication'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_date())
        self.url_df['authors'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_authors())
        self.url_df['name'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_name())

        # delete citation object
        del self.url_df['CiteURL_obj']

    def citation_generator(self, save_location='WorksCited.docx'):

        # replace nulls with zeroes.
        self.url_df = self.url_df.fillna(0)

        # create new works cited sheet
        wc = WorksCited()

        # add citation per row with the given attributes
        def cite_to_sheet(x):
            wc.add_citation(x.authors, x.timestamp_publication, x['name'], x.url)
        self.url_df.apply(cite_to_sheet, axis=1)

        # save based on given file location
        wc.save(save_location)

    def __init__(self, df):

        # dataframe must have a column of urls
        self.url_df = df

