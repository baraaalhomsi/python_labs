from lab03.base import Book

class Library:
    def __init__(self):
        self._items = []
    
    def add(self, book):
        for existing_book in self._items:
            if existing_book == book:
                raise ValueError(f"Book '{book.title}' by {book.author} already exists.")
        self._items.append(book)
    
    def remove(self, book):
        if not isinstance(book, Book):
            raise TypeError("Expected Book object.")
        for i, existing_book in enumerate(self._items):
            if existing_book == book:
                del self._items[i]
                return True
        return False
    
    def remove_at(self, index):
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Index {index} out of range.")
        return self._items.pop(index)
    
    def get_all(self):
        return self._items.copy()
    
    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate):
        self._items = [book for book in self._items if predicate(book)]
        return self
    
    def apply(self, func):
        for i in range(len(self._items)):
            self._items[i] = func(self._items[i])
        return self
    
    def find_by_title(self, title):
        title_lower = title.lower().strip()
        return [book for book in self._items if title_lower in book.title.lower()]
    
    def find_by_author(self, author):
        author_lower = author.lower().strip()
        return [book for book in self._items if author_lower in book.author.lower()]
    
    def find_by_price_range(self, min_price, max_price):
        return [book for book in self._items if min_price <= book.price <= max_price]
    
    def get_available(self):
        new_library = Library()
        for book in self._items:
            if book.is_available:
                new_library.add(book)
        return new_library
    
    def get_unavailable(self):
        new_library = Library()
        for book in self._items:
            if not book.is_available:
                new_library.add(book)
        return new_library
    
    def __len__(self):
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
            raise TypeError(f"Indices must be integers or slices, not {type(index).__name__}")
    
    def __contains__(self, book):
        if not isinstance(book, Book):
            return False
        return any(existing_book == book for existing_book in self._items)
    
    def __str__(self):
        if len(self._items) == 0:
            return "Library is empty."
        result = f"Library contains {len(self._items)} book(s):\n"
        result += "-" * 60 + "\n"
        for i, book in enumerate(self._items):
            result += f"[{i}] {book}\n"
        result += "-" * 60
        return result
    
    def __repr__(self):
        return f"Library(books={repr(self._items)})"