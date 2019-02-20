'''
Name: Jan Garong
Date: February 3rd, 2019

format:
https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/general_format.html

using beautifulsoup4 not BeautifulSoup

note: compare the two methods; beautifulsoup + urllib2 vs. mechanize for fetching webpage titles
'''
# import requests
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

    # main function to get the name of the article
    def get_name(self):

        # get name of the article through goose library
        def get_name_goose():
            g = Goose()
            g_article = g.extract(self.url)
            return g_article.title

        # get name of the article through urllib and beautifulsoup
        def get_name_soup():
            soup = BeautifulSoup(urllib.request.urlopen(self.url))
            return soup.title.string

        # use various methods to fetch the title
        try:
            return get_name_soup()
        except:
            try:
                return get_name_goose()
            except:
                print('fail at ' + self.url)
                return ''

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




