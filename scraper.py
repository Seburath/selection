import requests
import peewee
from bs4 import BeautifulSoup


collector = peewee.MySQLDatabase('collector',
                          host='localhost',
                          port=3306,
                          user='root',
                          password='deidei')


class Scraped(peewee.Model):
    exchange = peewee.CharField()
    symbol = peewee.CharField()
    symbol_type = peewee.CharField()
    market = peewee.CharField()
    currency = peewee.CharField()

    class Meta:
        database = collector
        db_table = 'scraped_symbols'


def scrap_pages():
    for exchange in exchanges:
        try:
            for page in range(1, 100):  # nasdaq goes till 34, nyse 86 and amex 86
                request_page  = requests.get('https://www.interactivebrokers.com/en/index.php?f=2222&exch=' + exchange + '&showcategories=STK&p=&cc=&limit=100&page=' + str(page))
                request_text = request_page.text
                soup = BeautifulSoup(request_text, features='lxml')
                content = soup.contents
                content_str = str(content)
                content_lst = content_str.split('<td>')
                parse_content(exchange, page, content_lst)
        except Exception as err:
            print(err)
        except IndexError:
            print('FINALIZED: ' + exchange)


def parse_content(exchange, page, content_lst):
    range_ini = 3
    range_end = 400
    for line in range(range_ini, range_end)[0::4]:
        vals = exchange, content_lst[line][:-6], 'STK', 'SMART', content_lst[line + 1][:3]
        symbols.append(vals)
        print(vals)


def fuse_duplicates():
    for symbol1 in symbols:
        replist = []
        exchanges = ''
        for symbol2 in symbols:
            if symbol1[1] == symbol2[1]:
                exchanges += str(symbol2[0]) + ';'
                replist.append(symbol2)
        if len(replist) > 1:
            for rep in replist:
                symbols.remove(rep)
            vals = (exchanges[:-1],
                    symbol1[1],
                    symbol1[2],
                    symbol1[3],
                    symbol1[4])
            symbols.append(vals)


def save_symbols():
    Scraped.truncate_table()
    for symbol in symbols:
        new_record = Scraped.create(exchange=symbol[0],
                                    symbol=symbol[1],
                                    symbol_type=symbol[2],
                                    market=symbol[3],
                                    currency=symbol[4],
                                    )
        new_record.save()


if __name__ == '__main__':
    if not Scraped.table_exists():
        Scraped.create_table()

    exchanges = ['nasdaq', 'nyse', 'amex']
    symbols = []

    scrap_pages()
    fuse_duplicates()
    save_symbols()

    print("""
There should be more than 10.000 symbols scraped,
if there's less it could be caused by a conection problem,
re-runing the script should solve it.""")
    print(len(symbols), 'scraped')
