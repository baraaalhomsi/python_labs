from lab03.base import Book
from lab03.models import PrintedBook, EBook, AudioBook

def by_title(book):
    return book.title.lower()

def by_price(book):
    return book.price

def by_pages(book):
    return book.pages

def by_author(book):
    return book.author.lower()

def by_price_then_title(book):
    return (book.price, book.title.lower())

def by_type_then_price(book):
    return (book.get_format_type(), book.price)

def by_times_borrowed(book):
    if isinstance(book, PrintedBook):
        return book.times_borrowed
    return 0

def is_available(book):
    return book.is_available

def is_expensive(book):
    return book.price > 30.0

def is_printed_book(book):
    return isinstance(book, PrintedBook)

def is_ebook(book):
    return isinstance(book, EBook)

def is_audio_book(book):
    return isinstance(book, AudioBook)

def is_bestseller(book):
    if isinstance(book, PrintedBook):
        return book.times_borrowed >= 0
    if isinstance(book, AudioBook):
        return book.times_played >= 0
    if isinstance(book, EBook):
        return book.times_downloaded >= 0
    return False

def make_price_filter(max_price):
    def filter_fn(item):
        return item.price <= max_price
    return filter_fn

def make_price_range_filter(min_price, max_price):
    def filter_fn(item):
        return min_price <= item.price <= max_price
    return filter_fn

def make_discount_func(discount_percent):
    def apply_discount(item):
        if item.is_available:
            item.apply_discount(discount_percent)
        return item
    return apply_discount

def make_format_filter(format_type):
    def filter_fn(item):
        if isinstance(item, EBook):
            return item.format_type == format_type
        if isinstance(item, PrintedBook):
            return item.cover_type == format_type
        return False
    return filter_fn

class DiscountStrategy:
    def __init__(self, percentage):
        self.percentage = percentage
    
    def __call__(self, item):
        if item.is_available:
            item.apply_discount(self.percentage)
        return item

class PriceIncreaseStrategy:
    def __init__(self, percentage):
        self.percentage = percentage
    
    def __call__(self, item):
        item.price = round(item.price * (1 + self.percentage / 100), 2)
        return item

class ProcessStrategy:
    def __call__(self, item):
        item.process()
        return item

class ActivateStrategy:
    def __init__(self, available=True):
        self.available = available
    
    def __call__(self, item):
        item.is_available = self.available
        return item

class BorrowStrategy:
    def __call__(self, item):
        if item.is_available:
            if isinstance(item, PrintedBook):
                item.borrow_with_tracking()
            else:
                item.borrow()
        return item

class ReturnStrategy:
    def __call__(self, item):
        item.return_book()
        return item