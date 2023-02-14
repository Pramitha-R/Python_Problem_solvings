class Library():
    def __init__(self,list):
        self.book_list=list
        self.available_book_list=list[:]
        self.book_lent={}

    def display_available_book(self):
        for i in self.available_book_list:
            print(i)

    def display_all_book(self):
        for i in self.book_list:
            print(i)
        
    def lend_book(self,name,book):
        if book not in self.book_list:
            print("incorect book is not in our library")
            return
        elif book in self.available_book_list:
            self.book_lent.update({book:name})
            self.available_book_list.remove(book)
            print("you can tack the book.......")
        else:
            print("the book is already taken by"+ self.book_lent[book])
        
    def return_book(self,book):
        if(book not in self.book_lent):
            print("who are u")
            return
        else:
            self.available_book_list.append(book)
            del self.book_lent[book]


    
    

if __name__=="__main__":
    lib=Library(["The life Divine","Harry Potter","The Alchemist","The Ramayanam","Ponniyin Selvan"])

print("Welcome to library. Enter an option: ")
while True:
    print("1. Display available book")
    print("2. Display all book")
    print("3. borrow a book")
    print("4. Return a book")
    print("5. Quit")
    user_choice=int(input())
    if(user_choice==1):
        lib.display_available_book()
    elif(user_choice==2):
        lib.display_all_book()
    elif(user_choice==3):
        name=input("Enter the name: ")
        book=input("Enter the book name: ")
        lib.lend_book(name,book)
    elif(user_choice==4):
        book=input("Enter the return book name: ")
        lib.return_book(book)
    elif(user_choice==5):
        break
    else:
        print("invelid choice number")
    