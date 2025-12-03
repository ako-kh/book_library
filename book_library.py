from rbtree import RedBlackTree as rbt
from string import ascii_lowercase
from tabulate import tabulate


class Book:
    def __init__(self, name, author, realise_year):
        self.name = name.lower()
        # todo check if name contains valid characters name shoul be more than 0 chars
        self.author = author
        self.realise_year = realise_year

    def __str__(self):
        return f"Name: {self.name} | Author: {self.author} | Realise Year: {self.realise_year}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.name == other.name

    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.name < other.name

    def __le__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.name <= other.name

    def __ne__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.name != other.name

    def __gt__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.name > other.name

    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError(f"Can't compare {type(self)} with {type(other)}")
        return self.name >= other.name


class BookManager:
    ordered_by_letter = {i: rbt() for i in ascii_lowercase}

    def add_book(self, name, author, realise_year):
        letter_tree = self.ordered_by_letter[name[0]]
        letter_tree.insert(
            Book(name, author, realise_year)
        )

    def print_all_books(self):
        headers = ["Name", "Author", "Realise year"]
        body = []
        for _, tree in self.ordered_by_letter.items():
            node_list = tree.get_all_nodes()
            if node_list:
                for node in node_list:
                    book = node.value
                    body.append([book.name, book.author, book.realise_year])
        print(tabulate(body, headers=headers, showindex="always", tablefmt="pipe", colalign=("center", "center", "center", "center")))

    def search_book(self, name):
        tree = self.ordered_by_letter[name[0]]
        t_book = Book(name, "fake", 0)
        search_result = tree.search(t_book)
        if search_result:
            return search_result.value
        return f"Could not find book by name '{name}'."
