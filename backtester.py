''' 
install yfinance with >>>>> pip install yfinance --upgrade --no-cache-dir
''' 

from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG

import yfinance

yfdata = yfinance.Ticker("MSFT")

yfdata.info

data = yfdata.history(period="ytd")

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


bt = Backtest(data, SmaCross, cash=10000, commission=.002)

output = bt.run()
bt.plot()
