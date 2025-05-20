print("Welcome to Library Manager")

library = [{
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': '1949',
        'genre': 'Dystopian',
        'status': 'Available'
    },
    {
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'publication_year': '1937',
        'genre': 'Fantasy',
        'status': 'Borrowed'
    }]

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
        
def add_book():
    book_title = input("Enter the book's title: ")
    book_author = input("Enter the book's author: ")
    book_publication_year = input("Enter the book's publication year: ")
    book_genre = input("Enter the book's genre: ")
    book_status = input("Enter the book's status: ")
    book = {
        'title': book_title,
        'author': book_author,
        'publication_year': book_publication_year,
        'genre': book_genre,
        'status': book_status
    }
    library.append(book)
    print(f"'{book_title}' added successfully!")
    return library

def remove_book():
    book_to_be_deleted = input("Enter the title of the book you'd like to be deleted: ")
    found = False
    
    for book in library:
        if book_to_be_deleted.lower() == book['title'].lower():
            library.remove(book)  
            found = True
            print(f"Book '{book_to_be_deleted}' has been removed successfully!")
            break
    
    if not found:
        print("Sorry the book could not be found in the Library")            

def search_book():
    searched_book = input("Please Input the book name you'd like to Search.")
    found = False

    for book in library:
        if searched_book.lower() in book['title'].lower() or searched_book.lower() in book['author'].lower():
            print("Book found:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['publication_year']}")
            print(f"Genre: {book['genre']}")
            print(f"Status: {book['status']}")
            found = True
    if not found:
            print("Sorry, the library does not contain such a book")

def display_books():
    print(library)

def display_statistics():
    print("Stats")

if __name__ == "__main__":
    main_menu()