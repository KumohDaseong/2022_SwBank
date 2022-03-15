from crawler.Review import Review


class Product():
    def __init__(self, product_url, img_url):
        self.url = product_url
        self.img_src = "img/"
        self.review_list = []
        #self.settingProduct()
    
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
        
    def getURL(self):
        return self.url
    
    def add_review(self):
        new_review = Review()
        