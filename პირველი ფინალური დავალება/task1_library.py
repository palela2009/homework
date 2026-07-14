class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = [
            Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1200),
            Book("დიდოსტატის მარჯვენა", "კონსტანტინე გამსახურდია", 1939),
            Book("სამოსელი პირველი", "გურამ დოჩანაშვილი", 1975),
            Book("ყაჩაღები", "ვაჟა-ფშაველა", 1890),
            Book("კაცია-ადამიანი?!", "ილია ჭავჭავაძე", 1863),
            Book("ჯაყოს ხიზნები", "მიხეილ ჯავახიშვილი", 1924),
            Book("დათა თუთაშხია", "ჭაბუა ამირეჯიბი", 1973),
            Book("მთვარის მოტაცება", "კონსტანტინე გამსახურდია", 1935),
            Book("გზაზე ერთი კაცი მიდიოდა", "ოთარ ჭილაძე", 1973),
            Book("სარდაფი", "აკაკი წერეთელი", 1900)
        ]

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)

    def show_books(self):
        for index, book in enumerate(self.books, 1):
            print(f"{index}. {book.title} | {book.author}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def take_book(self, title):
        book = self.search_book(title)
        if book:
            self.books.remove(book)
            return book
        return None


def main():
    library = Library()
    while True:
        print("\n--- ბიბლიოთეკის მენიუ ---")
        print("1. ყველა წიგნის ნახვა")
        print("2. წიგნის დამატება")
        print("3. წიგნის ძებნა სათაურით")
        print("4. წიგნის გატანა წასაკითხად")
        print("5. გასვლა")

        choice = input("აირჩიეთ მოქმედება (1-5): ").strip()

        if choice == "1":
            print("\nბიბლიოთეკაში არსებული წიგნები:")
            library.show_books()
        elif choice == "2":
            title = input("შეიყვანეთ სათაური: ").strip()
            author = input("შეიყვანეთ ავტორი: ").strip()
            year = int(input("შეიყვანეთ წელი: ").strip())
            library.add_book(title, author, year)
            print("წიგნი წარმატებით დაემატა!")
        elif choice == "3":
            title = input("შეიყვანეთ საძიებო წიგნის სათაური: ").strip()
            book = library.search_book(title)
            if book:
                print(f"მოიძებნა: {book}")
            else:
                print("წიგნი ვერ მოიძებნა.")
        elif choice == "4":
            title = input("შეიყვანეთ წიგნის სათაური წასაკითხად გასატანად: ").strip()
            book = library.take_book(title)
            if book:
                print(f"თქვენ გაიტანეთ წიგნი: {book}")
            else:
                print("ეს წიგნი ბიბლიოთეკაში არ არის.")
        elif choice == "5":
            break


if __name__ == "__main__":
    main()