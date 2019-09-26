import peewee
from playhouse.db_url import connect
import datetime

database = peewee.MySQLDatabase('stock_market', host='localhost', port=3306,user='root', password='root')

class Symbol(peewee.Model):
	symbol_id = peewee.BigIntegerField(primary_key=True)
	stock_symbol = peewee.CharField()
	stock_exchange
	created_at = peewee.DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = database
		db_table = 'symbol'