from bs4 import BeautifulSoup
import requests 

KEYWORDS = {'2004', 'фото', 'web', 'python'}

site = requests.get('https://habr.com/ru/all/')
if not site.ok:
  raise RuntimeError('Нет доступа к сайту')
text = site.text
soup = BeautifulSoup(text, features="html.parser")

# tm-article-snippet__title
#<time datetime="2021-08-20T09:56:00.000Z" #title="2021-08-20, 11:56">сегодня в 11:56</time>

articles = soup.find_all('article')
for article in articles:
    title = article.find('a', class_='tm-article-snippet__title-link').text
    time = article.find('time').text 
    link = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
    preview = article.find('div', class_='article-formatted-body').text
    new_preview = set(preview.split(' '))
    if new_preview & KEYWORDS:
      print(f'{title} — {time} — {link}')
