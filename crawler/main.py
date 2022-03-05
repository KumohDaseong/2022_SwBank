from selenium import webdriver
import urllib.request

from Product import Product

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

url_id = input("input url_id : ")

url = "https://www.amazon.com/s?k={0}&crid=9V9C63OT50BV&sprefix={1}%2Caps%2C269&ref=nb_sb_noss_2".format(url_id, url_id)

driver = webdriver.Chrome(options=options)
driver.get(url)

driver.implicitly_wait(1)

product_all = driver.find_elements_by_class_name("a-link-normal")
img_all = driver.find_elements_by_class_name("s-image")
product_list = []
img_url_list = []
url_list = []

for img_url in img_all:
    img_url_list.append(img_url.get_attribute("src"))
    
    

for product_url in product_all:
    product = Product(product_url.get_attribute("href"))
    product_list.append(product)
    
    
    
for i, url in enumerate(img_url_list):
    if url != None:
        urllib.request.urlretrieve(url,  f'img/{i}.jpg')

print(len(product_all))

for product in product_list:
    print(product.getURL())

