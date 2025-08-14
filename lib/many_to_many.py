from datetime import datetime

class Author:
    _all_authors = []

    def __init__(self, name: str):
        self.name = name
        Author._all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract._all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        if royalties < 0:
            raise Exception("royalties must be non-negative")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    @classmethod
    def all_authors(cls):
        return cls._all_authors


class Book:
    _all_books = []

    def __init__(self, title: str):
        self.title = title
        Book._all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self):
        return [contract for contract in Contract._all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})

    @classmethod
    def all_books(cls):
        return cls._all_books


class Contract:
    _all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be a Book instance")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        if value < 0:
            raise Exception("royalties must be non-negative")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date_str):
        # target_date = datetime.strptime(date, "%m/%d/%Y")
        filtered_contracts = [contract for contract in cls._all if contract.date == date_str]
        return sorted(filtered_contracts, key=lambda c: datetime.strptime(c.date, "%m/%d/%Y"))