import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lab03'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lab03.models import PrintedBook, EBook, AudioBook
from lab05.collection import Library
from lab05.strategies import (
    by_title,
    by_price,
    by_author,
    by_price_then_title,
    by_type_then_price,
    is_available,
    is_printed_book,
    is_ebook,
    is_audio_book,
    make_price_filter,
    make_price_range_filter,
    make_discount_func,
    DiscountStrategy,
    PriceIncreaseStrategy,
    ProcessStrategy,
    ActivateStrategy,
    BorrowStrategy,
    ReturnStrategy
)

def print_section(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def create_sample_library():
    lib = Library()
    lib.add(PrintedBook("War and Peace", "Leo Tolstoy", 45.0, 1225, "978-5-389-12345-6", "Azbuka", "Hardcover"))
    lib.add(PrintedBook("The Master and Margarita", "Mikhail Bulgakov", 38.0, 480, "978-5-389-23456-7", "AST", "Paperback"))
    lib.add(PrintedBook("Crime and Punishment", "Fyodor Dostoevsky", 30.0, 671, "978-5-389-34567-8", "Eksmo", "Hardcover"))
    lib.add(EBook("Python for Everybody", "Charles Severance", 25.0, 350, 5.2, "PDF", "https://example.com/python.pdf"))
    lib.add(EBook("Algorithms", "Robert Sedgewick", 55.0, 900, 12.0, "EPUB", "https://example.com/algo.epub"))
    lib.add(EBook("Clean Code", "Robert Martin", 42.0, 464, 3.5, "PDF", "https://example.com/clean.pdf"))
    lib.add(AudioBook("Harry Potter", "J.K. Rowling", 35.0, 500, 12.5, "Alexander Klyukvin", 192))
    lib.add(AudioBook("Sherlock Holmes", "Arthur Conan Doyle", 28.0, 400, 9.0, "Vasily Livanov", 128))
    lib._items[2].borrow()
    return lib

def scenario_1():
    print_section("SCENARIO 1: Method chaining filter -> sort -> apply")
    lib = create_sample_library()
    print("\nInitial library:")
    print(lib)
    lib.filter_by(is_available)
    print("\nStep 1: filter_by(is_available)")
    print(lib)
    lib.sort_by(by_price_then_title)
    print("\nStep 2: sort_by(by_price_then_title)")
    print(lib)
    lib.apply(make_discount_func(15))
    print("\nStep 3: apply(15% discount)")
    print(lib)

def scenario_2():
    print_section("SCENARIO 2: Strategy substitution without changing collection code")
    print("\n--- Sorting with different strategies ---")
    lib1 = create_sample_library()
    lib1.sort_by(by_title)
    print("\nsort_by(by_title):")
    print(lib1)
    lib1.sort_by(by_price)
    print("\nsort_by(by_price):")
    print(lib1)
    lib1.sort_by(by_type_then_price)
    print("\nsort_by(by_type_then_price):")
    print(lib1)
    print("\n--- Filtering with different strategies ---")
    lib2 = create_sample_library()
    lib2.filter_by(is_printed_book)
    print("\nfilter_by(is_printed_book):")
    print(lib2)
    lib3 = create_sample_library()
    lib3.filter_by(is_ebook)
    print("\nfilter_by(is_ebook):")
    print(lib3)
    lib4 = create_sample_library()
    lib4.filter_by(is_audio_book)
    print("\nfilter_by(is_audio_book):")
    print(lib4)
    lib5 = create_sample_library()
    lib5.filter_by(make_price_filter(35))
    print("\nfilter_by(make_price_filter(35)):")
    print(lib5)
    lib6 = create_sample_library()
    lib6.filter_by(make_price_range_filter(30, 50))
    print("\nfilter_by(make_price_range_filter(30, 50)):")
    print(lib6)

def scenario_3():
    print_section("SCENARIO 3: Callable objects as strategies")
    lib1 = create_sample_library()
    lib1.apply(DiscountStrategy(20))
    print("\napply(DiscountStrategy(20)):")
    print(lib1)
    lib2 = create_sample_library()
    lib2.apply(PriceIncreaseStrategy(10))
    print("\napply(PriceIncreaseStrategy(10)):")
    print(lib2)
    lib3 = create_sample_library()
    lib3.apply(ProcessStrategy())
    print("\napply(ProcessStrategy()):")
    print(lib3)
    lib4 = create_sample_library()
    lib4.apply(ActivateStrategy(False))
    print("\napply(ActivateStrategy(False)):")
    print(lib4)
    lib4.apply(ActivateStrategy(True))
    print("\napply(ActivateStrategy(True)):")
    print(lib4)
    lib5 = create_sample_library()
    lib5.apply(BorrowStrategy())
    print("\napply(BorrowStrategy()):")
    print(lib5)
    print("\n--- Comparison: callable object vs lambda ---")
    lib6 = create_sample_library()
    lib7 = create_sample_library()
    lib6.apply(DiscountStrategy(10))
    print("\nUsing DiscountStrategy(10):")
    print(lib6)
    lib7.apply(lambda b: (b.apply_discount(10) if b.is_available else None) or b)
    print("\nUsing lambda:")
    print(lib7)

def demo_map_and_lambda():
    print_section("ADDITIONAL: map() and lambda")
    lib = create_sample_library()
    books = lib.get_all()
    titles = list(map(lambda b: b.title, books))
    print("\nTitles via map():")
    for i, title in enumerate(titles):
        print(f"  {i+1}. {title}")
    prices_with_tax = list(map(lambda b: (b.title, b.calculate_price_with_tax()), books))
    print("\nPrices with tax via map():")
    for title, price in prices_with_tax:
        print(f"  '{title}': ${price:.2f}")
    types_list = list(map(lambda b: b.get_format_type(), books))
    print("\nBook types via map():")
    for i, t in enumerate(types_list):
        print(f"  {i+1}. {t}")
    print("\n--- Comparison: lambda vs named function ---")
    lib_lambda = create_sample_library()
    lib_named = create_sample_library()
    lib_lambda.sort_by(lambda b: b.author.lower())
    print("\nsort_by(lambda):")
    print(lib_lambda)
    lib_named.sort_by(by_author)
    print("\nsort_by(by_author):")
    print(lib_named)
    print("\nResult is identical.")
    lib_factory = create_sample_library()
    books_all = lib_factory.get_all()
    cheap_books = list(filter(make_price_filter(35), books_all))
    print(f"\nBooks cheaper than $35 (factory + filter):")
    for b in cheap_books:
        print(f"  '{b.title}' - ${b.price:.2f}")

def main():
    print("\n" + "*" * 70)
    print("  LABORATORY WORK #5")
    print("  Functions as arguments. Strategies and delegates.")
    print("*" * 70)
    scenario_1()
    scenario_2()
    scenario_3()
    demo_map_and_lambda()
    print("\n" + "*" * 70)
    print("  ALL SCENARIOS COMPLETED SUCCESSFULLY!")
    print("*" * 70 + "\n")

if __name__ == "__main__":
    main()