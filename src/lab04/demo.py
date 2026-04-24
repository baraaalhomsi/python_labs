from models import DigitalBook, Audiobook, PrintedBook
from library import Library
from interfaces import Printable, Comparable
import functools

def print_all(items: list[Printable]) -> None:
    print("\n=== Printing all printable items ===")
    for item in items:
        print(f" - {item.to_string()}")

def demonstrate_polymorphism():
    print("\n" + "=" * 60)
    print("SCENARIO 1: POLYMORPHISM THROUGH INTERFACES")
    print("=" * 60)
    
    digital = DigitalBook("Python Programming", "John Smith", 45.99, 500, 12.5, "PDF")
    audio = Audiobook("Clean Code", "Robert Martin", 35.50, 450, 12.5, "Uncle Bob")
    printed = PrintedBook("Design Patterns", "Gang of Four", 65.00, 400, 850, True)
    
    printable_items: list[Printable] = [digital, audio, printed]
    print_all(printable_items)

def demonstrate_library_filters():
    print("\n" + "=" * 60)
    print("SCENARIO 2: LIBRARY FILTERING BY INTERFACE")
    print("=" * 60)
    
    library = Library()
    
    library.add(DigitalBook("Python Programming", "John Smith", 45.99, 500, 12.5))
    library.add(Audiobook("Clean Code", "Robert Martin", 35.50, 450, 12.5, "Uncle Bob"))
    library.add(PrintedBook("Design Patterns", "Gang of Four", 65.00, 400, 850))
    library.add(DigitalBook("Machine Learning", "Andrew Ng", 55.00, 600, 8.3))
    library.add(PrintedBook("The Pragmatic Programmer", "Dave Thomas", 40.00, 350, 600, True))
    
    print(f"Total books: {len(library)}")
    
    printable_books = library.get_printable()
    print(f"\nPrintable books ({len(printable_books)}):")
    for book in printable_books:
        print(f"  - {book.to_string()}")
    
    comparable_books = library.get_comparable()
    print(f"\nComparable books ({len(comparable_books)}):")
    for book in comparable_books:
        print(f"  - {book.to_string()}")

def demonstrate_isinstance_checks():
    print("\n" + "=" * 60)
    print("SCENARIO 3: INTERFACE IMPLEMENTATION VERIFICATION")
    print("=" * 60)
    
    digital = DigitalBook("AI Basics", "Jane Doe", 30.00, 300, 5.2)
    audio = Audiobook("The Hobbit", "J.R.R. Tolkien", 25.00, 350, 10.0, "Andy Serkis")
    printed = PrintedBook("1984", "George Orwell", 15.00, 328, 400)
    
    print(f"DigitalBook implements Printable: {isinstance(digital, Printable)}")
    print(f"DigitalBook implements Comparable: {isinstance(digital, Comparable)}")
    print(f"DigitalBook category: {digital.get_category()}")
    
    print(f"\nAudiobook implements Printable: {isinstance(audio, Printable)}")
    print(f"Audiobook implements Comparable: {isinstance(audio, Comparable)}")
    print(f"Audiobook category: {audio.get_category()}")
    
    print(f"\nPrintedBook implements Printable: {isinstance(printed, Printable)}")
    print(f"PrintedBook implements Comparable: {isinstance(printed, Comparable)}")
    print(f"PrintedBook category: {printed.get_category()}")

def demonstrate_sorting():
    print("\n" + "=" * 60)
    print("SCENARIO 4: SORTING USING COMPARABLE INTERFACE")
    print("=" * 60)
    
    books = [
        DigitalBook("Python", "Smith", 45.99, 500, 12.5),
        DigitalBook("Java", "Johnson", 35.99, 400, 10.0),
        DigitalBook("C++", "Williams", 55.99, 600, 15.0),
    ]
    
    print("\nDigitalBooks before sorting:")
    for book in books:
        print(f"  - {book.to_string()}")
    
    def compare_books(a, b):
        return a.compare_to(b)
    
    books_sorted = sorted(books, key=functools.cmp_to_key(compare_books))
    
    print("\nDigitalBooks after sorting by price (using compare_to):")
    for book in books_sorted:
        print(f"  - {book.to_string()}")

def demonstrate_library_sorting():
    print("\n" + "=" * 60)
    print("SCENARIO 5: LIBRARY SORTING")
    print("=" * 60)
    
    library = Library()
    library.add(DigitalBook("Zebra Programming", "Adams", 50.00, 500, 12.5))
    library.add(DigitalBook("Apple Programming", "Baker", 30.00, 400, 10.0))
    library.add(DigitalBook("Python Programming", "ChLoading...book.toarlie", 40.00, 600, 15.0))
    
    print("\nBooks before sorting:")
    for book in library.get_all():
        print(f"  - {book.to_string()}")
    
    library.sort_by_price()
    print("\nBooks after sorting by price:")
    for book in library.get_all():
        print(f"  - {book.to_string()}")

def main():
    
    demonstrate_polymorphism()
    demonstrate_library_filters()
    demonstrate_isinstance_checks()
    demonstrate_sorting()
    demonstrate_library_sorting()

if __name__ == "__main__":
    main()