# Paython_Labs

## lab01: class Book (Вариант 2, Задача на 5)

## Objective
- Learn how to declare user-defined classes in Python
- Understand encapsulation using private fields
- Implement properties using @property
- Override magic methods (str, repr, eq)
- Understand the difference between class attributes and instance attributes

### Main Idea
Create a book class that:

✓ Monitors data correctness (validation)

✓ Prevents invalid operations (cannot apply discount to unavailable book, cannot borrow unavailable book)

✓ Provides a user-friendly interface through properties (@property)

✓ Tracks book state (available/unavailable)

---

## Implemented Class

### Book
```python
class Book:
    # Class Attributes
    total_books = 0
```
The main class representing a book in a library. Contains all the logic for handling books.

### Class Attributes:
- total_books — counter for tracking total number of books created

### Private Fields (Instance Attributes):
- _title - book title
- _author - book author
- _price - book price
- _pages - number of pages
- _is_available — availability status (available/unavailable)

### Properties:

| Property | Getter | Setter | Description |
|----------|--------|--------|-------------|
| title | ✅ | ❌ | Book title (read-only) |
| author | ✅ | ❌ | Book author (read-only) |
| price | ✅ | ✅ | Book price (read/write with validation) |
| pages | ✅ | ❌ | Number of pages (read-only) |
| is_available | ✅ | ✅ | Availability status (read/write) |

