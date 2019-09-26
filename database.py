import peewee
from playhouse.db_url import connect
import datetime

database = peewee.MySQLDatabase('stock_market', host='localhost', port=3306,user='root', password='root')

class Symbol(peewee.Model):
	symbol_id = peewee.AutoField()
	stock_symbol = peewee.CharField()
	stock_exchange = peewee.CharField()
	unknown_field = peewee.CharField()
	currency = peewee.CharField()
	routing = peewee.CharField()
	created_at = peewee.DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = database
		db_table = 'symbol'

if __name__ == '__main__':
	Symbol.create_table()