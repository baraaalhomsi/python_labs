from model import Book
from collection import Library

def print_separator(title: str = ""):
    if title:
        print("\n", title)

def scenario_1_basic_operations():
    print_separator("SCENARIO 1: Basic Operations")
    
    library = Library()
    print("\n[1.1] Creating books:")
    book1 = Book("Clean Code", "Robert Martin", 45.99, 464)
    book2 = Book("The Pragmatic Programmer", "David Thomas", 42.50, 352)
    book3 = Book("Design Patterns", "Erich Gamma", 55.00, 395)
    book4 = Book("Introduction to Algorithms", "Thomas Cormen", 85.00, 1312)
    
    print(f"  Created: {book1}")
    print(f"  Created: {book2}")
    print(f"  Created: {book3}")
    print(f"  Created: {book4}")
    
    print("\n[1.2] Adding books to library:")
    library.add(book1)
    library.add(book2)
    library.add(book3)
    library.add(book4)
    print(f"  Library size: {len(library)} books")
    
    print("\n[1.3] Display all books:")
    print(library)
    
    print("\n[1.4] Removing a book:")
    library.remove(book2)
    print(f"  Removed '{book2.title}'")
    print(f"  Library size after removal: {len(library)}")
    print("\n  Books remaining:")
    for book in library:
        print(f"    • {book.title}")
    
    print("\n[1.5] Trying to add duplicate book:")
    try:
        library.add(book1)  # Already exists
        print("  This should not print!")
    except ValueError as e:
        print(f"   Error caught: {e}")
    
    print("\n[1.6] Trying to add invalid object:")
    try:
        library.add("Not a book")  # type: ignore
        print("  This should not print!")
    except TypeError as e:
        print(f"   Error caught: {e}")
    
    return library  # Return the library for use in other scenarios

def scenario_2_search_and_iteration():
    """Scenario 2: Search, iteration, len(), and indexing."""
    print_separator("SCENARIO 2: Search, Iteration & Indexing")
    
    library = Library()
    
    # Add test books
    books = [
        Book("Python Crash Course", "Eric Matthes", 39.99, 544),
        Book("Automate the Boring Stuff", "Al Sweigart", 29.99, 592),
        Book("Fluent Python", "Luciano Ramalho", 59.99, 792),
        Book("Python Cookbook", "David Beazley", 54.99, 706),
        Book("Learning Python", "Mark Lutz", 64.99, 1600),
    ]
    
    for book in books:
        library.add(book)
    
    print(f"\n[2.1] Library contains {len(library)} books")
    
    print("\n[2.2] Using for loop to iterate:")
    for i, book in enumerate(library):
        print(f"  {i}: {book.title} by {book.author}")
    
    print("\n[2.3] Searching by title (case-insensitive partial match):")
    results = library.find_by_title("python")
    print(f"  Found {len(results)} book(s):")
    for book in results:
        print(f"    • {book.title}")
    
    print("\n[2.4] Searching by author:")
    results = library.find_by_author("lutz")
    for book in results:
        print(f"    • '{book.title}' by {book.author}")
    
    print("\n[2.5] Searching by price range ($40 - $60):")
    results = library.find_by_price_range(40, 60)
    for book in results:
        print(f"    • {book.title} - ${book.price}")
    
    print("\n[2.6] Using indexing (__getitem__):")
    # Make sure library has elements before accessing
    if len(library) > 0:
        print(f"  First book: {library[0].title}")
        print(f"  Last book: {library[4].title}")
        print(f"  Middle book: {library[2].title}")
    else:
        print("  Library is empty!")
    
    print("\n[2.7] Using slicing:")
    if len(library) >= 2:
        first_two = library[0:2]
        print(f"  First two books ({len(first_two)}):")
        for book in first_two:
            print(f"    • {book.title}")
    else:
        print("  Not enough books for slicing")
    
    print("\n[2.8] Using 'in' operator:")
    if len(books) > 0:
        check_book = books[0]
        print(f"  Is '{check_book.title}' in library? {check_book in library}")
    print(f"  Is 'Fake Book' in library? {'Fake Book' in library}")

