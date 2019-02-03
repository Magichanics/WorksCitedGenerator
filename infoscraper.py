'''
Name: Magichanics
February 3rd, 2019
'''
# class InfoScraper:
#
#     def scrape(self, url):
#
#
#     def __init__(self):
#         pass

from six.moves import urllib
page = urllib.request.urlopen('https://stackoverflow.com/questions/1843422/get-webpage-contents-with-python')
print(page.read())