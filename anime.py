from typing import List
from bs4 import BeautifulSoup
import requests 

def find_top_anime() -> List[dict]:
    data = requests.get('https://myanimelist.net/topanime.php')
    soup = BeautifulSoup(data.text, 'html.parser')

    anime_div_list = soup.find_all('div', { 'class': 'di-ib clearfix'})
    anime_list = []
    count = 0
    for anime_div in anime_div_list:
        # get the anime name 
        anime_h3 = anime_div.find_all_next('h3', { 'class': 'hoverinfo_trigger'})
        anime_name =  anime_h3[0].find_next('a').text
    
        # get the information
        anime_info = anime_div.find_next('div', { 'class': 'information'})
        info_list = anime_info.text.strip().splitlines()
        new_values = [info.strip() for info in info_list]

        anime_ratings = anime_div.find_next('span', { 'class': 'score-label' }).text

        anime = {
            "name" : anime_name,  
            "episodes" : new_values[0],
            "aired_date" : new_values[1],
            "rating" : anime_ratings
        }
        anime_list.append(anime)
    return anime_list