print("Welcome to Library Manager")

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-4): ")

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
    book_title = input("Enter the book's title please")
    book_author = input("Enter the book's title please")
    book_publication_year = input("Enter the book's title please")
    book_genre = input("Enter the book's title please")
    book_status = input("Enter the book's tit   le please")
    book = {
        'title': book_title,
        'author': book_author,
        'publication_year': book_publication_year,
        'genre': book_genre,
        'status': book_status
    }
    
    print("Adding book...")

def remove_book():
    print("Removing book...")

def search_book():
    print("Searching book...")

def display_books():
    print("All books")

def display_statistics():
    print("Stats")


if __name__ == "__main__":
    main_menu()