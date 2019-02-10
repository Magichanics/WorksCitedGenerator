'''
Name: Magichanics
Date: February 3rd, 2019

format:
https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_formatting_and_style_guide/general_format.html

using beautifulsoup4 not BeautifulSoup

note: compare the two methods; beautifulsoup + urllib2 vs. mechanize for fetching webpage titles
'''
# import requests
#from newspaper import Article # use newspaper3k
import newspaper
import whois # python-whois
import numpy as np
from bs4 import BeautifulSoup
import urllib
# from mechanize import Browser

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

    # return given properties using newspaper module
    def get_authors(self):

        # we need two if statements to prevent an attribute error from occuring.
        # check if empty
        if self.article == None:
            return np.nan
        # check if not doable
        elif self.article.authors == None:
            return np.nan

        return ''.join(str(a) + ', ' for a in self.article.authors)[:-2]

    def get_date(self):

        # check if empty
        if self.article == None:
            return np.nan
        # check if not doable
        if self.article.publish_date == None:
            return np.nan

        return self.article.publish_date

    # this cannot be null.
    def get_name(self):
        soup = BeautifulSoup(urllib.request.urlopen(self.url))
        return soup.title.string

    # setup url for parsing
    def __init__(self, url):

        self.url = url
        self.article = newspaper.Article(url)

        # check if it will download; if it won't, leave it blank
        try:
            # download and parse article
            self.article.download()
            self.article.html
            self.article.parse()
        except newspaper.article.ArticleException:
            self.article = None



