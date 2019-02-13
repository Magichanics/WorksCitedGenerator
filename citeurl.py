'''
Name: Jan Garong
Date: February 3rd, 2019

format:
https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/general_format.html

using beautifulsoup4 not BeautifulSoup

note: compare the two methods; beautifulsoup + urllib2 vs. mechanize for fetching webpage titles
'''
# import requests
#from newspaper import Article # use newspaper3k
# import whois # python-whois
# from mechanize import Browser
from newspaper import Article
import numpy as np
import requests
from lxml.html import fromstring
from bs4 import BeautifulSoup
import urllib
from threading import Thread, Event
import time

# for websites that take way too long
import multiprocessing
import time

class CiteURL:

    # # use whois module to obtain publisher (use either registrar or registrant name)
    # def get_publisher(self):
    #     # get whois information
    #     url_whois = whois.whois(self.url)
    #     try:
    #         return url_whois['registrant_name'][0]
    #     except KeyError:
    #         try:
    #             return url_whois['registrar']
    #         except KeyError:
    #             return np.nan

    # def get_authors_html(self, htmlfile):
    #
    #     # "author": x, is what we'll be looking for
    #     # look for starting index that contains "author:"
    #     idx = htmlfile.find('"author":')
    #     author_part = htmlfile[idx:]
    #
    #     # look for comma, and have the string only include the content in "author":
    #     idx_x = author_part.find(',')
    #     author_part = author_part[:idx_x][10:].strip('"')
    #     print(author_part)


    # return given properties using newspaper module
    def get_authors(self):

        try:
            # use library to get authors
            authors = self.article.authors

            # check if it is in the list of banned "authors":
            if 'About Us' in authors:
                authors.remove('About Us')

            return ''.join(str(a) + ', ' for a in authors)[:-2]
        except:
            return np.nan

    # get the publishing date
    def get_date(self):
        try:
            return self.article.publish_date
        except:
            return np.nan

    # this cannot be null?
    def get_name(self):

        # use BeautifulSoup and urllib to get the title
        try:
            soup = BeautifulSoup(urllib.request.urlopen(self.url))
            return soup.title.string
        except:
            return ''

        # # method 2: using requests to fetch article title
        # except urllib.error.HTTPError:
        #     print('Method 1 failed. Trying Method 2.')
        #     print('Issues with URL: ' + self.url)
        #     self.status = 'Warning'
        #
        #     # return self.article.title # find another way to fetch the title (can be inaccurate)
        #     r = requests.get(self.url)
        #     tree = fromstring(r.content)
        #     return tree.findtext('.//title')

    def timeout(self, function):

        # create thread
        action_thread = Thread(target=function)

        # start timer
        action_thread.start()
        action_thread.join(timeout=2)

        # tell the function to stop
        self.stop_event.set()

    def download_article(self):
        # check if it will download; if it won't, leave it blank
        try:

            # download and parse article
            self.article.download()
            self.article.html
            self.article.parse()

            # if it takes too long
            if self.stop_event.is_set():
                self.article = np.nan

        except:
            self.article = np.nan

    # setup url for parsing
    def __init__(self, url):

        # check if empty
        if url == '':
            self.article = None

        # get webpage
        self.url = url
        self.article = Article(url)

        # download article without timeout
        #self.download_article()

        # declare event
        self.stop_event = Event()

        # download article with timeout
        self.timeout(self.download_article)




