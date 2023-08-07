import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

#twilio account info
client = Client('account_sid','auth_token')
#item links to check
urls = ['']
#name or description of item
names = ['H4350']
#text to look for, must be exact
texts = ['Out of Stock, No Backorder']

i = 0

while True:
    page = requests.get(urls[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    if(soup.find(text=texts[i])):
        print('out of stock')
    else:
        print(str(names[i]) + ' is now in stock' + str(urls[i]))
        #to = your-number, from_ = number-from-twilio
        client.messages.create(to = '+###########', from_ = '+###########', body = str(names[i]) + ' is now in stock' + str(urls[i]))
        break
    i += 1
    if(i>=len(urls)):
        i = 0
        time.sleep(60)
