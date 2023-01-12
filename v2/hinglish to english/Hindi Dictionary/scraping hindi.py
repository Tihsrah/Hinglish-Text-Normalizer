import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
from tqdm import tqdm
import time
page_range = 247
page_words = 50
word_list = []
for i in tqdm(range(1, page_range)):
    # time.sleep(1)
    html_text = requests.get(
        f'https://dict.hinkhoj.com/hindi-words/listu.php?page={i}')
    html = html_text.text
    soup = BeautifulSoup(html, 'lxml')
    column = soup.find_all('div', class_="browse-word")
    for j in range(page_words):
        try:
            test = column[j].text
            test = test.strip()
            word_list.append(test)
        except:
            print("exception at word", j, "page", i)
word_list = pd.DataFrame(word_list)
word_list.to_csv("उ.csv", index=False)
