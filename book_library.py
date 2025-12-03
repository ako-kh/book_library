import json
from rbtree import RedBlackTree as rbt
from string import ascii_lowercase
from tabulate import tabulate



class Book:
    def __init__(self, title, author, realise_year):
        if not 0 < len(title):
            raise ValueError("Book title should contain at least one character")
        self.title = title.capitalize()
        if not 0 < len(author):
            raise ValueError("Author should contain at least one character")
        self.author = author
        self.realise_year = realise_year

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Realise Year: {self.realise_year}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.title == other.title

    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.title < other.title

    def __le__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.title <= other.title

    def __ne__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.title != other.title

    def __gt__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.title > other.title

    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.title >= other.title


class BookManager:
    # ordered_by_letter = {i: rbt() for i in ascii_lowercase}
    ordered_by_letter = {}


    def add_book(self, title, author, realise_year):
        new_book = Book(title, author, realise_year)
        title_first_c = new_book.title[0]

        try:
            letter_tree = self.ordered_by_letter[title_first_c]
        except KeyError:
            self.ordered_by_letter[title_first_c] = rbt()
            letter_tree = self.ordered_by_letter[title_first_c]

        letter_tree.insert(
            new_book
        )

    def print_all_books(self):
        headers = ["Title", "Author", "Realise year"]
        body = []
        for i in sorted(self.ordered_by_letter.keys()):
            node_list = self.ordered_by_letter[i].get_all_nodes()
            if node_list:
                for node in node_list:
                    book = node.value
                    body.append([book.title, book.author, book.realise_year])
            body = sorted(body, key=lambda title:title[0])                           # sorting body by alphabetic order
        print(tabulate(body, headers=headers, showindex="always", tablefmt="pipe", colalign=("center", "left", "left", "center")))

    def search_book(self, title):
        # todo key validation
        t_book = Book(title, "fake", 0)
        tree = self.ordered_by_letter[t_book.title[0]]
        search_result = tree.search(t_book)
        if search_result:
            return search_result.value
        return f"Could not find book by title '{title.capitalize()}'."

    def import_books_json(self, json_file):
        if "json" != json_file.split(".")[-1]:
            raise ValueError("File must json")

        with open(json_file) as f:
            book_list = json.load(f)
        for bool_dict in book_list:
            self.add_book(bool_dict["title"], bool_dict["author"], bool_dict["year"])

    def save_as_json(self, file_name):
        if "json" != file_name.split(".")[-1]:
            raise ValueError("File must json")

        book_list = []
        for _, tree in self.ordered_by_letter.items():
            node_list = tree.get_all_nodes()
            if node_list:
                for node in node_list:
                    book = node.value
                    book_list.append({
                        "title": book.title,
                        "author": book.author,
                        "year": book.realise_year
                    })

        with open(file_name, "w") as f:
            json.dump(book_list, f, indent=4)
