from book_library import BookManager


bm = BookManager()
# print(bm.ordered_by_letter)
bm.add_book("_osndnd", "Akaki", 1234)
print(bm.ordered_by_letter)
# bm.add_book("aco", "Akaki", 1234)
# bm.add_book("abo", "Akaki", 1234)
# bm.add_book("akkdo", "Akaki", 1234)
# bm.add_book("akosndnd", "Akaki", 1234)

# bm.add_book("bkkdo", "Akaki", 1234)
# bm.add_book("bkosndnd", "Akaki", 1234)
# bm.add_book("_osndnd", "Akaki", 1234)

bm.print_all_books()
# print(bm.search_book("ako"))
bm.import_books_json("books.json")
bm.print_all_books()
bm.save_as_json("books_save.json")



"""
todo sorted library class with

function for importing books from json

functions for serializing and deserializing library instance to binary/json

functions for finding book by name, author, realis date

function for printing data books as a grid
"""