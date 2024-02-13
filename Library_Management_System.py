class Library:
    def __init__(self):
        # Constructor: open the file
        self.books_file = open('books.txt', 'a+')

    def __del__(self):
        # Destructor: close the file
        self.books_file.close()

    def list_books(self):
        # List all the books
        self.books_file.seek(0)  # Go to the beginning of the file
        books = self.books_file.read().splitlines()
        for book in books:
            book_info = book.split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        # Add a new book
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter the first release year: ")
        pages = input("Enter the number of pages: ")
        self.books_file.write(f"{title},{author},{year},{pages}\n")

    def remove_book(self):
        # Get the title to remove from the user, case insensitive
        title_to_remove = input("Enter book title to remove: ").strip().lower()
        book_found = False

        # Open the file using a context manager
        with open('books.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)  # Go to the beginning of the file
            file.truncate()  # Clear the file

            for line in lines:
                # Extract title for comparison, assuming the title is the first element
                title = line.split(',')[0].strip().lower()

                if title != title_to_remove:
                    file.write(line)  # Write the line back to the file if it's not the book to remove
                else:
                    book_found = True  # Mark as found, but don't write it back (effectively deleting it)

            if not book_found:
                print("Book not found. No book has been removed.")
            else:
                # Ask for confirmation before deletion
                confirm = input(f"Are you sure you want to remove '{title_to_remove}'? (y/n): ").lower()
                if confirm == 'y':
                    print(f"Book '{title_to_remove}' has been removed.")
                else:
                    # Write the removed book back to the file
                    file.write(f"{title_to_remove}\n")
                    print("No books were removed.")


# Create an instance of the Library class
lib = Library()

# User interaction menu
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

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
