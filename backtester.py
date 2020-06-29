from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from sqlalchemy import create_engine
from backtesting.test import SMA, GOOG


engine = create_engine("mysql://user:pwd@localhost/stock", echo = True)

stocks = Table(
   'stocks', meta, 
   Column('symbol', String), 
   Column('price', String), 
)


st = stocks.select()
conn = engine.connect()
result = conn.execute(st)



for row in result:
   print (row)
class SmaCross(Strategy):
    n1 = 10
    n2 = 30

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


bt = Backtest(GOOG, SmaCross, cash=10000, commission=.002)

output = bt.run()
bt.plot()
