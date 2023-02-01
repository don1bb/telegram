import requests
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://www.mashina.kg'
URL = 'https://www.mashina.kg/search/all/'

response = requests.get(URL)
if response.status_code == 200:
        html = response.text
        soup = BS(response.text, 'html.parser')
        table = soup.find('div', class_='table-view-list')  # таблица с объявлениями
        ads = table.find_all('div', class_='list-item')  # все карточки объявлений
        cars = []
        for c in ads:
            BASE_URL + c.find('a').get('href')
            car = {
                'title': c.find('div', class_='title')\
                    .find('h2').string.replace('\n', '').strip(),
                'price': c.find('div', class_='price')\
                    .find('strong').string.replace('\n', '').strip()
            }
            cars.append(car)

        print(cars)