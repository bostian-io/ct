class Book:
    """Book class represents a book in the library"""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False
 
    def check_out(self): 
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."
    
    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."

    def __repr__(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"[{status}] {self.title} by {self.author}"

class EBook(Book):
    """EBook class represents an electronic book, inheriting from Book"""

    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size = file_size_mb  # in MB
        self.check_out_count = 0

    def check_out(self):
        self.check_out_count += 1
        self.checked_out = True
        return f"{self.title} has been checked out. Total checkouts: {self.check_out_count}"

    def return_book(self):
        if self.check_out_count > 0:
            self.checked_out_count -= 1
            self.checked_out = self.check_out_count > 0
            return f"{self.title} has been returned. Remaining checkouts: {self.check_out_count}"

    def __repr__(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"[{status}] {self.title} by {self.author}, {self.year}, File Size: {self.file_size}MB"

class Catalog:
    """Catalog class to manage a collection of books"""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"{book.title} has been added to the catalog."

    def search_by_author(self, author):
        results = [book for book in self.books if book.author == author]
        return results if results else f"No books found by {author}."

    def search_by_title(self, keyword):
        results = [book for book in self.books if keyword in book.title.lower()]
        return results if results else f"No books found with the title '{keyword}'."

    def get_available(self):
        available_books = [book for book in self.books if not book.checked_out]
        return available_books if available_books else "No available books in the catalog."

    def summary(self):
        summary = {}
        for book in self.books:
            summary[book.title] = {
                "author": book.author,
                "year": book.year,
                "checked_out": book.checked_out
            }
        return summary


catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

print(catalog.summary())
