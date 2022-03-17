'''
클래스 명 : ProductCrawler

설명 : 크롤링이 이뤄지는 클래스입니다.

작성일 : 2022.03.17

마지막 수정한 사람 : 전민규

마지막 수정한 날짜 : 2022.03.17

Todo >

Fixme >

'''

from selenium import webdriver
import urllib.request
from Product import Product

class ProductCrawler():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        
        self.product_list = [] #크롤링한 Product들이 저장됩니다.
        self.search_word = self.setSearchWord() #검색어를 입력합니다.
        
    
    #search_word를 입력하는 함수입니다. 확장성을 위해 분리했습니다.
    def setSearchWord(self):
        word = input("검색어를 입력하세요 : ")
        return word