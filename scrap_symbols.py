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

import csv
import os
from models.exchange import Exchange

os.remove("symbols.csv")
file = open('symbols.csv', 'w')
file.truncate()
writer = csv.writer(file)
list_result = []
exchanges = ['nasdaq', 'nyse', 'amex']


for exchanger_name in exchanges:
    exchanger = Exchange(exchanger_name)
    data_from_exchanger = exchanger.get_data()
    list_result.extend([data for data in data_from_exchanger if data not in list_result])

for val in list_result:
    writer.writerow(val)
file.close()