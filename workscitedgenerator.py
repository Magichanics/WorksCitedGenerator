'''
Author: Jan Garong
Date: January 31st, 2019
'''

from citeurl import CiteURL
from doccreation import WorksCited
import pandas as pd
import numpy as np
from datetime import datetime

class WorksCitedGenerator:

    def get_attributes(self):

        self.url_df['CiteURL_obj'] = self.url_df['url'].apply(CiteURL)

        # apply attributes
        self.url_df['authors'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_authors())
        self.url_df['name'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_name())
        self.url_df['timestamp'] = self.url_df['CiteURL_obj'].apply(lambda x: x.get_date())

        # # check if there are nulls per row
        # self.url_df['Warning'] = self.url_df.apply(lambda x:any(x.isnull()),axis=1)

        # delete citation object
        del self.url_df['CiteURL_obj']

    def export_table(self, location="assets/metadata.csv"):

        # get time attributes
        def get_date_attribute(x, type):

            try:
                if type == "year":
                    return x.year

                elif type == "month":
                    return x.month

                elif type == "day":
                    return x.day

            # if it doesn't exist, return null
            except:
                return np.nan

        # expand time and remove timestamp
        self.url_df['year'] = self.url_df['timestamp'].apply(lambda x: get_date_attribute(x, "year"))
        self.url_df['month'] = self.url_df['timestamp'].apply(lambda x: get_date_attribute(x, "month"))
        self.url_df['day'] = self.url_df['timestamp'].apply(lambda x: get_date_attribute(x, "day"))

        del self.url_df['timestamp']

        # export csv
        self.url_df.to_csv(location)

    def import_table(self, location="assets/metadata.csv"):

        # import csv
        self.url_df = pd.read_csv(location)

        def ints_to_timestamp(x):

            # check if timestamp exist
            try:
                return datetime(year=x.year, month=x.month, day=x.day)
            except:
                return np.nan

        # convert time columns into datetime formats
        self.url_df['timestamp'] = self.url_df[['year', 'month', 'day']].apply(ints_to_timestamp,axis=1)

        # remove extra columns
        del self.url_df['year']
        del self.url_df['month']
        del self.url_df['day']

    def citation_generator(self, save_location='WorksCited.docx'):

        # replace nulls with zeroes.
        self.url_df = self.url_df.fillna(0)

        # create new works cited sheet
        wc = WorksCited()

        # add citation per row with the given attributes
        def cite_to_sheet(x):
            wc.add_citation(x.authors, x.timestamp, x['name'], x.url)
        self.url_df.apply(cite_to_sheet, axis=1)

        # save based on given file location
        wc.save(save_location)

    def __init__(self):

        pass




