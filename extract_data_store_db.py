import requests
import csv
from bs4 import BeautifulSoup
import os
import pandas as pd 
import psycopg2
      
class DATABASE():
    def __init__(self):
        self.user="postgres"
        self.password = "admin"
        self.host = "localhost"
        self.port = "5432"
        self.database = "aplicacionPy"
        
    def conectar(self):
        try:
            connection = psycopg2.connect(user = self.user,
                                          password = self.password,
                                          host = self.host,
                                          port = self.port,
                                          database = self.database)

            cursor = connection.cursor()
            print ( connection.get_dsn_parameters(),"\n")

            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record,"\n")
            return connection
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
            return error
    def desconectar(self):
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
    def crear_tabla(self):
        try:
            connection = self.conectar()

            cursor = connection.cursor()

            create_table_query = '''CREATE TABLE public."RESULTS_CURRENCY"
                (
                    "IBSymbol" character varying NOT NULL,
                    "STK" character varying NOT NULL,
                    "SMART" character varying NOT NULL,
                    "Currency" character varying NOT NULL
                )
                WITH (
                    OIDS = FALSE
                );
                ALTER TABLE public."RESULTS"
                    OWNER to postgres;'''
            cursor.execute(create_table_query)
            connection.commit()
            print("Table created successfully in PostgreSQL ")
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating PostgreSQL table", error)
            
    def insert(self,value1,value2,value3,value4):
        try:
            connection=self.conectar()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO public.\"RESULTS_CURRENCY\" (\"IBSymbol\", \"STK\", \"SMART\",\"Currency\") VALUES(%s, %s, %s, %s)", (value1, value2, value3,value4))
            connection.commit()
            cursor.close()
            connection.close()
            print ("Record inserted successfully into mobile table")
        except (Exception, psycopg2.Error) as error :
            if(connection):
                print("Failed to insert record into mobile table", error)
                
file = open('symbols.csv', 'w')
file.truncate()
writer = csv.writer(file)
values_exchange = []

class Exchange:
    def __init__(self,url,page_max,ran_endC,name_exchange):
        self.url=url
        self.page_max=page_max
        self.ran_endC=ran_endC
        self.name_exchange=name_exchange
        
    def extract_data(self):
        database=DATABASE()
        for page in range(1, self.page_max):
            response  = requests.get(self.url + str(page))
            data = response.text
            soup = BeautifulSoup(data, features='lxml')
            html = str(soup.contents)
            html_preprocess = html.split('<td>')
            if page < self.page_max-1:
                ran_ini = 3
                ran_end = 400
            else:
                ran_ini = 3
                ran_end = self.ran_endC
            for i in range(ran_ini,ran_end)[0::4]:
                values = (html_preprocess[i][:-6], 'STK', 'SMART', html_preprocess[i+1][:3])
                database.insert(html_preprocess[i][:-6], 'STK', 'SMART', html_preprocess[i+1][:3])
                if values not in values_exchange:
                    print(i, self.name_exchange, values)
                    values_exchange.append(values)

urls=['https://www.interactivebrokers.com/en/index.php?f=2222&exch=nasdaq&showcategories=STK&p=&cc=&limit=100&page=','https://www.interactivebrokers.com/en/index.php?f=2222&exch=nyse&showcategories=STK&p=&cc=&limit=100&page=','https://www.interactivebrokers.com/en/index.php?f=2222&exch=amex&showcategories=STK&p=&cc=&limit=100&page=']

db=DATABASE()
db.crear_tabla()
exchange_nasdaq=Exchange(urls[0],35,15,'NASDAQ')                    
exchange_nasdaq.extract_data()

exchange_nyse=Exchange(urls[1],87,372,'NYSE')                    
exchange_nyse.extract_data()

exchange_amex=Exchange(urls[2],87,368,'AMEX')                    
exchange_amex.extract_data()