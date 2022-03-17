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
        self.product_key = 1 #프로그램 상에서 임시적으로 사용하는 product의 key값입니다. 추후 아마존네서 실제로 사용하는 SIC로 변경할 예정입니다.
        
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
        all_products_in_page = self.driver.find_elements_by_class_name("s-card-container.s-overflow-hidden.aok-relative.s-expand-height.s-include-content-margin.s-latency-cf-section.s-card-border") #페이지에서 추출한 모든 product의 배열입니다.
        
        for each_product in all_products_in_page:
            new_product = Product()
            
            #product의 url을 추출해 냅니다
            product_url = each_product.find_element_by_class_name("a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
            product_detail_url = product_url.get_attribute("href")
            new_product.setURL(product_detail_url)
            
            
            #product의 image를 추출해냅니다.
            img_element = each_product.find_element_by_class_name("s-image")
            img_url = img_element.get_attribute("src")
            urllib.request.urlretrieve(img_url,  f'img/{i}.jpg')
        
        
        
        
        