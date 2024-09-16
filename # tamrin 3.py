# tamrin 3
class Book:
    title ="book title"
    author="book author"
    isbn = "1348"
    available=True
    def __init__(self,title,author,isbn) :
        self.title=title
        self.author=author
        self.isbn=isbn
    def __str__(self) :
        return f"title : {self.title}, author : {self.author}, isbn :{self.isbn}"
    def borrow(self):
        available =False
    def return_book(self):
        available =True
