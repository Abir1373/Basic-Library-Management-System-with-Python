

def menu() :
    while True:
        print('\n ***** Choose Your Option ***** \n')
        print('1.View Book Info\n2.Borrow Book.\n3.Return Book\n4.Exit')
        type = int(input('Enter your option:'))
        if type==1 :
            Book.view_book_info()
        elif type==2 :
            book_id = int(input('Enter book id : '))
            Book.borrow_book(book_id) 