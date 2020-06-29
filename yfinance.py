import pandas as pd 
import requests
from bs4 import BeautifulSoup
import csv
import datetime


class Yahoo:
    def __init__(self):
        self.date = []
        self.open_ = []
        self.high = []
        self.low = []
        self.close = []
        self.volume = []

    def scrap(self, company_code):
        url = 'https://finance.yahoo.com/quote/{}/history?p={}'.format(company_code, company_code)
        request_text = requests.get(url).text
        return request_text

    def format_date(self, value):
        temp_date = value.split()
        temp_date[1] = temp_date[1].strip(',')            
        temp_date = " ".join(temp_date)
        formatted_date = datetime.datetime.strptime(temp_date, '%b %d %Y')
        return formatted_date


    def build_panda(self):
        request_text = self.scrap('GOOG')
        soup = BeautifulSoup(request_text, features='html.parser')
        rows = soup.find_all('tr', attrs={'class': 'BdT'})

        for row in rows[:-1]:
            values = row.find_all('td')
          
            self.date.append(self.format_date(values[0].text))
            self.open_.append(float(values[1].text.replace(',', '')))
            self.high.append(float(values[2].text.replace(',', '')))
            self.low.append(float(values[3].text.replace(',', '')))
            self.close.append(float(values[4].text.replace(',', '')))
            self.volume.append(float(values[5].text.replace(',', '')))

        return pd.DataFrame({"Open": self.open_, "High": self.high, "Low": self.low, "Close": self.close, "Volume": self.volume}, index= self.date)


GOOG = Yahoo().build_panda()
# print(GOOG)
