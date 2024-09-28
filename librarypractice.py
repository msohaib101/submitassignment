#List to hold books
books = []

# list to hold user info 
users = []

# Book dictionary 
def create_book(book_id, title, author, genre):
    return {
        'ID' : book_id,
        'Title' : title,
        'Author' : author,
        'Genre' : genre,
        'Status' : 'Available' #All new books are available by default
    }

# User dictionary
def create_user(user_id, name):
    return{
        'ID' : user_id,
        'Name' : name,
        'BorrowedBooks' : [] #List to track books borrowed by the user
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
            print("Exiting system, Good Bye")
        else:
            print("invalid choice please try again")

#adding new books to our list
def add_book():
    book_id = input("Enter book ID:")
    title = input("Enter book title:")
    author = input("Enter book Author name:")
    genre = input("Enter book Genre:")

    book = create_book(book_id, title, author, genre)
    books.append(book)
    print(f"Book {title} added Successfully")

#adding user to our list
def add_user():
    user_id = input("Enter user ID:")
    name = input("Enter your name:")
    user = create_user(user_id, name)
    users.append(user)
    print(f"User {name} added successfully")

# view all books 
def view_books():
    if not books:
        print("No Book is Available currently")
    else:
        for book in books:
            print(f"ID: {book_id['ID']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Status: {book['Status']}")

#find book from list
def find_book(book_id):
    for book in books:
        if book['ID'] == book_id:
            return book
    return None

# find user from list 
def find_user(user_id):
    for user in users:
        if user['ID'] == user_id:
            return user
    return None

#Borrow a book from list
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


# Return A Book 
def return_book():
    user_id = input("Enter User ID: ")
    user = find_user(user_id)
    
    if user:
        book_id = input("Enter Book ID to Return: ")
        book = find_book(book_id)
        
        if book:
            if book and book in user['BorrowedBooks']:
                book['Status'] = 'Available'
                user['BorrowedBooks'].remove(book)
                print(f"Book '{book['Title']}' returned successfully by {user['Name']}.")
            else:
                print("Book not Found or Not Borrowed by this user.")
        else:
            print("User not found.")

# Search a book by title author or genre 
def search_books():
    search_type = input("Search books by Title, Author or Genre:").lower()
    search_query = input("Enter search").lower()

    for book in books:
        if search_type == "Title" and search_query in book['title'].lower():
            results.append(book)
        elif search_type == "Author" and search_query in book['title'].lower():
            results.append(book)
        elif search_type == "Genre" and search_query in book['genre'].lower():
            results.append(book)
    
    if results:
        for book in results:
            print(f"Book ID {book['ID']}, Author{book['author']}, Genre{book['genre']}, Status{book['Status']}")
    
    else:
        print("No book Found.")

# Display available books 
def view_available_books():
    available_books = [book for book in books if book['Status'] == 'Available']

    if available_books:
        for book in available_books:
            print(f"Book ID {book['ID']}, Author{book['author']}, Genre{book['genre']}, Status{book['Status']}") 

    else:
        print("No Books are Available")

# For all checked out books 

def view_checked_Out_books():
    checked_out_books = [book for book in books if book['Status'] == 'Checked Out']

    if checked_out_books:
        for book in checked_out_books:
            print(f"Book ID {book['ID']}, Author{book['author']}, Genre{book['genre']}, Status{book['Status']}") 

    else:
        print("No Books are Currently Checked Out")


# User Information storing 
def view_user_info():
    user = find_user(user_id)

    if user:
        print(f"User Name {user['name']}")
        if user['BorrowedBooks']:
            print("BorrowedBooks:")
            for book in user['BorrowedBooks']:
                print(f"ID: {book['ID']}, Title: {book['Title']}")
        else:
            print("No Books are borrowed")
    else:
        print("User Not Found.")
if __name__ == "__main__":
    main_menu()