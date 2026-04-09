from base import Book
from models import PrintedBook, EBook, AudioBook
from models import filter_ebooks, filter_audiobooks, filter_printed_books, filter_available

def run_demo():
    print("=" * 70)
    print("LABORATORY WORK #3 - INHERITANCE & POLYMORPHISM".center(70))
    print("=" * 70)
    
    print("\n[1] Creating objects of different types (3 derived classes):")
    printed_book = PrintedBook(
        title="Clean Code", 
        author="Robert Martin", 
        price=45.99, 
        pages=464,
        isbn="9780132350884",
        publisher="Pearson",
        cover_type="Hardcover"
    )
    
    ebook = EBook(
        title="Python Crash Course", 
        author="Eric Matthes", 
        price=39.99, 
        pages=544, 
        file_size_mb=12.5, 
        format_type="EPUB", 
        download_link="https://store.com/book"
    )
    
    audiobook = AudioBook(
        title="The Pragmatic Programmer", 
        author="David Thomas", 
        price=42.50, 
        pages=352, 
        duration_hours=12.5, 
        narrator="John Smith", 
        bitrate_kbps=192
    )
    
    print(f"  PrintedBook: {printed_book}")
    print(f"  EBook: {ebook}")
    print(f"  AudioBook: {audiobook}")
    
    print("\n[2] New attributes and methods in PrintedBook:")
    print(f"  ISBN: {printed_book.isbn}, Publisher: {printed_book.publisher}, Cover: {printed_book.cover_type}")
    print(f"  {printed_book.borrow_with_tracking()}")
    print(f"  {printed_book.get_borrow_stats()}")
    
    print("\n[3] New attributes and methods in EBook:")
    print(f"  File size: {ebook.file_size_mb}MB, Format: {ebook.format_type}")
    print(f"  {ebook.download()}")
    print(f"  {ebook.get_download_stats()}")
    
    print("\n[4] New attributes and methods in AudioBook:")
    print(f"  Duration: {audiobook.duration_hours}h, Narrator: {audiobook.narrator}")
    print(f"  {audiobook.play()}")
    print(f"  {audiobook.get_play_stats()}")
    
    print("\n[5] Polymorphism - calculate_price_with_tax():")
    books = [printed_book, ebook, audiobook]
    for book in books:
        print(f"  {book.get_format_type()}: ${book.price:.2f} → ${book.calculate_price_with_tax():.2f}")
    
    print("\n[6] Polymorphism - process():")
    for book in books:
        print(f"  {book.process()}")
    
    print("\n[7] Overridden __str__() and display_info():")
    for book in books:
        print(f"\n  {book.display_info()}")
    
    print("\n[8] Type checking with isinstance():")
    print(f"  isinstance(printed_book, Book): {isinstance(printed_book, Book)}")
    print(f"  isinstance(printed_book, PrintedBook): {isinstance(printed_book, PrintedBook)}")
    print(f"  isinstance(printed_book, EBook): {isinstance(printed_book, EBook)}")
    print(f"  isinstance(ebook, EBook): {isinstance(ebook, EBook)}")
    print(f"  isinstance(audiobook, AudioBook): {isinstance(audiobook, AudioBook)}")
    
    print("\n[9] Using base class methods:")
    print(f"  Before borrow: {printed_book.is_available}")
    printed_book.return_book()
    print(f"  After return: {printed_book.is_available}")
    
    print("\n[10] Apply discount:")
    print(f"  Original price: ${ebook.price}")
    ebook.apply_discount(15)
    print(f"  After 15% discount: ${ebook.price}")

    print("\n[11] Filtering by type:")
    all_books = [printed_book, ebook, audiobook]

    ebooks = filter_ebooks(all_books)
    audiobooks = filter_audiobooks(all_books)
    printed_books = filter_printed_books(all_books)

    print(f"  EBooks ({len(ebooks)}): {[b.title for b in ebooks]}")
    print(f"  AudioBooks ({len(audiobooks)}): {[b.title for b in audiobooks]}")
    print(f"  PrintedBooks ({len(printed_books)}): {[b.title for b in printed_books]}")

    print("\n[12] Filtering available books:")
    available = filter_available(all_books)
    print(f"  Available books ({len(available)}): {[b.title for b in available]}")

    print("\n" + "=" * 70)
    print("DEMO COMPLETED SUCCESSFULLY".center(70))
    print("=" * 70)

if __name__ == "__main__":
    run_demo()