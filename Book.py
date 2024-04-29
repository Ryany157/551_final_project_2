from Media import Media
# self, id, title, authors, averageRating, isbn, isbn13, language, pages, bookRating, date, publisher
class Book(Media):
    def __init__(self, id, title, authors, averageRating, isbn, isbn13, language, pages, bookRating, date, publisher):
        Media.__init__(self, id, title, averageRating)
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__language = language
        self.__pages = pages
        self.__bookRating = bookRating
        self.__date = date
        self.__publisher = publisher

    # Getter
    def getAuthors(self):
        return self.__authors

    def getIsbn(self):
        return self.__isbn

    def getIsbn13(self):
        return self.__isbn13

    def getLanguage(self):
        return self.__language

    def getPages(self):
        return self.__pages

    def getBookRating(self):
        return self.__bookRating

    def getDate(self):
        return self.__date

    def getPublisher(self):
        return self.__publisher

    # Setter
    def setAuthors(self, newAuthors):
        self.__authors = newAuthors

    def setIsbn(self, newIsbn):
        self.__isbn = newIsbn

    def setIsbn13(self, newIsbn13):
        self.__isbn13 = newIsbn13

    def setLanguage(self, newLanguage):
        self.__language = newLanguage

    def setPages(self, newPages):
        self.__pages = newPages

    def setBookRating(self, newBookRating):
        self.__bookRating = newBookRating

    def setDate(self, newDate):
        self.__date = newDate

    def setPublisher(self, newPublisher):
        self.__publisher = newPublisher

    def __str__(self):
        return (f"Title:\n{self._title}\n"
                f"Author:\n{self.__authors}\n"
                f"Average Rating:\n{self._averageRating}\n"
                f"ISBN:\n{self.__isbn}\n"
                f"ISBN13:\n{self.__isbn13}\n"
                f"Language Code:\n{self.__language}\n"
                f"Pages:\n{self.__pages}\n"
                f"Rating Count:\n{self.__bookRating}\n"
                f"Publication Date:\n{self.__date}\n"
                f"Publisher:\n{self.__publisher}\n"
                f"\n\n****************************************************\n\n")

