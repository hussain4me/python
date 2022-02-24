
from dataclasses import dataclass,field
import random

def price_func():
    return  float(random.randrange(20,40))
    

@dataclass
class Book:
    title:str="No Title"
    author:str="No Author"
    pages:int=0
    # price:float=0.0
    # price:float = field(default=10.0)
    price:float = field(default_factory=price_func)
    
    
b1=Book("Thing Fail Aparts","Jonny Opara", 1225)
b2=Book("Send Your Account Detail","Abu Banaat", 234)

# b1 = Book()
print(b1)