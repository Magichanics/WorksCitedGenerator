'''
Name: Magichanics
February 3rd, 2019
'''
import requests
from newspaper import Article # use newspaper3k
import pythonwhois

class CiteURL:

    def get_publisher(self):
        pass

    def get_authors(self):
        return self.article.authors

    def get_date(self):
        return self.article.publish_date

    def __init__(self, url):

        # setup newspaper for parsing
        self.article = Article(url)
        self.article.download()
        self.article.html
        self.article.parse()

        pass

citations = CiteURL('https://www.macleans.ca/education/best-computer-science-universities-in-canada-2018-ranking/')
print(citations.get_authors())
# print(infoscrape.scrape('https://www.cnn.com/us/live-news/super-bowl-2019-updates/index.html'))

# page with multiple articles https://www.cnn.com/us/live-news/super-bowl-2019-updates/index.html
# 'https://www.macleans.ca/education/best-computer-science-universities-in-canada-2018-ranking/'
