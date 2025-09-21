
#Web scrapping
from bs4 import BeautifulSoup
import requests
import pandas as pd
response = requests.get("https://sportscorner.qa/en/mens/footwear.html?brand=5662")
print(response)
soup=BeautifulSoup(response.content,'html.parser')
print(soup)
names=soup.find_all('strong',class_="product name product-item-name")
#print(names)
name = []
for i in names[0:12]:
    d = i.get_text(strip=True)
    name.append(d)
print(name)
brands=soup.find_all('div',class_="ox-product-grid__brands ha_te")
#print(names)
brand = []
for i in brands:
    d = i.get_text(strip=True)
    brand.append(d)
print(brand)
prices=soup.find_all('span', class_="price-wrapper")
#print(prices)
price=[]
for i in prices[0:12]:
    d = i.get_text(strip=True)
    price.append(d)
print(price)
images = soup.find_all('img',class_="product-image-photo")
#print(images)
image = []
for i in images[0:12]:
    d = i['src']
    image.append(d)
print(image)
df = pd.DataFrame()
#print(df)
df['names'] = name
df['brands'] = brand
df['prices']=price
df['images']=image
print(df)
df.to_csv('PremiumShoes.csv')