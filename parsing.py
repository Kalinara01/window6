import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([data['title'], data['image']])


def get_html(url):
    response = requests.get(url)
    # print(response)
    return response.text
# print(get_html('https://cars.kg/offers'))


def get_total_page(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_= 'pages fl').find_all('a')
    last_page = pages[-2].text
    return last_page

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find('div', class_ = 'catalog-list').find_all('a', class_ = 'catalog-list-item')
    # print(cars)

    for car in cars:
        try:
            title = car.find('span', class_= 'catalog-item-caption').text.strip()
            print(title)
        except:
            title = ''
        # print(title)

        try:
            image = car.find('img', class_ = 'catalog-item-cover-img').get('src')
        except:
            image = ''
            # print(image)
        data = {'title': title, 'image': image}
        write_to_csv(data)

# get_data(get_html('https://cars.kg/offers'))
with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['     title     ', '     image     '])

def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)
    number = int(get_total_page(html))
    # get_data(html)
    i = 1
    while i <= number:
        print(i)
        url = f'https://cars.kg/offers/{i}'
        html = get_html(url)
        number = int(get_total_page(html))
        i+=1
        if not BeautifulSoup(html, 'lxml').find('div', class_ = 'catalog-list'):
            break

        get_data(html)


main()
     













import requests
from bs4 import BeautifulSoup
import csv