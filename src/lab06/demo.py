import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib', 'lab03'))

from container import TypedCollection, Displayable, Scorable, D, S
from models import PrintedBook, EBook, AudioBook
def demo_basic():
    print("=" * 60)
    print("SCENARIO 0: Basic TypedCollection with Student-like objects")
    print("=" * 60)
    
    class Student:
        def __init__(self, name: str, gpa: float, year: int) -> None:
            self._name: str = name
            self._gpa: float = gpa
            self._year: int = year
        
        def get_name(self) -> str:
            return self._name
        
        def get_gpa(self) -> float:
            return self._gpa
        
        def __str__(self) -> str:
            return f"Student: {self._name} | GPA: {self._gpa} | Year: {self._year}"
    
    students = TypedCollection[Student]()
    students.add(Student("Alice", 3.8, 2))
    students.add(Student("Bob", 3.5, 3))
    students.add(Student("Charlie", 3.9, 1))
    
    print("All students:")
    for s in students.get_all():
        print(f"  {s}")
    
    print("\nfind() - looking for GPA > 3.7:")
    found = students.find(lambda s: s.get_gpa() > 3.7)
    print(f"  Found: {found}")
    
    print("\nfind() - looking for GPA > 4.0 (returns None):")
    not_found = students.find(lambda s: s.get_gpa() > 4.0)
    print(f"  Found: {not_found}")
    
    print("\nfilter() - GPA >= 3.8:")
    filtered = students.filter(lambda s: s.get_gpa() >= 3.8)
    for s in filtered:
        print(f"  {s}")
    
    print("\nmap() - get names (list[str]):")
    names = students.map(lambda s: s.get_name())
    print(f"  {names} -> type: {type(names[0]) if names else 'empty'}")
    
    print("\nmap() - get GPAs (list[float]):")
    gpas = students.map(lambda s: s.get_gpa())
    print(f"  {gpas} -> type: {type(gpas[0]) if gpas else 'empty'}")
    
    print()

def demo_displayable():
    print("=" * 60)
    print("SCENARIO 1: TypedCollection[D] with Displayable Protocol")
    print("=" * 60)
    
    books: TypedCollection[D] = TypedCollection()
    
    pb = PrintedBook(
        title="The Art of Programming",
        author="Donald Knuth",
        price=59.99,
        pages=700,
        isbn="978-0-201-03801-9",
        publisher="Addison-Wesley",
        cover_type="Hardcover"
    )
    
    eb = EBook(
        title="Clean Code",
        author="Robert Martin",
        price=39.99,
        pages=464,
        file_size_mb=4.5,
        format_type="EPUB"
    )
    
    ab = AudioBook(
        title="Atomic Habits",
        author="James Clear",
        price=29.99,
        pages=320,
        duration_hours=5.5,
        narrator="James Clear",
        bitrate_kbps=192
    )
    
    books.add(pb)
    books.add(eb)
    books.add(ab)
    
    print("All items in collection (using display_info):")
    print("-" * 50)
    for item in books.get_all():
        print(item.display_info())
        print()
    
    print("find() - book with 'Clean' in title:")
    found = books.find(lambda b: "Clean" in b.display_info())
    if found:
        print(f"  Found: {found.display_info()}")
    else:
        print("  Not found")
    
    print("\nfilter() - books with price > 30:")
    filtered = books.filter(lambda b: b.price > 30)
    for b in filtered:
        print(f"  {b.display_info()}")
    
    print("\nmap() - get format types:")
    formats = books.map(lambda b: b.get_format_type())
    for f in formats:
        print(f"  {f}")
    
    print()

def demo_scorable():
    print("=" * 60)
    print("SCENARIO 2: TypedCollection[S] with Scorable Protocol")
    print("=" * 60)
    
    items: TypedCollection[S] = TypedCollection()
    
    pb = PrintedBook(
        title="Design Patterns",
        author="Gang of Four",
        price=54.99,
        pages=395,
        isbn="978-0-201-63361-0",
        publisher="Addison-Wesley",
        cover_type="Paperback"
    )
    
    eb = EBook(
        title="The Pragmatic Programmer",
        author="David Thomas",
        price=49.99,
        pages=352,
        file_size_mb=3.2,
        format_type="PDF"
    )
    
    ab = AudioBook(
        title="Deep Work",
        author="Cal Newport",
        price=24.99,
        pages=296,
        duration_hours=7.8,
        narrator="Jeff Bottoms",
        bitrate_kbps=160
    )
    
    items.add(pb)
    items.add(eb)
    items.add(ab)
    
    print("All items with scores (price with tax):")
    print("-" * 50)
    for item in items.get_all():
        print(f"  {item.title}: ${item.price:.2f} -> with tax: ${item.calculate_price_with_tax():.2f}")
    
    print("\nfind() - item with taxed price > 60:")
    found = items.find(lambda s: s.calculate_price_with_tax() > 60)
    if found:
        print(f"  Found: {found.title} - Taxed price: ${found.calculate_price_with_tax():.2f}")
    else:
        print("  Not found")
    
    print("\nfilter() - taxed price >= 30:")
    filtered = items.filter(lambda s: s.calculate_price_with_tax() >= 30)
    for item in filtered:
        print(f"  {item.title}: ${item.calculate_price_with_tax():.2f}")
    
    print("\nmap() - get taxed prices:")
    taxed = items.map(lambda s: s.calculate_price_with_tax())
    for t in taxed:
        print(f"  ${t:.2f}")
    
    print("\nmap() - get titles:")
    titles = items.map(lambda s: s.title)
    print(f"  {titles}")
    
    print()

if __name__ == "__main__":
    demo_basic()
    demo_displayable()
    demo_scorable()