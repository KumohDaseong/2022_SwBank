from numpy import product
from selenium import webdriver
import time
import urllib.request
from Product import Product

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

url_id = input("input url_id : ")

url = "https://www.amazon.com/s?k={0}&crid=9V9C63OT50BV&sprefix={1}%2Caps%2C269&ref=nb_sb_noss_2".format(url_id, url_id)

driver = webdriver.Chrome(options=options)
driver.get(url)

driver.implicitly_wait(1)

all_products = driver.find_elements_by_class_name("a-section.a-spacing-base")
product_list = []
for selected_product in all_products:
    product_url = selected_product.find_element_by_class_name("a-link-normal")
    print(product_url.get_attribute("href"))
    
    '''img_element_url = selected_product.find_element_by_class_name("s-image").get_attribute("src")
    new_product = Product(selected_product.get_attribute("href"))
    product_list.append(new_product)
    
    print(img_element_url)
    print(new_product)'''
