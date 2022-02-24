
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableClass():
    value1:str = "Value 1"
    value2:int = 0
        
    
obj = ImmutableClass()
print(obj.value1)

# TODO: Attempt change the value of a immutable class throw an existing 
obj.value1 = "Another Value"  
print(obj.value)
        
    # TODO use the __call__ method to call the object like a function
    
    
# b1=Book("Thing Fail Aparts","Jonny Opara", 5000.01,13)
# b2=Book("Send Your Account Detail","Abu Banaat",1000,100.5)

# print(b1.title)
# print(b1.pages)


# print(b1)


# print(b1 == b2)

 