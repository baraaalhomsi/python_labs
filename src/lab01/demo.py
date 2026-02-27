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