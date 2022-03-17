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
        self.driver = webdriver.Chrome(options=options)
        
        self.product_list = [] #크롤링한 Product들이 저장됩니다.
        
        self.max_page = 5 # 아마존 검색 결과의 max_page까지의 product들을 크롤링합니다.
        
        self.search_word = self.setSearchWord() #검색어를 입력합니다.
        
    
    #search_word를 입력하는 함수입니다. 확장성을 위해 분리했습니다.
    def setSearchWord(self):
        word = input("검색어를 입력하세요 : ")
        return word
    
    #url에 접속해 페이지의 product들을 크롤링하는 함수입니다.
    def onePageCrawl(self, url):
        self.driver.get(url)
        all_products_in_page = self.driver.find_elements_by_class_name("s-card-container.s-overflow-hidden.aok-relative.s-expand-height.s-include-content-margin.s-latency-cf-section.s-card-border")
        