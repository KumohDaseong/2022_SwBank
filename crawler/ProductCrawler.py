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
from crawler.Review import Review

class ProductCrawler():
    def __init__(self):
        self.new_product_key = 1 #프로그램 상에서 임시적으로 사용하는 product의 key값입니다. 추후 아마존네서 실제로 사용하는 SIC로 변경할 예정입니다. 해당 변수는 Product.key와 연동됩니다.
        
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
            
            new_product.setKey(self.new_product_key)
            
            #product의 url을 추출해 냅니다. 후에 함수로 변환시킬 수 있을듯합니다.
            product_url = each_product.find_element_by_class_name("a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
            product_detail_url = product_url.get_attribute("href")
            new_product.setURL(product_detail_url)
            
            #product의 image를 추출해냅니다. 후에 함수로 변환시킬 수 있을듯합니다.
            img_element = each_product.find_element_by_class_name("s-image")
            img_url = img_element.get_attribute("src")
            urllib.request.urlretrieve(img_url,  f'img/{self.new_product_key}.jpg')
            
            #product의 review를 추출해냅니다. 후에 함수로 변환시킬 수 있을듯합니다. 현재는 첫페이지의 리뷰만을 긁어 올 수 있습니다.
            self.driver.get(product_detail_url)
            all_review_url = self.driver.find_elements_by_class_name("a-link-emphasis.a-text-bold")[0]
            self.driver.get(all_review_url)
            all_reveiw = self.driver.find_elements_by_class_name("a-section.celwidget")
            
            for each_review in all_reveiw:
                new_review = Review()
                writer = each_review.find_element_by_class_name("a-profile-name")
                content = each_review.find_element_by_class_name("a-size-base.review-text.review-text-content")
                star = each_review.find_element_by_class_name("a-icon-alt") #숫자가 아닌, 불필요한 단어가 섞인 문자열입니다. 추후 숫자로 바꾸어야합니다.
                recommend_number = each_review.find_element_by_class_name("a-size-base.a-color-tertiary.cr-vote-text") #숫자가 아닌, 불필요한 단어가 섞인 문자열입니다. 추후 숫자로 바꾸어야합니다.
                
                new_review.setContent(content)
                new_review.setRecommendNumber(recommend_number)
                new_review.setWriter(writer)
                new_review.setStar(star)
                
        
            self.new_product_key += 1
        
        
        