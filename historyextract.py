'''
Name: Magichanics
Date: January 31st, 2019
'''

import os
import shutil
import sqlite3
import datetime
import platform
import pandas as pd
import warnings
from citeurl import CiteURL

class HistoryExtract:

    # search for history database
    def search(self, data_path=os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default",
               item='history'):
        files = os.listdir(data_path)
        self.history_db = os.path.join(data_path, item)

    # copy the history file so we don't view the history file that could be currently be in use by Google Chrome
    def copy(self):
        shutil.copy(self.history_db, 'assets\\curr_history')

    # converts chrome microseconds into realtime timestamps
    def chrome_to_real_time(self, microseconds):
        return datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=microseconds)

    # extract the authors and date of publication
    def extract_author_date(self, url):
        xmlFile = requests.get(url)

    # convert database to tuples to dataframe
    def extract(self):
        c = sqlite3.connect(self.history_db)
        cursor = c.cursor()
        select_statement = "SELECT urls.url, urls.last_visit_time, urls.title " \
                           "FROM urls, visits WHERE urls.id = visits.url;"
        cursor.execute(select_statement)
        db_tuple = cursor.fetchall() # originally tuple

        # convert chrome timestamps into regular ones and place into separate lists
        db_timestamps = [self.chrome_to_real_time(n[1]) for n in db_tuple]
        db_names = [n[2] for n in db_tuple]
        db_urls = [n[0] for n in db_tuple]

        # # convert to lowercase
        # db_names = [n.lower() for n in db_names]

        # store in dataframe
        history_df = pd.DataFrame({'name': db_names, 'timestamp_access': db_timestamps, 'url': db_urls})

        # remove duplicate urls
        history_df = history_df.drop_duplicates(subset=['url'],keep='last')

        return history_df

    # save start of time
    def start(self):
        self.starting_time = datetime.datetime.now()

    def stop(self, stopping_time=datetime.datetime.now(), save_all=False):

        # load database for usage
        self.history_df = self.database_extraction()

        # get all rows that are within the two given timestamps (try and combine this into one line for efficiency)
        if not save_all:
            self.history_df = self.history_df[self.history_df.timestamp_access >= self.starting_time]
            self.history_df = self.history_df[self.history_df.timestamp_access <= stopping_time]

    # NOTE: This requires the stop function to be played first before this function could go.
    def filter(self, tag, cols=['name'], save_to_obj=True):

        # associate local variable with the main dataframe
        local_history_df = self.history_df.copy()

        # check if tag is in the string
        def check_string(x):
            for f in cols:
                if tag in x[f]:
                    return True
            return False

        # apply to all columns
        local_history_df['valid'] = local_history_df[cols].apply(check_string,axis=1)
        local_history_df = local_history_df[local_history_df.valid == False]
        del local_history_df['valid']

        # reset index due to the possible missing links
        local_history_df = local_history_df.reset_index(drop=True)

        # return dataframe
        if not save_to_obj:
            return local_history_df
        else:
            self.history_df = local_history_df

    # obtain history database
    def database_extraction(self):
        self.search()
        self.copy()
        self.search(data_path='assets', item='curr_history')
        return self.extract()

    # get starting time
    def __init__(self):
        self.starting_time = datetime.datetime.now()

