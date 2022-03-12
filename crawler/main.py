'''
클래스 명 : main

설명 : 크롤링이 이뤄지는 클래스입니다.

작성일 : 2022.03.05

마지막 수정한 사람 : 전민규

마지막 수정한 날자 : 2022.03.13

Todo > 현재 Product의 url을 추출할 수 있는 상황입니다. 후 url로 접속해 세부정보를 추출해야합니다

Fixme > 코드구조가 지저분합니다, 정리가 필요합니자

'''


from numpy import product
from selenium import webdriver
import urllib.request
from Product import Product

#chrome driver 동기화
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

#url_id는 검색어를 뜻합니다
url_id = input("input url_id : ")

#max_page는 검색된 제품을 크롤링할 페이지 수를 뜻합니다.
max_page = 5

#i는 추출된 제품의 갯수이자, 임시적으로 추출한 제품의 image파일의 이름이기도 합니다.
i = 1

#max_page만큼의 반복을 수행합니다
for index in range(max_page):
    current_url = "https://www.amazon.com/s?k={0}&page={1}&crid=30C3YW3X77W5M&qid=1646884892&sprefix=cu%2Caps%2C296&ref=sr_pg_{1}".format(url_id, index+1)
    driver.get(current_url)
    driver.implicitly_wait(1)
    
    #페이지 내에 존재하는 제품들을 추출한 배열입니다.
    all_products_in_page = driver.find_elements_by_class_name("s-card-container.s-overflow-hidden.aok-relative.s-expand-height.s-include-content-margin.s-latency-cf-section.s-card-border")
    
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print(len(all_products_in_page))#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다

    #각 product들을 등록합니다
    for selected_product in all_products_in_page:
        #product의 url을 추출해 냅니다
        product_url = selected_product.find_element_by_class_name("a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
        product_detail_url = product_url.get_attribute("href")
        print(product_detail_url, "     ", i) #테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
        
        #product의 image를 추출해냅니다.
        img_element = selected_product.find_element_by_class_name("s-image")
        img_url = img_element.get_attribute("src")
        urllib.request.urlretrieve(img_url,  f'img/{i}.jpg')
        
        i += 1

    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print()#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다
    print(len(all_products_in_page))#테스트를 위한 임시 코드입니다. 추후에 삭제가 필요합니다