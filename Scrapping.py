from bs4 import BeautifulSoup
import requests 

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

site = requests.get('https://habr.com/ru/all/')
if not site.ok:
  raise RuntimeError('Нет доступа к сайту')
text = site.text
soup = BeautifulSoup(text, features="html.parser")


articles = soup.find_all('article')
for article in articles:
    title = [h.text.strip for h in article.find_all('a', class_='hub-links')]

#   time = {h.text.strip() for h in article.find_all('time', class_ = 'title')}
#   link = {h.text.strip() for h in article.find_all('a', class_ = 'hub-link')}
#   content =  {h.text.strip() for h in article.find_all('article', class_= 'post post preview')}
print(title)
