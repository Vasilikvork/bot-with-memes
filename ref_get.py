from bs4 import BeautifulSoup

import requests
import random
from keys import url_meme, token, url_anekdot, url_karikature, url_phrase

def meme_get():
    page = requests.get(url_meme)
    soup = BeautifulSoup(page.text, "html.parser")

    allmeme_path = list(soup.find_all('img'))
    list_all_url = [image["src"] for image in allmeme_path]
    list_meme_url = [list_all_url[url] for url in range(len(list_all_url)) if 'www.anekdot.ru' in list_all_url[url]]

    ref = random.choice(list_meme_url)
    # ref = random.choice(list_all_url)
    return ref

def anekdot_get():
    page = requests.get(url_anekdot)
    soup = BeautifulSoup(page.text, "html.parser")

    list_all_anekdot_text = [i.text for i in soup.find_all('div', class_="text")]
    anekdot = random.choice(list_all_anekdot_text)
    return anekdot

def karikature_get():
    page = requests.get(url_karikature)
    soup = BeautifulSoup(page.text, "html.parser")

    all_karicature = soup.find_all("img")
    list_all_karikature_img = [image["src"] for image in all_karicature]
    list_all_karikature_img_clear = [list_all_karikature_img[url] for url in range(len(list_all_karikature_img))if 'www.anekdot.ru' in list_all_karikature_img[url]]
    
    karikature_img = random.choice(list_all_karikature_img_clear)
    return karikature_img

def phrase_get():
    page = requests.get(url_phrase)
    soup = BeautifulSoup(page.text, "html.parser")

    list_all_phrase = [text.text for text in soup.find_all('div', class_= "text")]
    phrase_text = random.choice(list_all_phrase)

    return phrase_text

print(meme_get())