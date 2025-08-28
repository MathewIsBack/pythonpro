# Store data in dictionaries,

# Add/remove/search items,

# Use loops and conditions,

# Work with keys & values.

# A dictionary where books are stored as key-value pairs (book: availability)
library = {
    "harry potter": "available",
    "lord of the rings": "available",
    "the hobbit": "available",
    "sherlock holmes": "available"
}

while True:
    print("\n===== Library Menu======")
    print("1. View all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Add a new book")
    print("5. Remove a book")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        print("\nAvailable Books:")
        for book, status in library.items():
            print(f"{book.title()} ({status})")
    
    elif choice == "2":
        book = input("What book will you like to borrow: ").lower()

        if library.get(book) == "available":
            library[book] = "borrowed"
            print(f"You borrowed '{book.title()}'")

        elif library.get(book) == "borrowed":
            print(f"{book.title()} is already borrowed.")

        else:
            print("Book not found in library")

    elif choice == "3":
        book = input("What book would you like to return: ").lower()
        if library.get(book) == "borrowed":
            library[book] = "available"
            print(f"You returned '{book.title()}'")
        else:
            print("This book was not borrowed or not in the library")

        
    elif choice == "4":
        book = input("What book would you like to add: ").lower()

        if book in library:
            print("Book already in library")
        else:
            library[book] = "available"
            print(f"{book.title()} has been added to the library")

    elif choice == "5":
        book = input("What book would you like to remove: ").lower()
        if book in library:
            library.pop(book)
            print(f"'{book.title()}' has been removed")
        else:
            print(f"{book.title()} not found")

    elif choice == "6":
        print("Exiting Library systems... Goodbye")
        break

    else:
        print("Invalid choice! Please select a number between 1-6.")