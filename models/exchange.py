from bs4 import BeautifulSoup
import requests
import json

class Exchange:
    def __init__(self, name):
        self.name = name        
        config = self.get_configs()

        self.main_url = config['main_url']
        self.ran = (int(config['ran_ini']),int(config['ran_end'])) 
        self.ran_last = (int(config['ran_ini_last_page']),int(config['ran_end_last_page'])) 
        self.limit_page = config['limit_page']
        self.categories = config['categories']
        self.last_page = config['last_page']               
    
    def get_data(self):
        data_list = []
        for page in range(1, self.last_page + 1):
            full_url = self.get_full_url(page)
            data = self.get_data_from_url(full_url)

            ran_ini, ran_end = self.ran if page < self.last_page else self.ran_last           

            for i in range(ran_ini,ran_end)[0::4]:
                vals = (data[i][:-6], 'STK', 'SMART', data[i+1][:3])
                if vals not in data_list:
                    print(i, self.name.upper(), vals)
                    data_list.append(vals)
                    
        return data_list                                        
                
       

    def get_data_from_url(self, full_url):
        r  = requests.get(full_url)
        data = r.text
        soup = BeautifulSoup(data, features='lxml')
        x = str(soup.contents).split('<td>')
        return x

    def get_full_url(self, page):
        url = f"{self.main_url}?f=2222&exch={self.name}&showcategories={self.categories}&limit={self.limit_page}&page={page}"  
        return url

    def get_configs(self):        
        with open("exchanges_config.json", "r") as read_file:
            data = json.load(read_file)
            return data[self.name]
            
