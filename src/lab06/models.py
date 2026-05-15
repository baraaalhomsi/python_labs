from base import Book
from validators import validate_file_size, validate_duration, validate_isbn

class PrintedBook(Book):
    
    def __init__(self, title: str, author: str, price: float, pages: int,
                 isbn: str, publisher: str, cover_type: str = "Paperback"):
        super().__init__(title, author, price, pages)
        self._isbn = validate_isbn(isbn)
        self._publisher = publisher
        self._cover_type = cover_type
        self._times_borrowed = 0
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def publisher(self):
        return self._publisher
    
    @property
    def cover_type(self):
        return self._cover_type
    
    @property
    def times_borrowed(self):
        return self._times_borrowed
    
    def borrow_with_tracking(self) -> str:
        self._times_borrowed += 1
        self.borrow()
        return f"Borrowing '{self.title}' (ISBN: {self._isbn}) - Total borrows: {self._times_borrowed}"
    
    def get_borrow_stats(self) -> str:
        return f"'{self.title}' has been borrowed {self._times_borrowed} times"
    
    def calculate_price_with_tax(self) -> float:
        tax_rate = 0.08
        return round(self.price * (1 + tax_rate), 2)
    
    def get_format_type(self) -> str:
        return f"Printed Book ({self._cover_type})"
    
    def process(self) -> str:
        return f"Processing Printed Book '{self.title}': Checking inventory, updating stock..."
    
    def display_info(self) -> str:
        base_info = super().__str__()
        return f"{base_info}\n   Printed Book | ISBN: {self._isbn} | Publisher: {self._publisher} | Cover: {self._cover_type} | Borrows: {self._times_borrowed}"
    
    def __str__(self):
        return f" Printed: '{self.title}' | {self.author} | ${self.price:.2f} | {self._cover_type} | ISBN: {self._isbn}"

class EBook(Book):
    
    def __init__(self, title: str, author: str, price: float, pages: int, 
                 file_size_mb: float, format_type: str = "PDF", 
                 download_link: str = ""):
        super().__init__(title, author, price, pages)
        self._file_size_mb = validate_file_size(file_size_mb)
        self._format_type = format_type
        self._download_link = download_link
        self._times_downloaded = 0
    
    @property
    def file_size_mb(self):
        return self._file_size_mb
    
    @property
    def format_type(self):
        return self._format_type
    
    @property
    def times_downloaded(self):
        return self._times_downloaded
    
    def download(self) -> str:
        self._times_downloaded += 1
        return f"Downloading '{self.title}' ({self._file_size_mb} MB)..."
    
    def get_download_stats(self) -> str:
        return f"'{self.title}' has been downloaded {self._times_downloaded} times"
    
    def calculate_price_with_tax(self) -> float:
        tax_rate = 0.05
        return round(self.price * (1 + tax_rate), 2)
    
    def get_format_type(self) -> str:
        return f"E-Book ({self._format_type})"
    
    def process(self) -> str:
        return f"Processing E-Book '{self.title}': Converting formats, optimizing for devices..."
    
    def display_info(self) -> str:
        base_info = super().__str__()
        return f"{base_info}\n   E-Book | Format: {self._format_type} | Size: {self._file_size_mb}MB | Downloads: {self._times_downloaded}"
    
    def __str__(self):
        return f" E-Book: '{self.title}' | {self.author} | ${self.price:.2f} | {self._format_type} | {self._file_size_mb}MB"

class AudioBook(Book):
    
    def __init__(self, title: str, author: str, price: float, pages: int,
                 duration_hours: float, narrator: str, bitrate_kbps: int = 128):
        super().__init__(title, author, price, pages)
        self._duration_hours = validate_duration(duration_hours)
        self._narrator = narrator
        self._bitrate_kbps = bitrate_kbps
        self._times_played = 0
    
    @property
    def duration_hours(self):
        return self._duration_hours
    
    @property
    def narrator(self):
        return self._narrator
    
    @property
    def times_played(self):
        return self._times_played
    
    def play(self) -> str:
        self._times_played += 1
        hours = int(self._duration_hours)
        minutes = int((self._duration_hours % 1) * 60)
        return f" Playing '{self.title}' narrated by {self._narrator} (Duration: {hours}h {minutes}m, {self._bitrate_kbps}kbps)..."
    
    def get_play_stats(self) -> str:
        return f"'{self.title}' has been played {self._times_played} times"
    
    def calculate_price_with_tax(self) -> float:
        tax_rate = 0.10
        return round(self.price * (1 + tax_rate), 2)
    
    def get_format_type(self) -> str:
        return f"AudioBook ({self._bitrate_kbps}kbps)"
    
    def process(self) -> str:
        return f"Processing AudioBook '{self.title}': Normalizing audio, generating chapters..."
    
    def display_info(self) -> str:
        base_info = super().__str__()
        hours = int(self._duration_hours)
        minutes = int((self._duration_hours % 1) * 60)
        return f"{base_info}\n  🎧 AudioBook | Narrator: {self._narrator} | Duration: {hours}h {minutes}m | Bitrate: {self._bitrate_kbps}kbps | Plays: {self._times_played}"
    
    def __str__(self):
        hours = int(self._duration_hours)
        minutes = int((self._duration_hours % 1) * 60)
        return f"🎧 AudioBook: '{self.title}' | {self.author} | ${self.price:.2f} | Narrated by {self._narrator} | {hours}h {minutes}m"

# ========== Filtering Functions ==========

def filter_ebooks(books_list):
    """Filter - return only EBook objects"""
    return [book for book in books_list if isinstance(book, EBook)]

def filter_audiobooks(books_list):
    """Filter - return only AudioBook objects"""
    return [book for book in books_list if isinstance(book, AudioBook)]

def filter_printed_books(books_list):
    """Filter - return only PrintedBook objects"""
    return [book for book in books_list if isinstance(book, PrintedBook)]

def filter_available(books_list):
    """Filter - return only available books"""
    return [book for book in books_list if book.is_available]

def filter_by_price_range(books_list, min_price, max_price):
    """Filter - return books within price range"""
    return [book for book in books_list if min_price <= book.price <= max_price]