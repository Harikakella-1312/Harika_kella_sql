#Q3. Create an abstract class Book with an abstract method get_summary().
#Implement subclasses: FictionBook, Textbook, and Magazine,
#  each with a unique summary format.
#Use encapsulation to store title and author, 
# validating that both are non-empty.
#Create a method print_all_summaries() that takes a 
# list of books and prints their summaries.
#Add a custom exception MissingBookInfoError.

from abc import ABC, abstractmethod

class MissingBookInfoError(Exception):
    pass

class Book(ABC):
    def __init__(self, title, author):
        self.__title = None
        self.__author = None
        
        self.set_title(title)
        self.set_author(author)

    def get_title(self):
        return self.__title
   
    def set_title(self, title):
        if not title:
            raise ValueError("Title can't be empty")
        self.__title = title

    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        if not author:
            raise ValueError("author can't be empty")
        self.__author = author

    @abstractmethod

    def get_summary(self):
        pass

class FictionBook(Book):
    def get_summary(self):
        return f"FictionBook {self.get_title()} author: {self.get_author()}"
    
class Textbook(Book):
    def get_summary(self):
        return f"Textbook {self.get_title()} author: {self.get_author()}"
    
class Magazine(Book):
    def get_summary(self):
        return f"Magazine {self.get_title()} author: {self.get_author()}"



def print_all_summaries(Books):

    for book in Books:
        print(book.get_summary())

books =[]

num = int(input("How many books to enter? "))

for i in range(num):
    print(f"\nEnter details for Book {i+1}:")
    title = input("Title: ")
    author = input("Author: ")
    book_type = input("Type (Fiction/Textbook/Magazine): ")

    try:
        if book_type.lower() == "fiction":
            books.append(FictionBook(title, author))
        elif book_type.lower() == "textbook":
            books.append(Textbook(title, author))
        elif book_type.lower() == "magazine":
            books.append(Magazine(title, author))
        else:
            print("Invalid book type.")
    except MissingBookInfoError as e:
        print(f"Error: {e}")

# Print summaries using polymorphism
print("\n--- Book Summaries ---")
print_all_summaries(books)
        

    