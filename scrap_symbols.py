import requests
from bs4 import BeautifulSoup
# new imports
import pandas as pd
import pandas.io.sql as pd_sql
import sqlite3 as sql

'''
    Author: @pedrojsalinas
    Location: Loja, Ecuador
    Telephone: 0959776995
    Git: https://github.com/pedrojsalinas
    -------------------------------------
    Python 3
    install requirements -> requirements.txt
    pip install -r requirements.txt
'''
class ScrapperBS4():
    '''
        Class with variables and functions to make scrapy with BS4
    '''
    list = []
    # headers
    columns = ["IB_Symbol",
               "Description", "Symbol", "Currency"]
    # Dictionary with data of the exchanges
    dicExc = {
        'Nasdaq': {
            'url': 'https://www.interactivebrokers.com/en/index.php?f=2222&exch=nasdaq&showcategories=STK&p=&cc=&limit=100&page=',
            'minP': 1,
            'maxP': 35,
            'ran_end': 15,
        },
        'Nyse': {
            'url': 'https://www.interactivebrokers.com/en/index.php?f=2222&exch=nyse&showcategories=STK&p=&cc=&limit=100&page=',
            'minP': 1,
            'maxP': 87,
            'ran_end': 372,
        },
        'Amex': {
            'url': 'https://www.interactivebrokers.com/en/index.php?f=2222&exch=amex&showcategories=STK&p=&cc=&limit=100&page=',
            'minP': 1,
            'maxP': 87,
            'ran_end': 368,
        }
    }

    def ScrapyExchanges(self):
        '''
            Data scraper using BS4
        '''
        ran_ini = 3
        # loop dictionary of exchanges
        for exc in self.dicExc:
            url = self.dicExc[exc]['url']
            minP = self.dicExc[exc]['minP']
            maxP = self.dicExc[exc]['maxP']
            for page in range(minP, maxP):
                # scrapy
                r = requests.get(url+str(page))
                data = r.text
                soup = BeautifulSoup(data, features='lxml')
                x = self.cleanData(soup.contents)
                val = (self.dicExc[exc]['maxP'] - 1)
                if page < val:
                    ran_end = 400
                else:
                    ran_end = self.dicExc[exc]['ran_end']
                self.insertValues(x, ran_ini, ran_end)
        # save data
        self.saveCsv()
        self.saveDB()

    def cleanData(self, content):
        '''
            return clean data as string
        '''
        return str(content).split('<td>')

    def insertValues(self, x, min, max):
        '''
            insert values in array
        '''
        for i in range(min, max)[0::4]:
            vals = x[i][:-6], 'STK', 'SMART', x[i+1][:3]
            if vals not in self.list:
                self.list.append(vals)

    def saveCsv(self):
        '''
            save data as csv with header using pandas
        '''
        df = pd.DataFrame(self.list)
        # write dataframe to csv
        df.to_csv('symbols.csv', index=False, header=self.columns)

    def saveDB(self):
        '''
            Save data as sqlite3 DB,
            generate a file call exchanges.db
        '''
        conn = sql.connect('exchanges.db')
        df = pd.DataFrame(self.list)
        df.columns = self.columns
        # write dataframe to sqlite
        df.to_sql('exchanges.db', conn, if_exists='replace',
                  index=False)

if __name__ == "__main__":
    # initialize class
    scrap = ScrapperBS4()
    # call scrapy function
    scrap.ScrapyExchanges()
