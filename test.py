'''
Name: Magichanics
Date: February 9th, 2019
'''
from main import WorksCitedGenerator
from historyextract import HistoryExtract
import sys
import pandas as pd

# generate works cited page
def generate_wcp(url_df, location):
    wcg = WorksCitedGenerator(url_df)
    wcg.get_attributes()
    print(wcg.url_df)
    print(wcg.url_df['timestamp_publication'])
    wcg.citation_generator(location)

'''
Uses Google Chrome History to create the citations
'''
def test_history_extraction():

    # extract history and save
    historyextractor = HistoryExtract()
    historyextractor.stop(save_all=True)

    # save only the first 10 urls
    test_history_df = historyextractor.history_df.head(10).copy()

    generate_wcp(test_history_df, 'WorksCited_History.docx')

'''
First line should include n, which is the number of URLs.
For the next n+1 lines, input the URLs.
'''
def test_manual_input():

    print('Please enter input:')

    # obtain input
    n = int(sys.stdin.readline())
    urls = []
    for _ in range(n):
        urls.append(sys.stdin.readline())

    # convert to dataframe
    url_df = pd.DataFrame({'url': urls})

    generate_wcp(url_df, 'WorksCited_Manual.docx')

if __name__ == "__main__":
    test_manual_input()
    # test_history_extraction()



