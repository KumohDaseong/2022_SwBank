from datetime import date
from itertools import starmap


class Review():
    def __init__(self):
        self.writer = ""
        self.content = ""
        self.star = "" #HTML 요소는 문자열로 되어있다. 추후 숫자로 변환이 필요하다고 생각한다.
        self.date = ""
        self.recommend_number = 0
        
    def setWriter(self, writer):
        self.writer = writer
    
    def setContent(self, content):
        self.content = content
    
    def setStar(self, star):
        self.star = star
    
    def setDate(self, date):
        self.date = date
        
    def setRecommendNumber(self, recommend_number):
        self.recommend_number = recommend_number
    
    def getWriter(self):
        return self.writer
    
    def getContent(self):
        return self.content
    
    def getStar(self):
        return self.star
    
    def getStar(self):
        return self.star
    
    def gatDate(self):
        return self.date
    
    def getRecommendNumber(self):
        return self.recommend_number
    
    