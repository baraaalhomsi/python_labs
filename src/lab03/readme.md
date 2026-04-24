# Laboratory Work 3: Наследование и иерархия классов (Вариант на 5)

## Objective
- Master the mechanism of class inheritance
- Learn to build object hierarchies
- Understand the difference between base and derived classes
- Learn to reuse code using `super()`
- Master method overriding and polymorphism
- Implement a unified interface through abstract methods

---

## Implemented Class Hierarchy

### Base Class: `Book`

An abstract class representing a book in the library.

#### Class Attributes:
- `total_books` — counter of created books

#### Private Fields:
- `title` — book title
- `author` — book author
- `price` — book price
- `pages` — number of pages
- `is_available` — book availability
- `created_date` — date added

#### @property:
- Read: `title`, `author`, `price`, `pages`, `is_available`, `created_date`
- Read/Write: `price`, `is_available`

#### Abstract Methods (Interface):
- `calculate_price_with_tax()` — calculate price with tax
- `get_format_type()` — returns format type
- `process()` — process the book
- `display_info()` — display detailed information

#### Business Methods:
- `borrow()` — borrow the book
- `return_book()` — return the book
- `apply_discount(discount_percent)` — apply discount
- `get_shipping_weight()` — get shipping weight

#### Magic Methods:
- `__str__` — for print (readable description)
- `__repr__` — for developers
- `__eq__` — compare by title and author

---

### Derived Class 1: `PrintedBook`

Inherits from `Book`. Represents a physical book.

#### New Attributes:
- `isbn` — International Standard Book Number
- `publisher` — publisher name
- `cover_type` — cover type (Paperback/Hardcover)
- `times_borrowed` — borrow counter

#### New Methods:
- `borrow_with_tracking()` — borrow with statistics tracking
- `get_borrow_stats()` — get borrow statistics

#### Overridden Methods:
- `calculate_price_with_tax()` — 8% tax
- `get_format_type()` — returns "Printed Book (CoverType)"
- `process()` — inventory check
- `display_info()` — extended information
- `__str__` — format with 📖 emoji

---

### Derived Class 2: `EBook`

Inherits from `Book`. Represents a digital book.

#### New Attributes:
- `file_size_mb` — file size in megabytes
- `format_type` — format (PDF, EPUB)
- `download_link` — download link
- `times_downloaded` — download counter

#### New Methods:
- `download()` — download the book
- `get_download_stats()` — get download statistics

#### Overridden Methods:
- `calculate_price_with_tax()` — 5% tax
- `get_format_type()` — returns "E-Book (Format)"
- `process()` — format conversion
- `display_info()` — extended information
- `__str__` — format with 📱 emoji

---

### Derived Class 3: `AudioBook`

Inherits from `Book`. Represents an audio book.

#### New Attributes:
- `duration_hours` — duration in hours
- `narrator` — narrator name
- `bitrate_kbps` — bitrate in kbps
- `times_played` — play counter

#### New Methods:
- `play()` — play the book
- `get_play_stats()` — get play statistics

#### Overridden Methods:
- `calculate_price_with_tax()` — 10% tax
- `get_format_type()` — returns "AudioBook (Bitrate)"
- `process()` — audio normalization
- `display_info()` — extended information
- `__str__` — format with 🎧 emoji

---

### Filtering Functions (in `models.py`):

- `filter_ebooks(books_list)` – return only e-books
- `filter_audiobooks(books_list)` – return only audiobooks
- `filter_printed_books(books_list)` – return only printed books
- `filter_available(books_list)` – return only available books
- `filter_by_price_range(books_list, min_price, max_price)` – filter by price range

---

## Demonstration

### Scenario 1: Creating Objects of Different Types

![alt](/images/lab03/Screenshot%202026-04-09%20225709.png)

---

### Scenario 2: New Attributes and Methods (PrintedBook)

![alt](/images/lab03/Screenshot%202026-04-09%20230019.png)

---

### Scenario 3: New Attributes and Methods (EBook)

![alt](/images/lab03/Screenshot%202026-04-09%20230140.png)

---

### Scenario 4: New Attributes and Methods (AudioBook)

![alt](/images/lab03/Screenshot%202026-04-09%20230249.png)

---

### Scenario 5: Polymorphism — calculate_price_with_tax()

![alt](/images/lab03/Screenshot%202026-04-09%20230407.png)

*The same method behaves differently depending on the book type.*

---

### Scenario 6: Polymorphism — process()

![alt](/images/lab03/Screenshot%202026-04-09%20230536.png)

---

### Scenario 7: Overridden Methods __str__ and display_info()

![alt](/images/lab03/Screenshot%202026-04-09%20230806.png)

---

### Scenario 8: Type Checking with isinstance()

![alt](/images/lab03/Screenshot%202026-04-09%20230927.png)

---

### Scenario 9: Using Base Class Methods

![alt](/images/lab03/Screenshot%202026-04-09%20231223.png)

---

### Scenario 10: Applying Discount

![alt](/images/lab03/Screenshot%202026-04-09%20231433.png)

### Scenario 11 Filtering by type:

![alt](/images/lab03/Screenshot%202026-04-09%20231636.png)

---

### Scenario 12 Filtering available books:

![alt](/images/lab03/Screenshot%202026-04-09%20231651.png)

---

### Summary

A flexible and extensible class hierarchy has been developed, demonstrating all principles of object-oriented programming. The code is easily scalable — to add a new book type, simply create a new class inheriting from `Book` and implement its abstract methods.
