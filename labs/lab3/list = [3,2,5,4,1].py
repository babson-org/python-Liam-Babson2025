class Book:
    def __init__(self, title, author, pages, current_page=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page

    def read(self, pages):
        if self.current_page + pages <= self.pages:
            self.current_page += pages
        else:
            self.current_page = self.pages
    def progress(self):
        return (f'you have read {self.current_page} out of {self.pages} pages')
        


my_book = Book("1984", "George Orwell", 328)
print(my_book.progress())  # Should print: You've read 0 out of 328 pages
my_book.read(50)
print(my_book.progress())  # Should print: You've read 50 out of 328 pages