def scenario_3_sorting_and_filtering():
    """Scenario 3: Sorting and logical operations."""
    print_separator("SCENARIO 3: Sorting & Filtering")
    
    library = Library()
    
    # Add books with various prices and availability
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 15.99, 310)
    book2 = Book("1984", "George Orwell", 12.99, 328)
    book3 = Book("Dune", "Frank Herbert", 18.99, 412)
    book4 = Book("Foundation", "Isaac Asimov", 14.99, 244)
    book5 = Book("The Martian", "Andy Weir", 22.99, 369)
    book6 = Book("Project Hail Mary", "Andy Weir", 28.99, 496)
    
    library.add(book1)
    library.add(book2)
    library.add(book3)
    library.add(book4)
    library.add(book5)
    library.add(book6)
    
    # Borrow some books
    book2.borrow()
    book4.borrow()
    
    print("\n[3.1] Original order:")
    for book in library:
        print(f"  {book.title} - ${book.price}")
    
    print("\n[3.2] Sort by title:")
    library.sort_by_title()
    for book in library:
        print(f"  {book.title}")
    
    print("\n[3.3] Sort by price (descending):")
    library.sort_by_price(reverse=True)
    for book in library:
        print(f"  {book.title} - ${book.price}")
    
    print("\n[3.4] Sort by pages:")
    library.sort_by_pages()
    for book in library:
        print(f"  {book.title} - {book.pages} pages")
    
    print("\n[3.5] Get available books (filtering):")
    available_library = library.get_available()
    print(f"  Total books: {len(library)}")
    print(f"  Available: {len(available_library)}")
    for book in available_library:
        status = "Available" if book.is_available else "Borrowed"
        print(f"    • {book.title} - {status}")
    
    print("\n[3.6] Get expensive books (> $20):")
    expensive_library = library.get_expensive(20)
    print(f"  Found {len(expensive_library)} expensive book(s):")
    for book in expensive_library:
        print(f"    • {book.title} - ${book.price}")
    
    print("\n[3.7] Remove by index (remove_at):")
    print(f"  Before: {len(library)} books")
    if len(library) > 0:
        removed = library.remove_at(0)
        print(f"  Removed: '{removed.title}'")
        print(f"  After: {len(library)} books")
    else:
        print("  Library is empty, cannot remove")

def scenario_4_edge_cases_and_error_handling():
    """Scenario 4: Edge cases and error handling."""
    print_separator("SCENARIO 4: Error Handling & Edge Cases")
    
    library = Library()
    
    print("\n[4.1] Empty library behavior:")
    print(f"  len(library): {len(library)}")
    print(f"  str(library): {library}")
    print(f"  List from get_all(): {library.get_all()}")
    
    print("\n[4.2] Trying to access out-of-range index:")
    try:
        book = library[0]
        print("  This should not print!")
    except IndexError as e:
        print(f"   Error caught: {e}")
    
    print("\n[4.3] Trying to remove from empty library:")
    try:
        dummy_book = Book("Fake", "Fake", 10, 100)
        result = library.remove(dummy_book)
        print(f"  Removing non-existent book returns: {result}")
    except Exception as e:
        print(f"  This shouldn't raise exception: {e}")
    
    print("\n[4.4] Creating valid book:")
    book = Book("Valid Book", "Valid Author", 20.00, 200)
    library.add(book)
    print(f"  Added: {book.title}")
    
    print("\n[4.5] Trying to add invalid types:")
    try:
        library.add(None)  # type: ignore
        print("  This should not print!")
    except TypeError as e:
        print(f"   None: {e}")
    
    try:
        library.add(123)  # type: ignore
        print("  This should not print!")
    except TypeError as e:
        print(f"   Integer: {e}")
    
    print("\n[4.6] Filter operations on single-element library:")
    available = library.get_available()
    print(f"  Available books: {len(available)}")
    
    expensive = library.get_expensive(10)
    print(f"  Expensive books (> $10): {len(expensive)}")

def main():

    scenario_1_basic_operations()
    scenario_2_search_and_iteration()
    scenario_3_sorting_and_filtering()
    scenario_4_edge_cases_and_error_handling()
    
    print_separator("ALL SCENARIOS COMPLETED SUCCESSFULLY")
    print("\n All requirements for Grade 5 have been demonstrated:\n")
    print("  • Basic operations (add, remove, get_all)")
    print("  • Type checking and duplicate prevention")
    print("  • Search methods (find_by_*)")
    print("  • __len__() and __iter__()")
    print("  • __getitem__() (indexing and slicing)")
    print("  • remove_at() (delete by index)")
    print("  • Sorting (multiple methods)")
    print("  • Filtering (logical operations)")
    print("  • Error handling for edge cases")
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()