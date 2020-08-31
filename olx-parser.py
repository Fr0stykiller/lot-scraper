from bs4 import BeautifulSoup
from requests import get
import unicodedata

def znajdzCene(url):
    #Funkcja scrapuje html strony szukajac klase okreslającą cene dziełki.
    response = get(url)
    response_text = response.text
    html_soup = BeautifulSoup(response_text, 'html.parser')
    prices = html_soup.find('span', {'class' : 'amount'}).text
    prices = unicodedata.normalize('NFKC', prices)
    prices = prices.replace("zł", "")
    prices = prices.replace(" ", "")
    prices = int(prices)
    print(prices)
  
    pass

def znajdzMiejscowosc(url):
    #Funkcja szuka nazwy miejscowosci dzialki.
    response = get(url)
    response_text = response.text
    html_soup = BeautifulSoup(response_text, 'html.parser')
    prices = html_soup.find_all('div', {'class' : 'location'})
    print(prices)



    pass

znajdzCene("https://www.gumtree.pl/a-dzialki/skawina/ladna-dzialka-bud-10-5ar-w-skawinie+korabiniki/1007921241220911381140409")
znajdzMiejscowosc("https://www.gumtree.pl/a-dzialki/skawina/ladna-dzialka-bud-10-5ar-w-skawinie+korabiniki/1007921241220911381140409")