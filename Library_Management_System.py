class Library:
    book_list = []
    @classmethod
    def entrybook(self,book):
        self.book_list.append(book) 

    
class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id = book_id 
        self.__title = title 
        self.__author = author 
        self.__availability = availability 
    
    def borrow_book(book_id):
        for book in Library.book_list:
            if book.__book_id == book_id :
                if book.__availability == True :
                    book.__availability = False 
                    print("Book is available")
                else :
                    print("Book is not available") 

    def return_book(book_id):
        for book in Library.book_list:
            if book.__book_id == book_id :
                if book.__availability == True :
                    print('You didnot take this book so you can not return it')
                else :
                    book.__availability = True 
                    print("Book returned successfully")
    
    def view_book_info():
        for book in Library.book_list:
            print(f'book_id : {book.__book_id} , title : {book.__title} , author : {book.__author} , availability : {book.__availability}')

    def __repr__(self):
        return f"Book({self.__book_id}, '{self.__title}', '{self.__author}', {self.__availability})"


book1 = Book(1,'A Study in Scarlet','Sir Arthur Conan Doyle',True) 
book2 = Book(2,'The Sign of Four','Sir Arthur Conan Doyle',True) 

Library.entrybook(book1) 
Library.entrybook(book2) 

def menu() :
    while True:
        print('\n ***** Choose Your Option ***** \n')
        print('1.View Book Info\n2.Borrow Book.\n3.Return Book\n4.Exit')
        try:
            type = int(input('Enter your option:'))
            if type==1 :
                Book.view_book_info()
            elif type==2 :
                try :
                    book_id = int(input('Enter book id : '))
                    Book.borrow_book(book_id) 
                except :
                    print('Try to enter valid id')
            elif type==3:
                try:
                    book_id = int(input('Enter book id : '))
                    Book.return_book(book_id)
                except :
                    print('Try to enter valid id')
            elif type==4:
                break 
            else :
                print('Option is not available')
        except:
            print('Please choose correct option')

menu()




        