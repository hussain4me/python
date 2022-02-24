# Python Object Oriented Programming by Joe Marini course
# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod

class JSON(ABC):
    def __init__(self):
        super().__init()
        
    @abstractmethod
    def toJson(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def calcArea(self):
        pass
  
    
class Circle(GraphicShape,JSON):
    def __init__(self, radius):
        self.radius=radius
        
    def calcArea(self):
        return 3.14 * (self.radius ** 2)
        
    def toJson(self):
        return f"{'Radius':{self.radius}}"
        
    
       
class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
        
    def calcArea(self):
        return self.side * self.side
    
# g=GraphicShape()
c=Circle(12)
print(c.calcArea())
print(c.toJson())

s = Square(4)
print(s.calcArea())
