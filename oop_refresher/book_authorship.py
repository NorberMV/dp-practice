# Define Author class
class Author:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def get_author_info(self):
        print(f"{self.name}, (born {self.birth_year})")


class Book:
    def __init__(self, title: str, publication_year: int, author: Author):
        self.title = title
        self.publication_year = publication_year
        self.author = author

    def get_book_info(self):
        print(f"{self.title} by ({self.author.name}), publicated at {self.publication_year}")


if __name__ == "__main__":
    # Create authors
    author1 = Author("George Orwell", 1903)
    author2 = Author("Jane Austen", 1775)

    # Create books
    book1 = Book("1984", 1949, author1)
    book2 = Book("Animal Farm", 1945, author1)
    book3 = Book("Pride and Prejudice", 1813, author2)

    # Display author information
    print("=== Authors ===")
    author1.get_author_info()
    author2.get_author_info()

    print("\n=== Books ===")
    book1.get_book_info()
    book2.get_book_info()
    book3.get_book_info()