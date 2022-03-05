from selenium import webdriver

url_id = input("input url_id : ")
url = "https://www.amazon.com/s?k={0}&crid=9V9C63OT50BV&sprefix={1}%2Caps%2C269&ref=nb_sb_noss_2".format(url_id, url_id)

driver = webdriver.Chrome("./chromedriver")
driver.get(url)

list = []


