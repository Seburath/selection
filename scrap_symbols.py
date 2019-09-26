import requests
import csv
from bs4 import BeautifulSoup
import os
os.remove("symbols.csv")
file = open('symbols.csv', 'w')
file.truncate()
writer = csv.writer(file)
list = []

URL = 'https://www.interactivebrokers.com/en/index.php?f=2222&exch='
EXTENDS_URL = '&showcategories=STK&p=&cc=&limit=100&page='

def nasdaq():
    page = 35
    end = 15
    get_data_from_url('nasdaq', page, end)
 
def nyse():
    page = 87
    end = 372
    get_data_from_url('nyse', page, end)
 
def amex():
    page = 87
    end = 368
    get_data_from_url('amex', page, end)
 
switcher = {
        0: nasdaq,
        1: nyse,
        2: amex
    }

def optional(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()

def get_data_from_url(exchange, maxPage, end):
    ran_ini = 3
    ran_end = 400
    for page in range(1,maxPage):
        r  = requests.get(URL + exchange + EXTENDS_URL + str(page))
        data = r.text
        soup = BeautifulSoup(data, features='lxml')
        x = soup.contents
        x = str(x)
        x = x.split('<td>')
        if page >= (maxPage-1):
            ran_end = end
        for i in range(ran_ini,ran_end)[0::4]:
            vals = x[i][:-6], 'STK', 'SMART', x[i+1][:3]
            if vals not in list:
                print(i, exchange.upper(), vals)
                list.append(vals)

for exc in range(0,3):
   optional(exc)

for val in list:
    writer.writerow(val)
file.close()