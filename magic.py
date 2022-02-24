class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author = author
        self.price=price
        
    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, const{self.price}"
        
        
    # TODO use the __repr__ method to return an obj representation
    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"
    
b1=Book("Thing Fail Aparts","Jonny Opara", 5000)
b2=Book("Send Your Account Detail","Abu Banaat",1000)

print(b1)
print(b2)

print(str(b1))
print(repr(b2))
 