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

class HistoryExtract:

    # search for history database
    def search(self, data_path=os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default",
               item='history'):
        files = os.listdir(data_path)
        self.history_db = os.path.join(data_path, item)

    # extract to make sure
    def copy(self):
        try:
            shutil.copy(self.history_db, 'assets\\curr_history')
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())

    # convert database to tuples
    def extract(self):
        c = sqlite3.connect(self.history_db)
        cursor = c.cursor()
        select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
        cursor.execute(select_statement)
        self.db_tuple = cursor.fetchall() # tuple

    def __init__(self):

        # obtain history database
        print('intitalizing')
        self.search()
        self.copy()
        self.search(data_path='assets', item='curr_history')
        self.extract()
#
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

