from book_library import BookManager


bm = BookManager()

bm.print_all_books()

bm.add_book("Ako", "Akaki", 1234)

bm.import_books_json("books.json")

bm.print_all_books()

print(bm.search_book("hamlet"))

bm.save_as_json("book_save.json")

bm.consol_interface()
