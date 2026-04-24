from validators import validate_title, validate_author, validate_price, validate_pages
from abc import ABC, abstractmethod
from datetime import datetime
from interfaces import Printable, Comparable, Categorizable

class Book(ABC):
    total_books = 0

    def __init__(self, title: str, author: str, price: float, pages: int):
        self._title = validate_title(title)
        self._author = validate_author(author)
        self._price = validate_price(price)
        self._pages = validate_pages(pages)
        self._is_available = True
        self._created_date = datetime.now()
        Book.total_books += 1

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
    
    @property
    def created_date(self):
        return self._created_date

    @price.setter
    def price(self, new_price):
        self._price = validate_price(new_price)

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
    
    @abstractmethod
    def calculate_price_with_tax(self) -> float:
        pass
    
    @abstractmethod
    def get_format_type(self) -> str:
        pass
    
    @abstractmethod
    def process(self) -> str:
        pass
    
    @abstractmethod
    def display_info(self) -> str:
        pass

    def __str__(self):
        status = "Available" if self._is_available else "Unavailable"
        return f"'{self._title}' | {self._author} | {self._pages} pages | ${self._price:.2f} | Status: {status}"

    def __repr__(self):
        return f"Book(title='{self._title}', author='{self._author}', price={self._price}, pages={self._pages})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self._title == other._title and self._author == other._author

class DigitalBook(Book, Printable, Comparable, Categorizable):
    
    def __init__(self, title: str, author: str, price: float, pages: int, file_size_mb: float, format_type: str = "PDF"):
        super().__init__(title, author, price, pages)
        self._file_size_mb = file_size_mb
        self._format_type = format_type
    
    @property
    def file_size_mb(self):
        return self._file_size_mb
    
    def calculate_price_with_tax(self) -> float:
        return round(self.price * 1.05, 2)
    
    def get_format_type(self) -> str:
        return f"Digital ({self._format_type})"
    
    def process(self) -> str:
        return f"Processing digital book '{self.title}' - Download link generated"
    
    def display_info(self) -> str:
        return f"DIGITAL: {self.title} by {self.author} | {self.pages} pages | {self.file_size_mb}MB | ${self.price}"
    
    def to_string(self) -> str:
        return f"[DigitalBook] '{self.title}' by {self.author} - ${self.price:.2f} (Tax: ${self.calculate_price_with_tax():.2f}) - {self.file_size_mb}MB"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, DigitalBook):
            return 1
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        else:
            return 0
    
    def get_category(self) -> str:
        return "Digital Book"
    
    def __str__(self):
        return self.to_string()

class Audiobook(Book, Printable, Comparable, Categorizable):
    
    def __init__(self, title: str, author: str, price: float, pages: int, duration_hours: float, narrator: str):
        super().__init__(title, author, price, pages)
        self._duration_hours = duration_hours
        self._narrator = narrator
    
    @property
    def duration_hours(self):
        return self._duration_hours
    
    @property
    def narrator(self):
        return self._narrator
    
    def calculate_price_with_tax(self) -> float:
        return round(self.price * 1.08, 2)
    
    def get_format_type(self) -> str:
        return "Audiobook"
    
    def process(self) -> str:
        return f"Processing audiobook '{self.title}' - Audio stream ready"
    
    def display_info(self) -> str:
        return f"AUDIOBOOK: {self.title} by {self.author} | {self.duration_hours} hours | Narrated by {self.narrator} | ${self.price}"
    
    def to_string(self) -> str:
        return f"[Audiobook] '{self.title}' by {self.author} - ${self.price:.2f} (Tax: ${self.calculate_price_with_tax():.2f}) - {self.duration_hours}h, narrated by {self.narrator}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Audiobook):
            return -1
        if self.duration_hours < other.duration_hours:
            return -1
        elif self.duration_hours > other.duration_hours:
            return 1
        else:
            return 0
    
    def get_category(self) -> str:
        return "Audiobook"
    
    def __str__(self):
        return self.to_string()

class PrintedBook(Book, Printable, Comparable, Categorizable):
    
    def __init__(self, title: str, author: str, price: float, pages: int, weight_grams: float, is_hardcover: bool = False):
        super().__init__(title, author, price, pages)
        self._weight_grams = weight_grams
        self._is_hardcover = is_hardcover
    
    @property
    def weight_grams(self):
        return self._weight_grams
    
    @property
    def is_hardcover(self):
        return self._is_hardcover
    
    def calculate_price_with_tax(self) -> float:
        return round(self.price * 1.10, 2)
    
    def get_format_type(self) -> str:
        return "Hardcover" if self._is_hardcover else "Paperback"
    
    def process(self) -> str:
        return f"Processing printed book '{self.title}' - Shipping label created"
    
    def display_info(self) -> str:
        cover_type = "Hardcover" if self._is_hardcover else "Paperback"
        return f"PRINTED: {self.title} by {self.author} | {self.pages} pages | {cover_type} | {self.weight_grams}g | ${self.price}"
    
    def to_string(self) -> str:
        cover = "HC" if self._is_hardcover else "PB"
        return f"[PrintedBook] '{self.title}' by {self.author} - ${self.price:.2f} (Tax: ${self.calculate_price_with_tax():.2f}) - {self.pages}p, {cover}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, PrintedBook):
            return -1
        if self.pages < other.pages:
            return -1
        elif self.pages > other.pages:
            return 1
        else:
            return 0
    
    def get_category(self) -> str:
        return "Printed Book"
    
    def __str__(self):
        return self.to_string()