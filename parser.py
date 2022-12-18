from bs4 import BeautifulSoup
import requests

# headers = { 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
# like Gecko) Chrome/108.0.0.0 Safari/537.36' }

# req = requests.get('https://career.habr.com/salaries', headers=headers)
# src = req.text

# with open("index.html", "w", encoding="utf-8") as file:
#    file.write(src)

with open('index.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
section = soup.find(class_='body')
print(section)
