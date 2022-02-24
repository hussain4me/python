

class Publication:
    def __init__(self,title, price):
        self.title= title
        self.author = price
        
    
class Periodical(Publication):
    def __init__(self, title,price,period,publisher):
        super().__init__(title,price)
        self.period= period
        self.publisher=publisher
        
        

class Book(Publication):
    def __init__(self, title, author,pages, price):
        super().__init__(title,price)
        self.pages = pages
        self.author = author
        

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title,price,period, publisher)
        

class Newspaper(Periodical):
    def __init__(self, title, publisher,price, period):
        super().__init__(title,price,period, publisher)
        
        
m=Magazine("Things Fail Apart","Global Concept",20000,2022)       
n=Newspaper("Vanguards Newspaper","Vanguard Prints",500,2022)       
        
print(n.title)
print(m.title)   