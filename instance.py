# Python object oriented programming by by Joe Marini course example
#  Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialize
    
    def __init__(self, title, author, pages, price):
        self.title = title
        
        # TODO  add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"
        
    # TODO created instance method
    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setDiscount(self, amount):
        self._discount = amount

    def getsecretAttr(self):
        print(self.__secret)
        
b1=Book("My Lover wife","The prince",1000,2000,)
b2=Book("My Lover wife","The prince",1000,2000,)

b1.setDiscount(0.25)
print(b1.setDiscount(0.25))
print(b1.getPrice())
print(b2.getsecretAttr())
print(b2._Book__secret)