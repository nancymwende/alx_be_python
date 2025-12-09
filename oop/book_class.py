class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        return f"Book('{self.title}', '{self.author}', {self.year_published})"
    
    def __repr__(self):
        return f"Book('{self.title}',{self.author}', {self.year_published})"
    def __del__(self):
        print(f"The book '{self.title}' by {self.author} has been deleted.")