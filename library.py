import os

# Configuration: Text file used to store the catalogue
FILE_NAME = "books.txt"

def initialize_catalogue():
    """Ensures the text file exists before the program starts."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass  # Creates an empty file safely

def add_book():
    """Appends a new book entry to the text file."""
    print("\n--- Add New Book ---")
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    isbn = input("Enter ISBN / Book ID: ").strip()
    
    # Validating simple inputs
    if not title or not author or not isbn:
        print("Error: All fields are required!")
        return

    # Appending the new record to the file
    with open(FILE_NAME, "a") as file:
        file.write(f"{title},{author},{isbn}\n")
    
    print(f"Success: '{title}' has been added to the catalogue.")

def search_book():
    """Searches for a book by title or author (case-insensitive search)."""
    print("\n--- Search Book ---")
    query = input("Enter part of Title or Author to search: ").strip().lower()
    
    if not query:
        print("Error: Search term cannot be empty!")
        return

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            # Strip newline character and split into elements
            if line.strip():
                title, author, isbn = line.strip().split(",")
                
                # Check for query match in title or author
                if query in title.lower() or query in author.lower():
                    print(f"-> Found: Title: {title} | Author: {author} | ISBN: {isbn}")
                    found = True
                    
    if not found:
        print("No matching books found in the catalogue.")

def generate_total_report():
    """Displays the total number of books stored in the file."""
    print("\n--- Report: Total Books ---")
    count = 0
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                count += 1
                
    print(f"Total number of books in the catalogue: {count}")

def generate_author_report():
    """Generates a filtered report listing all books by a specific author."""
    print("\n--- Report: Books by Author ---")
    target_author = input("Enter Author's Name: ").strip().lower()
    
    if not target_author:
        print("Error: Author name cannot be empty!")
        return

    count = 0
    print(f"\nBooks written by '{target_author}':")
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip():
                title, author, isbn = line.strip().split(",")
                if target_author in author.lower():
                    print(f" * Title: {title} (ISBN: {isbn})")
                    count += 1
                    
    print(f"Total matching books by this author: {count}")

def main():
    """Main program execution loop displaying the interactive menu."""
    initialize_catalogue()
    
    while True:
        print("\n===============================")
        print("   LIBRARY CATALOGUE SYSTEM    ")
        print("===============================")
        print("1. Add a New Book")
        print("2. Search for a Book")
        print("3. Report: Total Count of Books")
        print("4. Report: Books by Specific Author")
        print("5. Exit Program")
        print("===============================")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            generate_total_report()
        elif choice == "4":
            generate_author_report()
        elif choice == "5":
            print("\nThank you for using the Library Catalogue System. Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
