class Library:
    def __init__(self):
        # Constructor: open the file
        self.books_file = open('books.txt', 'a+')

    def __del__(self):
        # Destructor: close the file
        self.books_file.close()

    def list_books(self):
        self.books_file.seek(0)  # Go to the beginning of the file
        books = self.books_file.read().splitlines()
        if not books:
            print("No books currently in the library.")
            return
        for book in books:
            book_info = book.split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter the first release year: ")
        pages = input("Enter the number of pages: ")
        self.books_file.write(f"{title}, {author}, {year}, {pages}\n")
        self.books_file.flush()  # Ensure the data is written to the file

    def remove_book(self):
        with open('books.txt', 'r') as file:
            lines = file.readlines()

        if not lines:
            print("No books currently in the library.")
            return

        title_to_remove = input("Enter book title to remove: ").strip().upper()
        books_to_remove = []

        with open('books.txt', 'w') as file:
            for line in lines:
                title = line.split(',')[0].strip().upper()
                print(title)
                print(title_to_remove)
                if title_to_remove in title:
                    books_to_remove.append(line)
                else:
                    file.write(line)

        if not books_to_remove:
            print("No matching books found.")
            return  # Early return if no books match the query

        # Handle the case where multiple or no books are found
        if not books_to_remove:
            print("No matching books found.")
        elif len(books_to_remove) == 1:
            confirm = input(f"Did you mean to remove '{books_to_remove[0]}'? (y/n): ").lower()
            if confirm == 'y':
                print(f"Book '{title}' has been removed.")
            else:
                with open('books.txt', 'a') as file:
                    file.write(books_to_remove[0])
        else:
            print("Multiple books found:")
            for idx, book in enumerate(books_to_remove, 1):
                print(f"{idx}. {book}")
            book_idx = int(input("Enter the number of the book you want to remove: ")) - 1
            if 0 <= book_idx < len(books_to_remove):
                confirm = input(f"Are you sure you want to remove '{books_to_remove[book_idx]}'? (y/n): ").lower()
                if confirm == 'y':
                    books_to_remove.pop(book_idx)
                    print("Book removed.")
                else:
                    print("No books were removed.")
            else:
                print("Invalid selection.")

            # Rewrite the removed books back to the file except the selected one
            with open('books.txt', 'a') as file:
                for book in books_to_remove:
                    file.write(book)


# Create an instance of the Library class
lib = Library()

# User interaction menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit\n")

    choice = input("Enter the menu item number: ")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
