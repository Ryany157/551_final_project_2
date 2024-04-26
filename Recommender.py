import os
import tkinter.messagebox
import tkinter.filedialog
from Book import Book
from Show import Show

class Recommender:
    def __init__(self):
        self.__books = {}   # key-value: id-book<object>
        self.__shows = {}   # key-value: id-show<object>
        self.__associations = {}   # key-value: id-dictionary(id-the number of times the outer id and inner id are associated)

    # done
    def loadBooks(self):
        #books10.csv -> self.__books
        filename = tkinter.filedialog.askopenfilename(title="Files",initialdir=os.getcwd())
        while os.path.exists(filename):
            filename = tkinter.filedialog.askopenfilename(title="Files",initialdir=os.getcwd())
        file = open(filename, "r")
        for line in file:
            # line is <string>
            line = line.strip()
            entry = line.split(",")
            self.__books[entry[0]] = Book(*entry)
        # print(self.__books)
        file.close()

    # done
    def loadShows(self):
        #shows10.csv -> self.__shows
        filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        while os.path.exists(filename):
            filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        file = open(filename, "r")
        for line in file:
            # line is <string>
            line = line.strip()
            entry = line.split(",")
            self.__shows[entry[0]] = Show(*entry)
        # print(self.__shows)
        file.close()

    # done
    def loadAssociations(self):
        # associated10.csv -> self.__associations
        filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        while os.path.exists(filename):
            filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        file = open(filename, "r")
        for line in file:
            line = line.strip()
            entry = line.split(",")  # ["showid", "book id"]
            if entry[0] not in self.__associations:
                self.__associations[entry[0]] = {f"{entry[1]}": 1}
            else:
                if entry[1] in self.__associations[entry[0]]:  # associations[entry[0]] -> inner dictionary
                    self.__associations[entry[0]][entry[1]] += 1
                else:
                    self.__associations[entry[0]][entry[1]] = 1  # add {"entry[1]": 1}
        # print(self.__associations)
        file.close()
        file = open("associated10.csv", "r")
        for line in file:
            line = line.strip()
            entry = line.split(",")  # ["showid", "book id"]
            if entry[1] not in self.__associations:
                self.__associations[entry[1]] = {f"{entry[0]}": 1}
            else:
                if entry[0] in self.__associations[entry[1]]:  # associations[entry[0]] -> inner dictionary
                    self.__associations[entry[1]][entry[0]] += 1
                else:
                    self.__associations[entry[1]][entry[0]] = 1  # add {"entry[1]": 1}
        # print(self.__associations)
        file.close()

    # done but format
    def getMovieList(self):
        movieList = "Title\t Movie"
        for show in self.__shows.values():   # show -> <object>
            if show.getType() == "Movie":
                movieList += f"{show.getTitle()}\t{show.getDuration()}\n"
        return movieList

    # done but format
    def getTVList(self):
        tvList = "Title\t Seasons"
        for show in self.__shows.values():   # show -> <object>
            if show.getType() == "TV Show":
                tvList += f"{show.getTitle()}\t{show.getDuration()}\n"
        return tvList

    # done but format
    def getBookList(self):
        bookList = "Title\t Author"
        for book in self.__books.values():
            bookList += f"{book.getTitle()}\t{book.getAuthors()}\n"
        return bookList

    # ***Statistics***
    def getMovieStats(self):
        #
        title = "Ratings:"
        rate = {}  # {"rate": 1}
        director = {}
        actor = {}
        genre = {}
        count = 0  # number of movie
        duration = 0
        for show in self.__shows.values():   # show -> <object>
            if show.getType() == "Movie":
                count += 1

                # Average movie duration
                time = show.getDuration().split()
                duration += float(time[0])

                # Rating for movies
                if show.getShowRating() not in rate:
                    rate[show.getShowRating()] = 1
                else:
                    rate[show.getShowRating()] += 1

                # Director the most
                for i in show.getDirectors().split("\\"):
                    if i not in director:
                        director[i] = 1
                    else:
                        director[i] += 1

                # Actor the most
                for i in show.getActors().strip().split("\\"):
                    if i not in actor:
                        actor[i] = 1
                    else:
                        actor[i] += 1
                # Genre the most
                for i in show.getGenres().strip().split("\\"):
                    if i not in genre:
                        genre[i] = 1
                    else:
                        genre[i] += 1

        rateStats = ""
        for i in rate:
            rateStats += f"{i} {rate[i]/count:.2%}\n"

        # average duration
        averageStats = f"Average Movie Duration {duration / count:.2f} minutes"

        # most Director
        countDirec = 0
        mostDirec = ""
        for i in director.keys():
            if director[i] > countDirec and i != '':
                countDirec = director[i]
                mostDirec = i
        directorStats = f"Most prolific Director: {mostDirec}"

        # most Actor
        countAct = 0
        mostAct = ""
        for i in actor.keys():
            if actor[i] > countAct and i != '':
                countAct = actor[i]
                mostAct = i
        actorStats = f"Most prolific Actor: {mostAct}"

        # most Genre
        countGen = 0
        mostGen = ""
        for i in genre.keys():
            if genre[i] > countGen and i != '':
                countGen = genre[i]
                mostGen = i
        genreStats = f"Most prolific Genre: {mostGen}"

        movieStats = f"{title}\n{rateStats}\n{averageStats}\n{directorStats}\n{actorStats}\n{genreStats}"

        return movieStats

    def getTVStats(self):
        title = "Ratings:\n"
        rate = {}  # {"rate": 1}
        director = {}
        actor = {}
        genre = {}
        count = 0  # number of movie
        duration = 0
        for show in self.__shows.values():  # show -> <object>
            if show.getType() == "TV Show":
                count += 1

                # Average seasons duration
                seasons = show.getDuration().split()
                duration += float(seasons[0])

                # Rating for TV Show
                if show.getShowRating() not in rate:
                    rate[show.getShowRating()] = 1
                else:
                    rate[show.getShowRating()] += 1

                # Actor the most
                for i in show.getActors().strip().split("\\"):
                    if i not in actor:
                        actor[i] = 1
                    else:
                        actor[i] += 1
                # Genre the most
                for i in show.getGenres().strip().split("\\"):
                    if i not in genre:
                        genre[i] = 1
                    else:
                        genre[i] += 1

        rateStats = ""
        for i in rate:
            rateStats += f"{i} {rate[i] / count:.2%}\n"

        # average duration
        averageStats = f"Average Number of Seasons {duration / count:.2f} seasons"

        # most Actor
        countAct = 0
        mostAct = ""
        for i in actor.keys():
            if actor[i] > countAct and i != '':
                countAct = actor[i]
                mostAct = i
        actorStats = f"Most prolific Actor: {mostAct}"

        # most Genre
        countGen = 0
        mostGen = ""
        for i in genre.keys():
            if genre[i] > countGen and i != '':
                countGen = genre[i]
                mostGen = i
        genreStats = f"Most prolific Genre: {mostGen}"

        tvshowStats = f"{title}\n{rateStats}\n{averageStats}\n{actorStats}\n{genreStats}"

        return tvshowStats

    def bookStats(self):
        author = {}
        genre = {}
        count = 0  # number of movie
        pages = 0
        for book in self.__books.values():  # show -> <object>
            if book.getId() != "bookID":
                count += 1

                # Average seasons duration
                pages += float(book.getPages())

                # Actor the most
                for i in book.getAuthors().strip().split("\\"):
                    if i not in author:
                        author[i] = 1
                    else:
                        author[i] += 1
                # Genre the most
                for i in book.getPublisher().strip().split("\\"):
                    if i not in genre:
                        genre[i] = 1
                    else:
                        genre[i] += 1

        # average duration
        averageStats = f"Average Page {pages / count:.2f} pages"

        # most Author
        countAut = 0
        mostAut = ""
        for i in author.keys():
            if author[i] > countAut and i != '':
                countAut = author[i]
                mostAut = i
        autorStats = f"Most prolific Autor: {mostAut}"

        # most Genre
        countGen = 0
        mostGen = ""
        for i in genre.keys():
            if genre[i] > countGen and i != '':
                countGen = genre[i]
                mostGen = i
        genreStats = f"Most Prolific Publisher: {mostGen}"

        bookStats = f"{averageStats}\n{autorStats}\n{genreStats}"

        return bookStats

    # done but format
    def searchTVMovies(self, show="", title="", director="", genre=""):
        if show not in ["Movie", "TV Show"]:
            tkinter.messagebox.showerror(title="Error", message=f"Please select Movie or TV Show from Type first!")
            return "No Results"
        elif title == "" and director == "" and genre == "":
            tkinter.messagebox.showerror(title="Error", message=f"Please enter information for the Title, Directory, Actor and/or Genre first!")
            return "No Results"
        else:
            # 对非“”的元素进行比对
            for i in self.__shows.values():
                if title in i.getTitle() and title != "":
                    searchresult = f"=>\n{i.getTitle()}\n{i.getDirectors()}\n{i.getActors()}\n{i.getGenres()}"
                    return searchresult
                if director in i.getDirectors() and director != "":
                    searchresult = f"==>\n{i.getTitle()}\n{i.getDirectors()}\n{i.getActors()}\n{i.getGenres()}"
                    return searchresult
                if genre in i.getGenres() and genre != "":
                    searchresult = f"===>\n{i.getTitle()}\n{i.getDirectors()}\n{i.getActors()}\n{i.getGenres()}"
                    return searchresult

    # done but format
    def searchBooks(self, title="", author="", publisher=""):
        if title == "" and author == "" and publisher == "":
            tkinter.messagebox.showerror(title="Error", message=f"Please enter information for the Title, Author, and/or Publisher first!")
            return "No Results"
        else:
            # 对非“”的元素进行比对
            for i in self.__books.values():
                if title in i.getTitle() and title != "":
                    searchresult = f"=>\n{i.getTitle()}\n{i.getAuthors()}\n{i.getPublisher()}"
                    return searchresult
                if author in i.getAuthors() and author != "":
                    searchresult = f"==>\n{i.getTitle()}\n{i.getAuthors()}\n{i.getPublisher()}"
                    return searchresult
                if publisher in i.getPublisher() and publisher != "":
                    searchresult = f"===>\n{i.getTitle()}\n{i.getAuthors()}\n{i.getPublisher()}"
                    return searchresult

    # done
    def getRecommendations(self, type="", title=""):
        recommendInfo = ""
        if type in ["Movie", "TV Show"]:
            print("show!")
            for show in self.__shows.values():
                if title == show.getTitle():  # whether title is exist 存在则进入
                    showId = show.getId()  # string: show id
                    print("show id=", showId)
                    print(self.__associations[showId].keys())
                    for i in self.__associations[showId].keys():  # i -> "book id"
                        recommendInfo += self.__books[i].__str__()  # books[i] -> object
                    return recommendInfo
            # title no exsit
            return "No result!"

        if type == "Book":
            print("Book!")
            for book in self.__books.values():
                if title == book.getTitle():  # whether title is exist 存在则进入
                    bookId = book.getId()  # string: book id
                    print("book id=", bookId)
                    print(self.__associations[bookId].keys())
                    for i in self.__associations[bookId].keys():  # i -> "show id"
                        recommendInfo += self.__shows[i].__str__()  # shows[i] -> object
                    return recommendInfo
            # title no exist
            return "No result!"

        else:   #if user do not select any combobox items
            return "No result!"



