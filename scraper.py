import requests
from bs4 import BeautifulSoup
import time

#Function that scrap s&p 500 price
def sp500Price():
    URL = "https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC"

    #Parsing the page
    respone = requests.get(URL)
    soup = BeautifulSoup(respone.text, 'html.parser')

    #Getting and printing the price
    sp500_price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(f"s&p 500 stock market price: {sp500_price}")




while True:
    #Calling the functions
    sp500Price()

    #Repeat function calling every 60 seconds 
    time.sleep(60)
