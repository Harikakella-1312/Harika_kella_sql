# Q1. Design a Book class with attributes like title, author, and ISBN. 
#Create a Library class to manage a collection of books. 
#Include methods to add, remove, and search for books.
#Implement borrowing and returning mechanisms for books.

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def remove_book(self,isbn):
        self.books =[book for book in self.books if book.ISBN != isbn]
        print(f"book with ISBN {isbn} removed from library.")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if results:
            print("\nSearch Results:")
            for book in results:
                print(book)
        else:
            print("No matching books found.")

    def borrow_book(self, isbn):
         for book in self.books:
              if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You borrowed '{book.title}'.")
                return
         print("Book not available or already borrowed.")

    def return_book(self,isbn):
        for book in self.books:
            if book.ISBN == isbn and book.is_borrowed:
                book.is_borrowed = False
                print(f"You returned '{book.title}'.")
                return
        print("Book not found or was not borrowed.")

library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Show All Books")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter ISBN: ")
        new_book = Book(title, author, isbn)
        library.add_book(new_book)

    elif choice == "2":
        isbn = input("Enter ISBN of book to remove: ")
        library.remove_book(isbn)

    elif choice == "3":
        keyword = input("Enter title/author keyword: ")
        library.search_book(keyword)

    elif choice == "4":
        isbn = input("Enter ISBN of book to borrow: ")
        library.borrow_book(isbn)

    elif choice == "5":
        isbn = input("Enter ISBN of book to return: ")
        library.return_book(isbn)

    elif choice == "6":
        show_books()

    elif choice == "7":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

