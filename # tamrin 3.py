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
class Member:
    name="name"
    member_id="M098"
    borrowed_books=[]
    def __init__(self,name,member_id) :
        self.name=name
        self.member_id=member_id
    def __str__(self) :
        return f"name : {self.name}, member id: {self.member_id}"
    def borrow_book(self,book):
        self.borrowed_books.append(book)
        book.borrow()
    def return_book(self,book):
        self.borrowed_books.remove(book)
        book.return_book()
class Library:
    books=[]
    members=[]
   
    def __init__(self) :
         books=[]
         members=[]
    def add_book(self,book):
        self.books.append(book)
    def register_member(self,member):
        self.members.append(member)
    def issue_book(self,member_id,isbn):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.isbn == isbn:
                        member.borrow_book(book)
    def return_book(self,member_id,isbn):
         for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.isbn == isbn:
                        member.return_book(book)

book1 = Book("1984", "جورج اورول", "1234567890")
book2 = Book("کشتن مرغ مقلد", "هارپر لی", "0987654321")

# ایجاد کتابخانه و اضافه کردن کتاب‌ها
library = Library()
library.add_book(book1)
library.add_book(book2)

# ثبت یک عضو
member = Member("آلیس", "M001")
library.register_member(member)

# امانت دادن کتاب به عضو
library.issue_book("M001", "1234567890")

# بازگرداندن کتاب
library.return_book("M001", "1234567890")
#https://github.com/FatemehHosseini2024/library_management_system



        

