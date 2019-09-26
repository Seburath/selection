import requests
import csv
from bs4 import BeautifulSoup
import os
import pandas as pd 

file = open('symbols.csv', 'w')
file.truncate()
writer = csv.writer(file)
values_exchange = []

class Exchange:
    def __init__(self,url,page_max,ran_endC,name_exchange):
        self.url=url
        self.page_max=page_max
        self.ran_endC=ran_endC
        self.name_exchange=name_exchange
        
    def extract_data(self):
        for page in range(1, self.page_max):
            response  = requests.get(self.url + str(page))
            data = response.text
            soup = BeautifulSoup(data, features='lxml')
            html = str(soup.contents)
            html_preprocess = html.split('<td>')
            if page < self.page_max-1:
                ran_ini = 3
                ran_end = 400
            else:
                ran_ini = 3
                ran_end = self.ran_endC
            for i in range(ran_ini,ran_end)[0::4]:
                values = (html_preprocess[i][:-6], 'STK', 'SMART', html_preprocess[i+1][:3])
                if values not in values_exchange:
                    print(i, self.name_exchange, values)
                    values_exchange.append(values)

urls=['https://www.interactivebrokers.com/en/index.php?f=2222&exch=nasdaq&showcategories=STK&p=&cc=&limit=100&page=','https://www.interactivebrokers.com/en/index.php?f=2222&exch=nyse&showcategories=STK&p=&cc=&limit=100&page=','https://www.interactivebrokers.com/en/index.php?f=2222&exch=amex&showcategories=STK&p=&cc=&limit=100&page=']
exchange_nasdaq=Exchange(urls[0],35,15,'NASDAQ')                    
exchange_nasdaq.extract_data()

exchange_nyse=Exchange(urls[1],87,372,'NYSE')                    
exchange_nyse.extract_data()

exchange_amex=Exchange(urls[2],87,368,'AMEX')                    
exchange_amex.extract_data()
