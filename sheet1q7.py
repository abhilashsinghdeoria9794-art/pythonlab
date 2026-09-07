# Library Management System Using Inheritance and Polymorphism 
class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.issued = False

    def display(self):
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Status:", "Issued" if self.issued else "Available")

    def borrow(self):
        if self.issued:
            print(self.title, "is already issued.")
        else:
            self.issued = True
            print(self.title, "has been borrowed.")

    def return_item(self):
        if self.issued:
            self.issued = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")


#derived classes
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def display(self):
        print("\n Book ")
        super().display()
        print("Author:", self.author)

class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        super().__init__(item_id, title)
        self.issue_number = issue_number

    def display(self):
        print("\n Magazine ")
        super().display()
        print("Issue Number:", self.issue_number)

class Journal(LibraryItem):
    def __init__(self, item_id, title, research_field):
        super().__init__(item_id, title)
        self.research_field = research_field

    def display(self):
        print("\n Journal ")
        super().display()
        print("Research Field:", self.research_field)


# Main program
book = Book(101, "python by harry", "code with harry")
magazine = Magazine(102, "India Yesterday", 245)
journal = Journal(103, "My life MY Rule", " journey of a sunflower")


# Polymorphism
# Using Inheritance and Polymorphism


# Base class
items = [book, magazine, journal]

print(" LIBRARY ITEMS ")

for item in items:
    item.display()


print("\n BORROW OPERATIONS ")

for item in items:
    item.borrow()


print("\n TRYING TO BORROW BOOK AGAIN ")

book.borrow()


print("\n RETURN OPERATIONS ")

for item in items:
    item.return_item()


print("\n FINAL STATUS ")

for item in items:
    item.display()