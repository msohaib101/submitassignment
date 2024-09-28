# List to hold books
books = []

# List to hold users
users = []

# Book dictionary structure
def create_book(book_id, title, author, genre):
    return {
        'ID': book_id,
        'Title': title,
        'Author': author,
        'Genre': genre,
        'Status': 'Available'  # All new books are available by default
    }

# User dictionary structure
def create_user(user_id, name):
    return {
        'ID': user_id,
        'Name': name,
        'BorrowedBooks': []  # List to track books borrowed by the user
    }
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Add a Book")
        print("5. Add a User")
        print("6. View User Information")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            add_book()
        elif choice == '5':
            add_user()
        elif choice == '6':
            view_user_info()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Add a new book to the system
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    genre = input("Enter Book Genre: ")
    
    book = create_book(book_id, title, author, genre)
    books.append(book)
    print(f"Book '{title}' added successfully!")

# Add a new user to the system
def add_user():
    user_id = input("Enter User ID: ")
    name = input("Enter User Name: ")
    
    user = create_user(user_id, name)
    users.append(user)
    print(f"User '{name}' added successfully!")

# View all books in the library
def view_books():
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")
# Find book by ID
def find_book(book_id):
    for book in books:
        if book['ID'] == book_id:
            return book
    return None

# Find user by ID
def find_user(user_id):
    for user in users:
        if user['ID'] == user_id:
            return user
    return None

# Borrow a book
def borrow_book():
    user_id = input("Enter User ID: ")
    user = find_user(user_id)
    
    if user:
        book_id = input("Enter Book ID to borrow: ")
        book = find_book(book_id)
        
        if book:
            if book['Status'] == 'Available':
                book['Status'] = 'Checked Out'
                user['BorrowedBooks'].append(book)
                print(f"Book '{book['Title']}' borrowed successfully by {user['Name']}.")
            else:
                print("Book is already checked out.")
        else:
            print("Book not found.")
    else:
        print("User not found.")

# Return a book
def return_book():
    user_id = input("Enter User ID: ")
    user = find_user(user_id)
    
    if user:
        book_id = input("Enter Book ID to return: ")
        book = find_book(book_id)
        
        if book and book in user['BorrowedBooks']:
            book['Status'] = 'Available'
            user['BorrowedBooks'].remove(book)
            print(f"Book '{book['Title']}' returned successfully by {user['Name']}.")
        else:
            print("Book not found or not borrowed by this user.")
    else:
        print("User not found.")
# Search for books
def search_books():
    search_type = input("Search by Title, Author, or Genre: ").lower()
    search_query = input("Enter search query: ").lower()
    
    results = []
    
    for book in books:
        if search_type == "title" and search_query in book['Title'].lower():
            results.append(book)
        elif search_type == "author" and search_query in book['Author'].lower():
            results.append(book)
        elif search_type == "genre" and search_query in book['Genre'].lower():
            results.append(book)
    
    if results:
        for book in results:
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")
    else:
        print("No books found.")
# Display all available books
def view_available_books():
    available_books = [book for book in books if book['Status'] == 'Available']
    
    if available_books:
        for book in available_books:
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")
    else:
        print("No available books.")

# Display all checked-out books
def view_checked_out_books():
    checked_out_books = [book for book in books if book['Status'] == 'Checked Out']
    
    if checked_out_books:
        for book in checked_out_books:
            print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}")
    else:
        print("No books currently checked out.")
def view_user_info():
    user_id = input("Enter User ID: ")
    user = find_user(user_id)
    
    if user:
        print(f"User Name: {user['Name']}")
        if user['BorrowedBooks']:
            print("Borrowed Books:")
            for book in user['BorrowedBooks']:
                print(f"ID: {book['ID']}, Title: {book['Title']}")
        else:
            print("No books borrowed.")
    else:
        print("User not found.")
if __name__ == "__main__":
    main_menu()
