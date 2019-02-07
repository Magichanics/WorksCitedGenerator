'''
Name: Magichanics
Date: January 31st, 2018
'''

from historyextract import HistoryExtract
from citeurl import CiteURL
from newspaper import Article

def news(df):
    pass

def to_cite(df):

    # get author and date
    df['CiteURL_obj'] = df['url'].apply(lambda x: CiteURL(x))
    df['timestamp_publication'] = df['CiteURL_obj'].apply(lambda x: x.get_date())
    df['author'] = df['CiteURL_obj'].apply(lambda x: x.get_authors())
    del df['CiteURL_obj']

    return df

historyextractor = HistoryExtract()
historyextractor.stop(save_all=True)
historyextractor.filter('google', cols=['name', 'url'])
print(historyextractor.history_df)
print('getting more information')
print(to_cite(historyextractor.history_df.head(50)).dropna())


