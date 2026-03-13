# Paython_Labs

## lab01 (Вариант 2, Задача на 5)

### model.py (the basic kod)

```python
class Book:
    total_books = 0

    def __init__(self, title, author, price, pages):
        self._title = self._validate_title(title)
        self._author = self._validate_author(author)
        self._price = self._validate_price(price)
        self._pages = self._validate_pages(pages)
        self._is_available = True
        Book.total_books += 1

    def _validate_title(self, value):
        if not value or not isinstance(value, str) or value.strip() == "":
            raise ValueError("Title cannot be empty and must be a string.")
        return value.strip()

    def _validate_author(self, value):
        if not value or not isinstance(value, str) or value.strip() == "":
            raise ValueError("Author name cannot be empty.")
        return value.strip()

    def _validate_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value <= 0:
            raise ValueError("Price must be greater than zero.")
        return float(value)

    def _validate_pages(self, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError("Pages must be an integer.")
        if value <= 0:
            raise ValueError("Pages must be greater than zero.")
        return value

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def price(self):
        return self._price

    @property
    def pages(self):
        return self._pages

    @property
    def is_available(self):
        return self._is_available

    @price.setter
    def price(self, new_price):
        self._price = self._validate_price(new_price)

    @is_available.setter
    def is_available(self, status: bool):
        if not isinstance(status, bool):
            raise TypeError("Status must be True or False.")
        self._is_available = status

    def borrow(self):
        if not self._is_available:
            raise Exception("Cannot borrow the book because it is currently unavailable.")
        self._is_available = False

    def return_book(self):
        self._is_available = True

    def apply_discount(self, discount_percent: float) -> float:
        if not self._is_available:
            raise Exception("Cannot apply discount to an unavailable book.")
        if not 0 < discount_percent <= 100:
            raise ValueError("Discount percent must be between 1 and 100.")
        discount_amount = self._price * (discount_percent / 100)
        self._price = round(self._price - discount_amount, 2)
        return self._price

    def get_shipping_weight(self) -> float:
        if self._pages <= 0:
            return 0.0
        weight = round(self._pages * 0.01, 2)
        return weight

    def __str__(self):
        status = "Available" if self._is_available else "Unavailable"
        return f"'{self._title}' | {self._author} | {self._pages} pages | ${self._price:.2f} | Status: {status}"

    def __repr__(self):
        return f"Book(title='{self._title}', author='{self._author}', price={self._price}, pages={self._pages})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self._title == other._title and self._author == other._author
```

### demo.py (printing/directing)

```python
from model import Book

def run_demo():
    print("=" * 60)
    print("Python OOP Lab 1: Book Class".center(60))
    print("=" * 60)

    print("\n[1] Creating valid objects:")
    book1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 25.50, 300)
    book2 = Book("The 7 Habits of Highly Effective People", "Stephen Covey", 30.00, 420)
    print(book1)
    print(book2)

    print("\n[2] Official representation (repr):")
    print(repr(book1))
    print(repr(book2))

    print("\n[3] Comparing objects:")
    book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 20.00, 200)
    print(f"book1 == book3? {book1 == book3}")

    print("\n[4] Accessing properties:")
    print(f"First book title: {book1.title}")
    print(f"Second book author: {book2.author}")

    print("\n[5] Modifying price using setter:")
    book1.price = 29.99
    print(f"New price: ${book1.price}")
    try:
        book1.price = -10
    except ValueError as e:
        print(e)

    print("\n[6] Class attribute (total_books):")
    print(f"Total books created (via class): {Book.total_books}")
    print(f"Total books created (via object): {book1.total_books}")

    print("\n[7] Object state management:")
    print(f"book1 availability before borrowing: {book1.is_available}")
    book1.borrow()
    print(f"book1 availability after borrowing: {book1.is_available}")
    try:
        book1.borrow()
    except Exception as e:
        print(e)
    book1.return_book()
    print(f"book1 availability after return: {book1.is_available}")

    print("\n[8] Business methods:")
    book1.apply_discount(15)
    print(f"Price after 15% discount: ${book1.price}")
    book1.is_available = False
    try:
        book1.apply_discount(10)
    except Exception as e:
        print(e)
    book1.is_available = True
    book1.apply_discount(10)
    print(f"Shipping weight: {book1.get_shipping_weight()} kg")

    print("\n[9] Error handling during object creation:")
    try:
        book_bad = Book("", "Author", 100, 100)
    except ValueError as e:
        print(e)
    try:
        book_bad = Book("Valid Title", "Author", -50, 100)
    except ValueError as e:
        print(e)
    try:
        book_bad = Book("Valid Title", "Author", 100, -5)
    except ValueError as e:
        print(e)

    print("\n" + "=" * 60)
    print("Demo completed successfully.".center(60))
    print("=" * 60)

if __name__ == "__main__":
    run_demo()
```

![alt text](/images/lab01/Screenshot%202026-03-13%20131005.png)
![alt text](/images/lab01/Screenshot%202026-03-13%20131040.png)