from abc import ABC, abstractmethod


class Book(ABC):
    nextId = 10_000  # class attribute
    recordPrefix = "bf"

    def __init__(self, writer, title):
        self._id = Book.nextId
        Book.nextId += 10
        self._writer = writer
        self._title = Book.recordPrefix + "_" + title
        self.isBorrow = False

    @property # getter method
    def id(self):
        return self._id

    def getwriter(self):
        return self._writer

    @property  #getTitle    book.getTitle()     book.title
    def title(self):
        return self._title

    @title.setter  # setTitle   book.setTitle("new title")    book.title = "new title"
    def title(self, newTitle):
        self._title = newTitle

    @abstractmethod  # decorator
    def borrow(self):
        pass

    def __str__(self):
        return f"Id {self._id} Writer {self._writer} title {self._title}"


class Audiobook(Book):
    def __init__(self, writer, title, length):
        super().__init__(writer, title)
        self._length = length

    def getlength(self):
        return self._length
    #override
    def borrow(self):
        if self.isBorrow == False:
            print("Audıo file sent")
            self.isBorrow = True
        else:
            raise BookIsAlreadyBorrowedExp("")
    #override
    def __str__(self):
        return "Audio Book " + super().__str__() + f" Length {self._length}"


class Videobook(Book):
    def __init__(self, writer, title, vq):
        super(Videobook, self).__init__(writer, title)
        self.videoquality = vq

    def getvideoquality(self):
        return self.videoquality

    def borrow(self):
        if self.isBorrow == False:
            print("Video link sent")
            self.isBorrow = True
        else:
            raise BookIsAlreadyBorrowedExp("")


    def __str__(self):
        return "Video Book " + super().__str__() + f" Quality {self.videoquality}"


class TextBook(Book):
    def __init__(self, writer, title, pageCount):
        super().__init__(writer, title)
        self.pageCount = pageCount

    def getPageCount(self):
        return self.pageCount

    def borrow(self):
        if self.isBorrow == False:
            print("Cargo takip numarası...")
            self.isBorrow = True
        else:
            raise BookIsAlreadyBorrowedExp("")


    def __str__(self):
        return "Text Book " + super().__str__() + f" Page Count {self.pageCount}"


class Bookwebsite:
    def __init__(self, domainName):
        self.__name = domainName
        self.__allBooks = []

    def addBook(self, book):
        self.__allBooks.append(book)

    def removeBook(self, book):
        self.__allBooks.remove(book)

    def borrowBook(self, book):
        book.borrow()

    def returnBook(self, book):
        book.returnBook()

    def displayBooks(self):
        for book in self.__allBooks:
            print(book)

    def findBook(self, id):
        for book in self.__allBooks:
            if book.id == int(id):
                return book

        raise BookNotFoundException("Book not found")


######################################################################
class BookNotFoundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class BookIsAlreadyBorrowedExp(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class App:
    site = Bookwebsite("book.com")

    @staticmethod
    def menu():
        print("1 Add Book")
        print("2 display book")
        print("3 borrow book")
        print("4 exit")

    @staticmethod
    def boookCatMenu():
        print("1 Audio book")
        print("2 Video book")
        print("3 Text book")
        print("4 main menu")

    @staticmethod
    def getBookInfo(s):
        writer = input("Writer")
        title = input("title")
        other = input(s)
        return writer, title, other

    @staticmethod
    def main():
        while True:
            App.menu()
            opt = input("Choose")
            if opt == "1":
                while True:
                    App.boookCatMenu()
                    opt = input("Choose")
                    if opt == "1":
                        writer, title, length = App.getBookInfo("Length")
                        ab = Audiobook(writer, title, length)
                        App.site.addBook(ab)
                    elif opt == "2":
                        writer, title, q = App.getBookInfo("Video Quality")
                        vb = Videobook(writer, title, q)
                        App.site.addBook(vb)
                    elif opt == "3":
                        writer, title, pc = App.getBookInfo("Page Count")
                        vb = TextBook(writer, title, pc)
                        App.site.addBook(vb)
                    elif opt == "4":
                        break
                    else:
                        print("Invalid option")
            elif opt == "2":
                App.site.displayBooks()
            elif opt == "3":
                App.site.displayBooks()
                bookId = input("Please chhose ıd")
                try:
                    book = App.site.findBook(bookId)
                    App.site.borrowBook(book)
                except BookNotFoundException:
                    print("Given id not found in website")
                except BookIsAlreadyBorrowedExp:
                    print("Not suitable for borrow")

            elif opt == "4":
                print("Goodbye")
                break
            else:
                print("Invalid option")


# app = App()
# app.main()
App.main()
