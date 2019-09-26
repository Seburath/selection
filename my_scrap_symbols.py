# -*- coding: utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup
import os

def do_scrapping(exchange,page_ini,page_end,ran_end_param):
    list = []
    for page in range(page_ini,page_end):
        url = "https://www.interactivebrokers.com/en/index.php?f=2222&exch=%s&showcategories=STK&p=&cc=&limit=100&page=%d" % (exchange,page)
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, features='lxml')
        x = soup.contents
        x = str(x)
        x = x.split('<td>')
        if page < (page_end - 1):
            ran_ini = 3
            ran_end = 400
        else:
            ran_ini = 3
            ran_end = ran_end_param
        for i in range(ran_ini,ran_end)[0::4]:
            vals = x[i][:-6], 'STK', 'SMART', x[i+1][:3]
            if vals not in list:
                #print(i, exchange.upper() , vals)
                list.append(vals)
    return list
 

def write_csv(list):
    os.remove("symbols.csv")
    file = open('symbols.csv', 'w')
    file.truncate()
    writer = csv.writer(file)
    for val in list:
        writer.writerow(val)
    file.close()

def main():
    list = []
    exchanges = ['nasdaq', 'nyse', 'amex']
    params_scrapping = {'nasdaq': (1,35,15),'nyse' : (1,87,372),'amex': (1,87,368)}
    for exch in exchanges:
        params = params_scrapping[exch]
        list_result = do_scrapping(exch,params[0],params[1],params[2])
        list.extend(list_result)
    write_csv(list)
    print("Records scrapped = %d" % len(list))

if __name__ == "__main__":
    main()
