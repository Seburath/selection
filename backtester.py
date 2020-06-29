from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA
import pandas as pd
import requests

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

r = requests.get('https://finance.yahoo.com/trending-tickers')
result = pd.read_html(r.text)
data = pd.DataFrame({'Open': (), 'Low': (), 'Close': (), 'High': (), 'Volume': ()})
data['Volume'] = result[0]['Volume']
data['Open'] = result[0]['Last Price'] + result[0]['Change'] 
data['Close'] = result[0]['Last Price']
data['High'] = result[0]['Market Cap']
data = data.fillna(0)
bt = Backtest(data, SmaCross, cash=10000, commission=.002)

output = bt.run()
bt.plot()
