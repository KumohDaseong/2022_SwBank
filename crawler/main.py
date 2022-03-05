from selenium import webdriver
import time

from crawler.Product import Product

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

url_id = input("input url_id : ")

url = "https://www.amazon.com/s?k={0}&crid=9V9C63OT50BV&sprefix={1}%2Caps%2C269&ref=nb_sb_noss_2".format(url_id, url_id)

driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(3)

product_all = driver.find_elements_by_class_name("a-link-normal")
product_list = []
url_list = []

for product_url in product_all:
    product = Product(product_url.get_attribute("href"))
    product_list.append(product)

print(len(product_all))

for i in url_list:
    print(i)

