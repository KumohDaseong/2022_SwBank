from crawler.Review import Review


class Product():
    def __init__(self, product_url, img_url):
        self.url = product_url
        self.img_src = ""
        self.review_list = []
        self.name = ""
        self.key = ""
    
    def setInfo(self):
        self.name
        self.price
        self.review_rating
        self.standard
        self.Weight
        self.item_model_number
        self.date_first_available
        self.manufacturer
        self.asin
        self.review = []
    
    def setURL(self, url):
        self.url = url
        
    def setImgSrc(self, img_src):
        self.img_src = img_src
        
    def getURL(self):
        return self.url
    
    def getImgSrc(self):
        return self.img_src
    
    def add_review(self):
        new_review = Review()