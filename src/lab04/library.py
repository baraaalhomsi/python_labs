from typing import List, Optional, Callable
from models import Book, Printable, Comparable

class Library:

    def __init__(self):
        self._items: List[Book] = []
    
    def add(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError(f"Cannot add {type(book).__name__}. Expected Book object.")
        
        for existing_book in self._items:
            if existing_book == book:
                raise ValueError(f"Book '{book.title}' by {book.author} already exists in the library.")
        
        self._items.append(book)
    
    def remove(self, book: Book) -> bool:
        if not isinstance(book, Book):
            raise TypeError("Expected Book object.")
        
        for i, existing_book in enumerate(self._items):
            if existing_book == book:
                del self._items[i]
                return True
        return False
    
    def remove_at(self, index: int) -> Book:
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Index {index} out of range. Library has {len(self._items)} books.")
        
        return self._items.pop(index)
    
    def get_all(self) -> List[Book]:
        return self._items.copy()
    
    def find_by_title(self, title: str) -> List[Book]:
        title_lower = title.lower().strip()
        return [book for book in self._items if title_lower in book.title.lower()]
    
    def find_by_author(self, author: str) -> List[Book]:
        author_lower = author.lower().strip()
        return [book for book in self._items if author_lower in book.author.lower()]
    
    def find_by_price_range(self, min_price: float, max_price: float) -> List[Book]:
        return [book for book in self._items if min_price <= book.price <= max_price]
    
    def get_available(self) -> 'Library':
        new_library = Library()
        for book in self._items:
            if book.is_available:
                new_library.add(book)
        return new_library
    
    def get_unavailable(self) -> 'Library':
        new_library = Library()
        for book in self._items:
            if not book.is_available:
                new_library.add(book)
        return new_library
    
    def get_expensive(self, threshold: float = 30.0) -> 'Library':
        new_library = Library()
        for book in self._items:
            if book.price > threshold:
                new_library.add(book)
        return new_library
    
    def get_printable(self) -> List[Printable]:
        return [book for book in self._items if isinstance(book, Printable)]
    
    def get_comparable(self) -> List[Comparable]:
        return [book for book in self._items if isinstance(book, Comparable)]
    
    def sort_by_title(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda book: book.title.lower(), reverse=reverse)
    
    def sort_by_author(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda book: book.author.lower(), reverse=reverse)
    
    def sort_by_price(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda book: book.price, reverse=reverse)
    
    def sort_by_pages(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda book: book.pages, reverse=reverse)
    
    def sort(self, key: Optional[Callable[[Book], any]] = None, reverse: bool = False) -> None:
        if key is None:
            self._items.sort(reverse=reverse)
        else:
            self._items.sort(key=key, reverse=reverse)
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            new_library = Library()
            for book in self._items[index]:
                new_library.add(book)
            return new_library
        elif isinstance(index, int):
            if index < 0 or index >= len(self._items):
                raise IndexError(f"Index {index} out of range.")
            return self._items[index]
        else:
            raise TypeError(f"Indices must be integers or slices, not{type(index).__name__}")
    
    def __contains__(self, book) -> bool:
        if not isinstance(book, Book):
            return False
        return any(existing_book == book for existing_book in self._items)
    
    def __str__(self) -> str:
        if len(self._items) == 0:
            return "Library is empty."
        
        result = f"Library contains {len(self._items)} book(s):\n"
        result += "-" * 50 + "\n"
        for i, book in enumerate(self._items):
            result += f"[{i}] {book}\n"
        result += "-" * 50
        return result
    
    def __repr__(self) -> str:
        return f"Library(books={repr(self._items)})"