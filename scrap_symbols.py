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

from database import Symbol
import requests
from bs4 import BeautifulSoup

exchanges = ['nasdaq', 'nyse', 'amex']
#exchanges = ['lse','tse']

for exchange in exchanges:
    r = requests.get('https://www.interactivebrokers.com/en/index.php?f=2222&exch={}&showcategories=STK&p=&cc=&limit=100&page=1'.format(exchange))
    data = r.text
    soup = BeautifulSoup(data, features='lxml')
    pagination = soup.find_all('ul', class_='pagination')
    last_page = int([ul.find_all('li')[-2].text for ul in pagination ][0])
    for page_num in range(1, last_page+1):
        page_request = requests.get('https://www.interactivebrokers.com/en/index.php?f=2222&exch={}&showcategories=STK&p=&cc=&limit=100&page={}'.format(exchange, page_num))
        data = page_request.text
        soup = BeautifulSoup(data, features='lxml')
        tables = soup.find_all('table')
        table_body = tables[2].find_all('tbody')
        table_tr = table_body[0].find_all('tr')
        for tr in table_tr:
            td = tr.find_all('td')
            Symbol.create(
                        stock_symbol=td[0].text,
                        stock_exchange=exchange.upper(),
                        currency=td[3].text,
                        routing='SMART',
                        unknown_field='STK'
                        )
            print("{} {}, STK, SMART, {}".format(exchange.upper(), td[0].text, td[3].text))
