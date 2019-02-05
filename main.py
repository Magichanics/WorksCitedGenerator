'''
Name: Magichanics
Date: January 31st, 2018
'''

from historyextract import HistoryExtract

historyextractor = HistoryExtract()
# historyextractor.filter('dab', cols=['url'])
historyextractor.stop(save_all=True)
historyextractor.filter('My Drive - Google Drive', cols=['name'])
print(historyextractor.history_df)
