# -*- coding: utf-8 -*-
from Book import Book

#First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []
        
    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        return b
    
    def removeBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        for book in self.books:
            if book==b:
                self.books.remove(b)
                self.different_book_count -= 1
        return b
    
    #Only available to admin
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)
  
    def searchByName(self,name):
        for book in self.books:
            if name.strip() == book.name:
                print("book available")
                return book
        else:
            print("book not available")
    
    def searchByAuthor(self,author):
        for book in self.books:
            if author.strip() == book.author:
                print("book available")
                return book
        else:
            print("book not available")
            
#    def issueBook(self, name, isbn):
#        for book in self.books:
#            if name.strip() in book.name:
#                print("You have now borrowed : ",name)
#                self.removeBookItem(name,isbn)
#                return True
#        else:
#            print("Sorry, requested_book is not there in our library at the moment")
#            return False
#        
#    def returnBook(self, name, isbn, rack, days=10):
#        for book in self.books:
#            if name.strip() in book.name:
#                if days > 10:
#                    fine = (days - 10)*20
#                    print("Thankyou for returning book {}. As the due date exeded please pay the fine of Rs.{} charged @Rs.20/day".format(name,fine))
#                    self.addBookItem(name,isbn,rack)
#                else:
#                    print("Thankyou for returning borrowed book : ",name)
#                    self.addBookItem(name,isbn,rack)
#                    return True
#        else:
#            print("Sorry, returned book is not borrowed by you..")
#            return False
#        
    def displayAllBooks(self):
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        
        print ('Total Book Count',c)
        print ('Different Book Count',self.different_book_count)

    def removeBookItem(self,name,isbn):
        book = self.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)