from crawler.Review import Review


class Product():
    def __init__(self, product_url, img_url):
        self.url = product_url
        self.img_src = ""
        self.review_list = []
        self.name = ""
        self.key = 0

    
    def setURL(self, url):
        self.url = url
        
    def setKey(self, key):
        self.key = key
        
    def setImgSrc(self, img_src):
        self.img_src = img_src
        
    def getURL(self):
        return self.url
    
    def getKey(self):
        return self.key
    
    def getImgSrc(self):
        return self.img_src
    
    def add_review(self, new_review : Review):
        self.review_list.append(new_review)