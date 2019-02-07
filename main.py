'''
Name: Magichanics
Date: January 31st, 2019
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
test_history_df = historyextractor.history_df.head(100)
print(to_cite(test_history_df).dropna())


