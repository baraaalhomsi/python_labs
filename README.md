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