class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author = author
        self.price=price
        
    # TODO: the __eq__ method checks for equallity between objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == value.title and self.author == value.author and self.price == value.price) 
    
    # TODO : the __get__ establishs >= relationship with another obj
    def __gt__(self, value):
        if not isinstance(value, Book):
            raise  ValueError('Cant compare a book to a non-book')
        return self.price >= value.price
    
    # TODO : the __it__establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise  ValueError('Cant compare a book to a non-book')
        return self.price < value.price
    
b1=Book("Thing Fail Aparts","Jonny Opara", 5000)
b2=Book("Send Your Account Detail","Abu Banaat",1000)
b3=Book("Thing Fail Aparts","Jonny Opara", 5000)
b4=Book("To kill a Mocingbird","Harper lee",1000)

# TODO: Check for equality
# print(b1 == b3)
# print(b1 == b2)
# print(b2 == 40)

# TODO check for greater than and lesser value
# print(b2 > b1)
# print(b2 < b1)



# TODO now we can sort them too
books = [b1, b2, b3, b4]

books.sort()
print([book.title for book in books])

 