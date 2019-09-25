# esto es un script que escribí hace un tiempo y funciona.
# pero el código es terrible, con pésimas prácticas, duele leer.
# si consideras que todo deberia ser borrado y quieres escribir algo diferente
# desde 0, no hay problema.
# no hace falta saber pep 8 de memoria, un plugin en el editor ayuda.
# arreglar esto puede tomar un tiempo, pero si lo terminas y te queda tiempo...
# estaria bueno que todo se guarde en mysql, cualquier orm que sepas esta ok.

# QUE HACE ESTE CODIGO:
# el scraper va a al sitio de interactive brokers y guarda en csv todos los
# simbolos de tres exchanges (NASDAQ, NYSE y AMEX).

# interactive brokers es una plataforma de compra y venta de acciones.
# los simbolos son empresas (TSLA para Tesla, APPL para Apple).
# los exchanges son mercados (NYSE para bolsa de New York).

# recuerda las sabias palabras del tío Bob:
'''A comment is a failure to express yourself in code.
   If you fail, then write a comment; but try not to fail.'''
# si haces comentarios, es mejor que estén en ingles

import requests
import csv
from bs4 import BeautifulSoup
import os
os.remove("symbols.csv")
file = open('symbols.csv', 'w')
file.truncate()
writer = csv.writer(file)
list = []
exchanges = ['nasdaq', 'nyse', 'amex']

#nasdaq
for page in range(1,35):
    r  = requests.get('https://www.interactivebrokers.com/en/index.php?f=2222&exch=nasdaq&showcategories=STK&p=&cc=&limit=100&page=' + str(page))
    data = r.text
    soup = BeautifulSoup(data, features='lxml')
    x = soup.contents
    x = str(x)
    x = x.split('<td>')
    if page < 34:
        ran_ini = 3
        ran_end = 400
    else:
        ran_ini = 3
        ran_end = 15
    for i in range(ran_ini,ran_end)[0::4]:
        vals = x[i][:-6], 'STK', 'SMART', x[i+1][:3]
        if vals not in list:
            print(i, 'NASDAQ', vals)
            list.append(vals)

#nyse
for page in range(1,87):
    r  = requests.get('https://www.interactivebrokers.com/en/index.php?f=2222&exch=nyse&showcategories=STK&p=&cc=&limit=100&page=' + str(page))
    data = r.text
    soup = BeautifulSoup(data, features='lxml')
    x = soup.contents
    x = str(x)
    x = x.split('<td>')
    if page < 86:
        ran_ini = 3
        ran_end = 400
    else:
        ran_ini = 3
        ran_end = 372
    for i in range(ran_ini,ran_end)[0::4]:
        vals = (x[i][:-6], 'STK', 'SMART', x[i+1][:3])
        if vals not in list:
            print(i, 'NYSE', vals)
            list.append(vals)

#amex
for page in range(1,87):
    r  = requests.get('https://www.interactivebrokers.com/en/index.php?f=2222&exch=amex&showcategories=STK&p=&cc=&limit=100&page=' + str(page))
    data = r.text
    soup = BeautifulSoup(data, features='lxml')
    x = soup.contents
    x = str(x)
    x = x.split('<td>')
    if page < 86:
        ran_ini = 3
        ran_end = 400
    else:
        ran_ini = 3
        ran_end = 368
    for i in range(ran_ini,ran_end)[0::4]:
        vals = (x[i][:-6], 'STK', 'SMART', x[i+1][:3])
        if vals not in list:
            print(i, 'AMEX', vals)
            list.append(vals)

for val in list:
    writer.writerow(val)
file.close()
