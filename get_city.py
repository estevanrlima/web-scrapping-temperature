import requests
import sys
from bs4 import BeautifulSoup as bs

def get_city_tmin_and_tmax(index, offline = False, debug = False ):
    
    if not offline :
        html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/"+ index).content
        soup = bs(html, 'html.parser')
        tmin = soup.find('span', {'id': 'min-temp-1'}).string # pega a temperatura mínima
        tmax = soup.find('span', {'id': 'max-temp-1'}).string # pega a temperatura máxima
        cidade = soup.findAll('span', {'itemprop': 'name'})[3].string # pega o nome da cidade
    else :
        # html pre-baixado , para o caso do Climatempo estar fora do ar
        html = open('riodejaneiro-rj.html', 'r', encoding='UTF8').read()
        soup = bs(html, 'html.parser')
        tmin = soup.find('span', {'id': 'min-temp-1'}).string # pega a temperatura mínima
        tmax = soup.find('span', {'id': 'max-temp-1'}).string # pega a temperatura máxima
        cidade = soup.findAll('span', {'itemprop': 'name'})[3].string # pega o nome da cidade
        
    if debug :
        print (soup.prettify())
        
    return cidade , tmin , tmax