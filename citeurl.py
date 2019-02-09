'''
Name: Magichanics
Date: February 3rd, 2019
'''
# import requests
#from newspaper import Article # use newspaper3k
import newspaper
import whois # python-whois
import numpy as np

class CiteURL:

    # use whois module to obtain publisher (use either registrar or registrant name)
    def get_publisher(self):
        # get whois information
        url_whois = whois.whois(self.url)
        try:
            return url_whois['registrant_name'][0]
        except KeyError:
            try:
                return url_whois['registrar']
            except KeyError:
                return np.nan

    # return given properties using newspaper module
    def get_authors(self):
        if self.article == None:
            return np.nan
        return self.article.authors

    def get_date(self):
        if self.article == None:
            return np.nan
        return self.article.publish_date

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


citations = CiteURL('https://www.bloomberg.com/profiles/companies/756657Z:US-markmonitor-inc')
print(citations.get_publisher())
# print(citations.get_publisher())

