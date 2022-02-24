
from dataclasses import dataclass

@dataclass
class Book:
    title:str
    author:str
    pages:int
    price:float
    
    # TODO: use the __str__ method to return a string
    def __post_init__(self):
        
                self.description = f"{self.title} by {self.author}, {self.pages} pages"
   
        
    # TODO use the __call__ method to call the object like a function
    
    
b1=Book("Thing Fail Aparts","Jonny Opara", 5000.01,13)
b2=Book("Send Your Account Detail","Abu Banaat",1000,100.5)

print(b1.description)
print(b1.description)