### Magic Methods:
- __str__ — for print function (user-friendly description)
- __repr__ — for developers (detailed object representaeq
- __eq__ — for comparing books based on title and author

### Business Methods:
- apply_discount(discount_percent) - apply discount to book price
- get_shipping_weight() - calculate book shipping weight
- borrow() - borrow the book (changes status to unavailable)
- return_book() - return the book (changes status to available)

---

## Demonstration

### 1. CREATING BOOKS
![alt text](/images/lab01/Screenshot%202026-03-14%20180702.png)

Shows that each book is created correctly, and the total_books counter increases with each new book.

### 2. MAGIC METHODS DEMONSTRATION

--- __str__ method (for users) ---

![alt text](/images/lab01/Screenshot%202026-03-14%20181119.png)

--- __repr__ method (for developers) ---

![alt text](/images/lab01/Screenshot%202026-03-14%20180712.png)

--- __eq__ method (book comparison) ---

![alt](/images/lab01/Screenshot%202026-03-14%20180733.png)

### 3. Accessing properties

![alt](/images/lab01/Screenshot%202026-03-14%20180746.png)

### 4. Modifying price using setter

the new price of book1 is 29.99$

![a](/images/lab01/Screenshot%202026-03-14%20180814.png)

### 5. Class attribute (total_books)

![a](/images/lab01/Screenshot%202026-03-14%20180828.png)

### 6. Object state management

![a](/images/lab01/Screenshot%202026-03-14%20180857.png)

### 7. Business methods

![a](/images/lab01/Screenshot%202026-03-14%20181011.png)

### 8. Error handling during object creation

![a](/images/lab01/Screenshot%202026-03-14%20181025.png)

## lab02: class Library (Вариант 2, Задача на 5)

## Objective
- Learn to work with collections of objects
- Understand the difference between entity model and object container
- Implement a custom container class
- Master iteration over objects
- Implement basic collection management operations
- Implement indexing, sorting, and filtering operations

### Main Idea
Create a container class `Library` that manages a collection of `Book` objects (from lab01).

✓ Stores objects in an internal list

✓ Manages adding and removing objects

✓ Provides access to objects

✓ Allows iteration over the collection

✓ Supports indexing, searching, sorting, and filtering

---

## Implemented Class

### Library

```python
class Library:
    """
    Container class for managing Book objects.
    Supports adding, removing, searching, sorting, filtering, and indexing.
    """
```

The main container class representing a library that holds multiple books. Provides complete collection management functionality.

### Private Fields (Instance Attributes):
- `_items` - internal list storing Book objects

### Core Methods:

| Method | Description |
|--------|-------------|
| `add(book)` | Add a book to the library (with type checking and duplicate prevention) |
| `remove(book)` | Remove a book from the library |
| `remove_at(index)` | Remove a book at specific index |
| `get_all()` | Return a copy of all books in the library |

### Search Methods:

| Method | Description |
|--------|-------------|
| `find_by_title(title)` | Search for books by title (case-insensitive partial match) |
| `find_by_author(author)` | Search for books by author (case-insensitive partial match) |
| `find_by_price_range(min, max)` | Find books within price range |

### Magic Methods:

| Method | Description |
|--------|-------------|
| `__len__()` | Returns the number of books (supports `len(library)`) |
| `__iter__()` | Makes the library iterable (supports `for book in library`) |
| `__getitem__(index)` | Supports indexing and slicing (`library[0]`, `library[1:3]`) |
| `__contains__(item)` | Supports `in` operator (`book in library`) |
| `__str__()` | User-friendly string representation |
| `__repr__()` | Developer-friendly representation |

### Sorting Methods:

| Method | Description |
|--------|-------------|
| `sort_by_title(reverse)` | Sort books alphabetically by title |
| `sort_by_author(reverse)` | Sort books alphabetically by author |
| `sort_by_price(reverse)` | Sort books by price |
| `sort_by_pages(reverse)` | Sort books by number of pages |
| `sort(key, reverse)` | Generic sort with custom key function |

### Filtering Methods (Logical Operations):

| Method | Description |
|--------|-------------|
| `get_available()` | Return new library with only available books |
| `get_unavailable()` | Return new library with only borrowed books |
| `get_expensive(threshold)` | Return new library with books above price threshold |

---

## Demonstration

### SCENARIO 1: Basic Operations

**Creating books and adding to library:**

![alt text](/images/lab02/Screenshot%202026-04-03%20150855.png)

Shows:
- Creating multiple Book objects
- Adding books to Library collection
- Displaying all books in the library
- Removing a book from the library
- Type checking (cannot add non-Book objects)
- Duplicate prevention (cannot add same book twice)

### SCENARIO 2: Search, Iteration & Indexing

**Iteration and indexing:**

![alt text](/images/lab02/Screenshot%202026-04-03%20151242.png)
![alt text](/images/lab02/Screenshot%202026-04-03%20151306.png)

**Search functionality:**

![alt text](/images/lab02/Screenshot%202026-04-03%20151126.png)

Shows:
- `find_by_title()` - partial match, case-insensitive search
- `find_by_author()` - search by author name
- `find_by_price_range()` - filter by price range
- `for book in library` - iteration using `__iter__`
- `len(library)` - collection size using `__len__`
- `library[0]`, `library[-1]` - indexing using `__getitem__`
- `library[0:2]` - slicing support
- `book in library` - membership test using `__contains__`

### SCENARIO 3: Sort


ing & Filtering

**Sorting by different criteria:**

![alt text](/images/lab02/Screenshot%202026-04-03%20151831.png)

**Filtering operations:**

![alt text](/images/lab02/Screenshot%202026-04-03%20151847.png)

Shows:
- `sort_by_title()` - alphabetical order by title
- `sort_by_price(reverse=True)` - descending order by price
- `sort_by_pages()` - ascending order by page count
- `get_available()` - returns new library with only available books
- `get_expensive(20)` - returns books priced above $20
- `remove_at(index)` - deletion by index position

### SCENARIO 4: Error Handling & Edge Cases

**Empty library handling:**

![alt text](/images/lab02/Screenshot%202026-04-03%20152036.png)

Shows:
- Empty library behavior (len = 0, empty string representation)
- Index out of range error handling
- Type validation when adding invalid objects
- Filter operations on single-element library
- Graceful handling of edge cases

---

## Requirements Traceability Matrix

![alt text](/images/lab02/Screenshot%202026-04-03%20152557.png)