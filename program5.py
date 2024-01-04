# Write a program in python to manage a library catalog, use control structures to add search for and checkout books and maintain the library's inventyory
libraryinventory = {}
# Main loop for the library catalog
while True:
    print("Library Catalog Menu:")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Checkout Book")
    print("4. Exit")
    choice = str(input("Enter your choice (a-d): "))
    if choice == '1':
        # Add Book
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        quantity = int(input("Enter the quantity of the book: "))
        
        if title in libraryinventory:
            libraryinventory[title]['quantity'] += quantity
        else:
            libraryinventory[title] = {'author': author, 'quantity': quantity}
    elif choice == '2':
        # Search Book
        title = input("Enter the title of the book to search: ")
        
        if title in libraryinventory:
            book_info = libraryinventory[title]
            print(f"Title: {title}, Author: {book_info['author']}, Quantity: {book_info['quantity']}")
        else:
            print(f"Book with title '{title}' not found in the library.")
    elif choice == '3':
        # Checkout Book
        title = input("Enter the title of the book to checkout: ")  
        if title in libraryinventory:
            if libraryinventory[title]['quantity'] > 0:
                libraryinventory[title]['quantity'] -= 1
                print(f"You have successfully checked out '{title}'.")
            else:
                print(f"Sorry, '{title}' is out of stock.")
        else:
            print(f"Book with title '{title}' not found in the library.")
    elif choice == '4':
        # Exit
        print("Exiting the library catalog. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")