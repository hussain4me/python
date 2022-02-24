class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author = author
        self.price=price
        
    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, const{self.price}"
        
        
    # TODO use the __call__ method to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
b1=Book("Thing Fail Aparts","Jonny Opara", 5000)
b2=Book("Send Your Account Detail","Abu Banaat",1000)

print(b1)

b1("Zubai Hussain","Abu Baanat",5050)
print(b1)

 