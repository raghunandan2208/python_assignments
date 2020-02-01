#-*- coding: utf-8 -*-
from Book import Book
from BookItem import BookItem
from Catalog import Catalog
from User import User, Member, Librarian

catalog = Catalog()


while True:
    print("************Welcome to Edyoda Library**************")
    print()
    print(
          """
          Login Page
          
          1. Librarian
          2. Student
          3. Exit
          
          """
          )
    
    choice = int(input("Enter Your Choice : "))
    try:
        choice = int(choice)
    except ValueError:
        print("That's not an int!")
        continue
            
    if choice == 1:      
        print(
              """
              Welcome to Librarian Desk
              a. Add Book
              b. Add Book item
              c. Remove Book
              d. Remove Book item
              e. Search Book by Title
              f. Search Book by Author
              g. Display Catalog
              h. Add Member
              i. Issue Book
              j. Return Book
              k. Exit
              """)
        choice = input("Enter your choice: ")
        if choice == 'a' or choice == 'A':
            while True:
                name = input("Enter book title: ")
                author = input("Enter book Author: ")
                publish_date = input("Enter Publish date: ")
                pages = input("Enter Number of Pages: ")
                b1 = Book(name,author,publish_date,pages)
                b = catalog.addBook(name,author,publish_date,pages)
                catalog.displayAllBooks()
                print("The following Book: {} by {} added successfully".format(b1.name,b1.author))
                choice = input("Do you wish to add another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        if choice == 'b' or choice == 'B':
            while True:
                print("Add book items: ")
                isbn = input("Enter ISBN number: ")
                rack = input("Enter Rack number: ")
                b1.addBookItem(isbn,rack)
                catalog.addBookItem(b,isbn,rack)
                catalog.displayAllBooks()
                print("The following Book Item added successfully")
                choice = input("Do you wish to add another book item (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        if choice == 'c' or choice == 'C':
            while True:
                name = input("Enter book title to remove: ")
                author = input("Enter book Author: ")
                publish_date = input("Enter Publish date: ")
                pages = input("Enter Number of Pages: ")
                br1 = Book(name,author,publish_date,pages)
                br = catalog.removeBook(name,author,publish_date,pages)
                catalog.displayAllBooks()
                print("The following Book: {} by {} added successfully".format(b1.name,b1.author))
                choice = input("Do you wish to remove another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        if choice == 'd' or choice == 'D':
            while True:
                print("Remove book items: ")
                name = input("Enter Book Title: ")
                isbn = input("Enter ISBN number: ")
                catalog.removeBookItem(name,isbn)
                print("The following Book Item removed successfully")
                choice = input("Do you wish to remove another book item (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
            
        if choice == 'e' or choice == 'E':
            while True:
                name = input("Enter Title of book to search: ")
                catalog.searchByName(name)
                choice = input("Do you wish to search another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        if choice == 'f' or choice == 'F':
            while True:
                author = input("Enter Author of book to search: ")
                catalog.searchByAuthor(author)
                choice = input("Do you wish to search another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        if choice == 'g' or choice == 'G':
            print("===== CATALOG =====")
            catalog.displayAllBooks()
            choice = input("Do you wish to continue (y/n): ")
            if choice == 'y':
                continue
            else:
                break
            
        elif choice == 'h' or choice == 'H':
            while True:
                print("Please enter the following new member details:")
                name = input("Enter New member name: ")
                location = input("Enter member location: ")
                age = input("Age of the member: ")
                aadhar_id = input("Aadhar ID number: ")
                student_id = input("Student ID number: ")
                m1 = Member(name, location, age, aadhar_id,student_id)
                choice = input("Do you wish to add another member (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
        
        elif choice == 'i' or choice == 'I':
            while True:
                name = input("Enter title of book to borrow: ")
                isbn = input("Enter ISBN : ")
                catalog.issueBook(name,isbn)
                choice = input("Do you wish to borrow another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
        
        elif choice == 'j' or choice == 'J':
            while True:
                name = input("Enter title of book to return: ")
                isbn = input("Enter ISBN : ")
                rack = input("Enter rack number: ")
                days = int(input("Enter number of days you have borrowed this book: "))
                catalog.returnBook(name,isbn,rack,days)
                choice = input("Do you wish to return another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        elif choice == 'k' or choice == 'K':
            break
        
    if choice == 2:      
        print(
              """
              Welcome to Student Desk:
              
              a. Display Catalog
              b. Student registration
              c. Search Book by Title
              d. Search Book by Author
              e. Borrow Book
              f. Return Book
              g. Exit
              
              """)
        choice = input("Enter your choice: ")
        if choice == 'a' or choice == 'A':
            print("===== CATALOG =====")
            catalog.displayAllBooks()
            choice = input("Do you wish to continue (y/n): ")
            if choice == 'y':
                continue
            else:
                break
        if choice == 'b' or choice == 'B':   
             while True:
                print("Please enter the following new member details:")
                name = input("Enter New member name: ")
                location = input("Enter member location: ")
                age = input("Age of the member: ")
                aadhar_id = input("Aadhar ID number: ")
                student_id = input("Student ID number: ")
                m1 = Member(name, location, age, aadhar_id,student_id)
                choice = input("Do you wish to add another member (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        if choice == 'c' or choice == 'C':
            while True:
                name = input("Enter Title of book to search: ")
                catalog.searchByName(name)
                choice = input("Do you wish to search another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        if choice == 'd' or choice == 'D':
            while True:
                author = input("Enter Author of book to search: ")
                catalog.searchByAuthor(author)
                choice = input("Do you wish to search another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
        elif choice == 'e' or choice == 'E':
            while True:
                name = input("Enter title of book to borrow: ")
                isbn = input("Enter ISBN : ")
                catalog.issueBook(name,isbn)
                choice = input("Do you wish to borrow another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
        
        elif choice == 'f' or choice == 'f':
            while True:
                name = input("Enter title of book to return: ")
                isbn = input("Enter ISBN : ")
                rack = input("Enter rack number: ")
                days = int(input("Enter number of days you have borrowed this book: "))
                catalog.returnBook(name,isbn,rack,days)
                choice = input("Do you wish to return another book (y/n): ")
                if choice == 'y':
                    continue
                else:
                    break
            
        elif choice == 'g' or choice == 'G':
            break
        
#        
#    if choice == 3:
#        print("Thankyou... Visit again....")
#        break
#    else:
#        break
#    
    
    
