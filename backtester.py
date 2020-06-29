from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, 
import quandl

quandl.ApiConfig.api_key= "1JzcSRocvMqEaHSrEyyB"
data = quandl.get("WIKI/GOOGL")


class SmaCross(Strategy):
    n1 = 10
    n2 = 30

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
        data = bt.feeds.YahooFinanceData(dataname='AAPL',
                                 fromdate=datetime(2016, 1, 1),
                                 todate=datetime(2019, 5, 31))

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


bt = Backtest(data, SmaCross, cash=10000, commission=.002)

output = bt.run()
bt.plot()
