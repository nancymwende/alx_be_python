class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        return f"Book('{self.title}', '{self.author}', {self.year_published})"