import requests
from bs4 import BeautifulSoup
import time
import datetime

#Curent time
now = datetime.datetime.now()

#Function that scrap s&p 500 price
def sp500Price():
    URL = "https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC"

    #Parsing the page
    respone = requests.get(URL)
    soup = BeautifulSoup(respone.text, 'html.parser')

    #Getting and printing the price
    sp500_price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(f"s&p 500 stock market price: {sp500_price}")

def TeslaPrice():
    URL = "https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch"
    respone = requests.get(URL)
    soup = BeautifulSoup(respone.text, 'html.parser')
    tesla_price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(f"Tesla stock market price: {tesla_price}")

def ApplePrice():
    URL = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
    respone = requests.get(URL)
    soup = BeautifulSoup(respone.text, 'html.parser')
    apple_price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(f"Apple stock market price: {apple_price}")


while True:
    print (now.now().strftime("%H:%M:%S"))

    #Calling the functions
    sp500Price()
    TeslaPrice()
    ApplePrice()

    #Repeat function calling every 60 seconds
    time.sleep(300)
