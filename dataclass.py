
from dataclasses import dataclass

@dataclass
class Book:
        title:str
        author:str
        pages:int
        price:float
        
    # TODO: use the __str__ method to return a string
   
        
    # TODO use the __call__ method to call the object like a function
    
    
b1=Book("Thing Fail Aparts","Jonny Opara", 5000.01,13)
b2=Book("Send Your Account Detail","Abu Banaat",1000,100.5)

print(b1.title)
print(b1.pages)


print(b1)


print(b1 == b2)

 