class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# управління списком книг (додавання, видалення, пошук)
class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def find_book(self, title):
        return next((book for book in self.books if book.title == title), None)

# відображення інформації
class LibraryUI:
    def show_books(self, books):
        if not books:
            print("У бібліотеці немає книг.")
        else:
            for book in books:
                print(f"{book.title} - {book.author} ({book.year})")

    def show_message(self, message):
        print(message)

# Використання:
if __name__ == "__main__":
    # Ініціалізація
    manager = LibraryManager()
    ui = LibraryUI()

    # Додавання книг
    manager.add_book(Book("Кобзар", "Тарас Шевченко", 1840))
    manager.add_book(Book("Тіні забутих предків", "Михайло Коцюбинський", 1911))
    manager.add_book(Book("Зачарована Десна", "Олександр Довженко", 1957))

    #список книг
    ui.show_books(manager.books)

    # Пошук книги
    book = manager.find_book("Кобзар")
    if book:
        ui.show_message(f"Знайдено книгу: {book.title} - {book.author} ({book.year})")
    else:
        ui.show_message("Книгу не знайдено.")

    # Видалення книги
    manager.remove_book("Кобзар")
    ui.show_books(manager.books)
