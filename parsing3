import requests
from bs4 import BeautifulSoup 
import csv

base_url = "https://www.kivano.kg/mobilnye-telefony"
page = 1

with open('products.csv', 'w') as file:
    writer = csv.writer(file)

    
    while page<25:
        print("______________________________________PAGE___________________________",page)
        url = base_url + "?page="+str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        
            
        product_list = soup.find_all("div",{"class": "product_listbox"})
        

        
        for product in product_list:
            name = product.find("div",{"class":"listbox_title"}).text.strip()
            price = product.find("div",{"class": "listbox_price"}).find("strong").text.strip()
            image_link = product.find("div",{"class": "listbox_img"}).find("img")["src"]
            print(name,price,image_link)
            writer.writerow([name,price,image_link])
                
        page = page + 1