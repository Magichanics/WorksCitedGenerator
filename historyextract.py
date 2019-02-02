'''
Name: Magichanics, vivekandathil
Date: January 31st, 2019

Sources:
https://geekswipe.net/technology/computing/analyze-chromes-browsing-history-with-python/
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import xml.etree.ElementTree as ET
# from xmljson import parker
# from json import dumps
# import requests
import os
import shutil
import sqlite3
import datetime
import platform
import pandas as pd

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

    # convert database to tuples
    def extract(self):
        c = sqlite3.connect(self.history_db)
        cursor = c.cursor()
        select_statement = "SELECT urls.url, urls.last_visit_time, urls.title " \
                           "FROM urls, visits WHERE urls.id = visits.url;"
        cursor.execute(select_statement)
        db_tuple = cursor.fetchall() # originally tuple

        # convert chrome timestamps into regular ones and place into separate lists
        db_timestamps = [self.chrome_to_real_time(n[1]) for n in db_tuple]
        db_names = [n[0] for n in db_tuple]
        db_urls = [n[2] for n in db_tuple]

        # store in dataframe
        history_df = pd.DataFrame({'names': db_names, 'timestamp': db_timestamps, 'urls': db_urls})

        return history_df

    def start(self):
        self.starting_history_df = self.database_extraction()
        self.starting_history_df.to_csv('assets\\starting_history.csv')

    def stop(self):
        self.ending_history_df = self.database_extraction()
        self.starting_history_df.to_csv('assets\\stopping_history.csv')

    # obtain history database
    def database_extraction(self):
        self.search()
        self.copy()
        self.search(data_path='assets', item='curr_history')
        return self.extract()

    def __init__(self):
        pass

# class XMLParsing:
#
#     def parse(self, url):
#         # Get content from provided URL
#         xmlFile = requests.get(url)
#
#         # Store binary data from url into xml file.
#         # 'wb' (write binary) is required to write the page contents to a file in XML format.
#         with open('feed.xml', 'wb') as file:
#             file.write(xmlFile.content)
#             print('XML file created and written')
#
#         # parse xml file, get the root, and store in a string
#         tree = ET.parse('feed.xml')
#         root = tree.getroot()
#         xmlstr = ET.tostring(root, encoding='utf8', method='xml')
#
#         # convert to JSON using dumps method, in "parker" format
#         a = dumps(parker.data(ET.fromstring(xmlstr)), sort_keys=True, indent=4, separators=(',', ': '))
#
#         # write to JSON file
#         with open('File.JSON', 'w') as outfile:
#             outfile.write((a))
#             print("JSON File written")  # Success message
#
#     def __init__(self):
#         pass

