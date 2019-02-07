'''
Name: Magichanics
Date: February 3rd, 2019
'''
# import requests
#from newspaper import Article # use newspaper3k
import newspaper
# import pythonwhois
import numpy as np

class CiteURL:

    # def get_publisher(self):
    #     return pythonwhois.get_whois(self.url)

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


# citations = CiteURL('https://www.macleans.ca/education/best-computer-science-universities-in-canada-2018-ranking/')
# print(citations.get_authors())
# print(citations.get_publisher())

