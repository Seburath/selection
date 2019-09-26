# -*- coding: utf-8 -*-
from urllib import parse, request
import csv
from bs4 import BeautifulSoup
import os
 
NASDAQ = 'nasdaq'
NYSE = 'nyse'
AMEX = 'amex'
 
os.remove("symbols.csv")
file = open('symbols.csv', 'w')
file.truncate()
writer = csv.writer(file)
 
exchanges_dict = {
    NASDAQ  :
            {'pages_max': 5,
               'params': {
                   'f': 2222,
                   'exch': NASDAQ,
                   'showcategories': 'STK',
                   'p': '',
                   'cc': '',
                   'limit': 100,
                }
            },
    NYSE:
        {'pages_max': 87,
            'params': {
                'f': 2222,
                'exch': NYSE,
                'showcategories': 'STK',
                'p': '',
                'cc': '',
                'limit': 100,
            }
        },
    AMEX:
        {'pages_max': 87,
            'params': {
                'f': 2222,
                'exch': AMEX,
                'showcategories': 'STK',
                'p': '',
                'cc': '',
                'limit': 100,
            }
        },
}

base_url = "https://www.interactivebrokers.com/en/index.php"
symbols = set()
index = 0
for exchange, value in exchanges_dict.items():
    pages_max = value['pages_max']
    params = value['params']
    for page in range(1, pages_max):
        params['page'] = page
        query_string = parse.urlencode(params) 
        url = base_url + "?" + query_string
        with request.urlopen( url ) as response:  
            response_text = response.read()
            xml = BeautifulSoup(response_text, features='lxml')
            section = xml.find_all('section', id="exchange-products")
            rows = section[0].find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) > 0:
                    entry = (
                        cells[0].get_text(),
                        params['showcategories'],
                        'SMART',
                        cells[3].get_text()
                    )
                    print(index, exchange, entry)
                    symbols.add(entry)
                index += 1

sorted_symbols = sorted(symbols)
for s in sorted_symbols:
    writer.writerow(s)
file.close()