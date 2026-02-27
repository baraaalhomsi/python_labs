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

    def str(self):
        status = "Available" if self._is_available else "Unavailable"
        return f"'{self._title}' | {self._author} | {self._pages} pages | ${self._price:.2f} | Status: {status}"

    def repr(self):
        return f"Book(title='{self._title}', author='{self._author}', price={self._price}, pages={self._pages})"

    def eq(self, other):
        if not isinstance(other, Book):
            return False
        return self._title == other._title and self._author == other._author