from bs4 import BeautifulSoup
import requests
import csv

req = requests.get("https://unicode.org/Public/emoji/15.0/emoji-test.txt")

soup = BeautifulSoup(req.content, "html.parser")
with open("datasets\emoji_data\emoji_text_scrapped.txt", "w", encoding="utf-8") as file: 
    file.write(str(soup.prettify()))

print(soup.prettify())