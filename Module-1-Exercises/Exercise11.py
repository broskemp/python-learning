class Publication:
    def __init__(self,name):
        self.name = name


class Book(Publication):
    def __init__(self,name,author,page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_book(self):
        print(f"The book {self.name} has {self.page_count} pages and is written by {self.author}")


class Magazine(Publication):
    def __init__(self,name,chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_magazine(self):
        print(f"The chief editor of the {self.name} magazine is {self.chief_editor}")


Donald_Duck = Magazine("Donald Duck","Aki Hyyppä")
Compartment_6 = Book("Compartment No. 6","Rosa Liksom",192)

Donald_Duck.print_magazine()
Compartment_6.print_book()

# Task 2 of Exercise 11 is in the Exercise9.py file, also linked in the submission
