from bs4 import BeautifulSoup as bs
import requests


def scraper():
	# requests HTML code for yahoo finance URL

	r = requests.get("https://api.scrapingdog.com/scrape?api_key=5ea541dcacf6581b0b4b4042&url=https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch").text

	soup = bs(r,'html.parser') #parses html 

	table_body = soup.find_all('tbody') #finds all site content with the tbody tag

	for tr in table_body:
		table_row = tr.find_all('tr', attrs={'data-reactid': '122'})
		for td in table_row:
			table_data = td.find_all('td')
			for i in table_data:
				if i != None:
					try:
						result = {table_data[0].text: table_data[1].text}
					except:
						result = {table_data[0].text: ""} 
		print(result) #returns a dict of the market volume and its value

scraper()

