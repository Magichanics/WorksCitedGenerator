'''
Name: Jan Garong
Date: January 31st, 2019
'''

from citeurl import CiteURL
from doccreation import WorksCited

class WorksCitedGenerator:

    def get_attributes(self):

        self.url_df['CiteURL_obj'] = self.url_df['url'].apply(CiteURL)

        # apply attributes
        self.url_df['authors'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_authors())
        self.url_df['name'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_name())
        self.url_df['timestamp_publication'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_date())

        # check if there are nulls per row
        self.url_df['Warning'] = self.url_df.apply(lambda x:any(x.isnull()),axis=1)

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

