class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author = author
        self.price=price
        self._discount = 0.1
        
    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, const{self.price}"
        
        
    # TODO __getattribute__called when an attribute is retrieved Dont
    # directly access the attr name otherwise a recursive loop is created
    # def __getattribute__(self,name):
    #     if name== "price":
    #         p=super().__getattribute__("price")
    #         d = super().__getattribute__("_discount")
    #         return p - (p * d)
    #     return super().__getattribute__(name)
    
    # TODO __setattr__ called when an attribute value is set. Don't set   
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name, value)
    
    #TODO __getattr__ called when __getattribute__lookup fails -you
    def __getattr__(self, name):
        return name + " is not here"
    
b1=Book("Thing Fail Aparts","Jonny Opara", float(5000))
b2=Book("Send Your Account Detail","Abu Banaat",float(1000))

# b1.price = float(40)
# raise an error when test with integer number
# b1.price = 1000 

print(b1.randompro)
 