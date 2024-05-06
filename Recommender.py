import os
import tkinter.messagebox
import tkinter.filedialog
from matplotlib.figure import Figure
from Book import Book
from Show import Show

class Recommender:
    def __init__(self):
        self.__books = {}   # key-value: id-book<object>
        self.__shows = {}   # key-value: id-show<object>
        self.__associations = {}   # key-value: id-dictionary(id-the number of times the outer id and inner id are associated)

    def loadBooks(self):
        '''
        Read books.csv file to create book object
        '''
        #books.csv -> self.__books
        filename = tkinter.filedialog.askopenfilename(title="Files",initialdir=os.getcwd())
        while not os.path.exists(filename):
            filename = tkinter.filedialog.askopenfilename(title="Files",initialdir=os.getcwd())
        file = open(filename, "r",encoding="utf-8")
        for line in file:
            # line is <string>
            line = line.strip()
            entry = line.split(",")
            self.__books[entry[0]] = Book(*entry)
        # print(self.__books)
        file.close()

    def loadShows(self):
        '''
        Read shows.csv file to create show object
        '''
        #shows10.csv -> self.__shows
        filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        while not os.path.exists(filename):
            filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        file = open(filename, "r",encoding="utf-8")
        for line in file:
            # line is <string>
            line = line.strip()
            entry = line.split(",")
            self.__shows[entry[0]] = Show(*entry)
        # print(self.__shows)
        file.close()

    def loadAssociations(self):
        '''
        Read associated.csv file to create association object
        '''
        # associated10.csv -> self.__associations
        filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        while not os.path.exists(filename):
            filename = tkinter.filedialog.askopenfilename(title="Files", initialdir=os.getcwd())
        file = open(filename, "r",encoding="utf-8")
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
        file = open(filename, "r",encoding="utf-8")
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

    def getMovieList(self):
        '''
        Get the information of Movie and then print out
        :return: A String of movie information
        '''
        titleWidth = 0
        durationWidth = 0
        for show in self.__shows.values():  # show -> <object>
            if show.getType() == "Movie":
                if len(show.getTitle()) > titleWidth:
                    titleWidth = len(show.getTitle())
                if len(show.getDuration()) > durationWidth:
                    durationWidth = len(show.getDuration())

        movieList = f"{"Title":<{titleWidth + 3}}{"Runtime":<{durationWidth}}\n"

        for show in self.__shows.values():  # show -> <object>
            if show.getType() == "Movie":
                movieList += f"{show.getTitle():<{titleWidth + 3}}{show.getDuration():<{durationWidth}}\n"
        return movieList

    def getTVList(self):
        '''
        Get the information of TV Show and then print out
        :return: A String of TV show information
        '''
        titleWidth = 0
        seasonsWidth = 0

        for show in self.__shows.values():  # show -> <object>
            if show.getType() == "TV Show":
                if len(show.getTitle()) > titleWidth:
                    titleWidth = len(show.getTitle())
                if len(show.getDuration()) > seasonsWidth:
                    seasonsWidth = len(show.getDuration())

        tvList = f"{"Title":<{titleWidth + 3}}{"Seasons":<{seasonsWidth}}\n"

        for show in self.__shows.values():  # show -> <object>
            if show.getType() == "TV Show":
                tvList += f"{show.getTitle():<{titleWidth + 3}}{show.getDuration():<{seasonsWidth}}\n"
        return tvList

    def getBookList(self):
        '''
        Get the information of Book and then print out
        :return: A String of books information
        '''
        titleWidth = 0
        authorWidth = 0
        for book in self.__books.values():  # show -> <object>
            if len(book.getTitle()) > titleWidth:
                titleWidth = len(book.getTitle())
            if len(book.getAuthors()) > authorWidth:
                authorWidth = len(book.getAuthors())

        bookList = f"{"Title":<{titleWidth + 3}}{"Author(s)":<{authorWidth}}\n"

        for book in self.__books.values():  # show -> <object>
            if book.getId() != "bookID":   # filter the info of first line
                bookList += f"{book.getTitle():<{titleWidth + 3}}{book.getAuthors():<{authorWidth}}\n"
        return bookList

    # ***Statistics***
    def getMovieStats(self):
        '''
        Calculate the statistics of Movie and then print out
        :return: A string of Movie Statistics
        '''
        title = "Ratings:\n"
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
        for i in rate.keys():
            if i == "":
                rateStats += f"None {rate[i] / count:.2%}\n"
            else:
                rateStats += f"{i} {rate[i]/count:.2%}\n"

        # average duration
        averageStats = f"Average Movie Duration {duration / count:.2f} minutes\n"

        # most Director
        countDirec = 0
        mostDirec = ""
        for i in director.keys():
            if director[i] > countDirec and i != '':
                countDirec = director[i]
                mostDirec = i
        directorStats = f"Most prolific Director: {mostDirec}\n"

        # most Actor
        countAct = 0
        mostAct = ""
        for i in actor.keys():
            if actor[i] > countAct and i != '':
                countAct = actor[i]
                mostAct = i
        actorStats = f"Most prolific Actor: {mostAct}\n"

        # most Genre
        countGen = 0
        mostGen = ""
        for i in genre.keys():
            if genre[i] > countGen and i != '':
                countGen = genre[i]
                mostGen = i
        genreStats = f"Most prolific Genre: {mostGen}\n"

        movieStats = f"{title}{rateStats}\n{averageStats}\n{directorStats}\n{actorStats}\n{genreStats}"

        return movieStats

    def getTVStats(self):
        '''
        Calculate the statistics of TV Show and then print out
        :return: A string of TV Show Statistics
        '''
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
        for i in rate.keys():
            if i == "":
                rateStats += f"None {rate[i] / count:.2%}\n"
            else:
                rateStats += f"{i} {rate[i] / count:.2%}\n"

        # average duration
        averageStats = f"Average Number of Seasons {duration / count:.2f} seasons\n"

        # most Actor
        countAct = 0
        mostAct = ""
        for i in actor.keys():
            if actor[i] > countAct and i != '':
                countAct = actor[i]
                mostAct = i
        actorStats = f"Most prolific Actor: {mostAct}\n"

        # most Genre
        countGen = 0
        mostGen = ""
        for i in genre.keys():
            if genre[i] > countGen and i != '':
                countGen = genre[i]
                mostGen = i
        genreStats = f"Most prolific Genre: {mostGen}\n"

        tvshowStats = f"{title}{rateStats}\n{averageStats}\n{actorStats}\n{genreStats}"

        return tvshowStats

    def getBookStats(self):
        '''
        Calculate the statistics of Books and then print out
        :return: A string of Books Statistics
        '''
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
        averageStats = f"Average Page {pages / count:.2f} pages\n"

        # most Author
        countAut = 0
        mostAut = ""
        for i in author.keys():
            if author[i] > countAut and i != '':
                countAut = author[i]
                mostAut = i
        autorStats = f"Most prolific Autor: {mostAut}\n"

        # most Genre
        countGen = 0
        mostGen = ""
        for i in genre.keys():
            if genre[i] > countGen and i != '':
                countGen = genre[i]
                mostGen = i
        genreStats = f"Most Prolific Publisher: {mostGen}\n"

        bookStats = f"{averageStats}\n{autorStats}\n{genreStats}"

        return bookStats

    def searchTVMovies(self, show="", title="", director="", actor="", genre=""):
        '''
        Get shows type and each one of the other parameter to search the Shows
        :return: A string containing all the related information
        '''
        search = set()  # store the object without repeating
        titleWidth = 8
        directorWidth = 10
        actorWidth = 8
        genreWidth = 0
        if show not in ["Movies", "TV Shows"]:
            tkinter.messagebox.showerror(title="Error", message=f"Please select Movie or TV Show from Type first!")
            return "No Results"
        elif title == "" and director == "" and actor =="" and genre == "":
            tkinter.messagebox.showerror(title="Error", message=f"Please enter information for the Title, Directory, Actor and/or Genre first!")
            return "No Results"
        else:
            for i in self.__shows.values():
                if title in i.getTitle() and title != "":  # filter the ""
                    search.add(i)
                if director in i.getDirectors() and director != "":
                    search.add(i)
                if actor in i.getActors() and actor != "":
                    search.add(i)
                if genre in i.getGenres() and genre != "":
                    search.add(i)
            if len(search) == 0: return "No Results"  # if there is no related shows
            for i in search:  # i -> <target object>
                if len(i.getTitle()) > titleWidth: titleWidth = len(i.getTitle())
                if len(i.getDirectors()) > directorWidth: directorWidth = len(i.getDirectors())
                if len(i.getActors()) > actorWidth: actorWidth = len(i.getActors())
                if len(i.getGenres()) > genreWidth: genreWidth = len(i.getGenres())

            searchresult = f"{"Title":<{titleWidth + 3}}{"Director":<{directorWidth + 3}}{"Actor":<{actorWidth + 3}}{"Genre":<{genreWidth + 3}}\n"
            for i in search:
                searchresult += f"{i.getTitle():<{titleWidth + 3}}{i.getDirectors():<{directorWidth + 3}}{i.getActors():<{actorWidth + 3}}{i.getGenres():<{genreWidth + 3}}\n"

            return searchresult

    def searchBooks(self, title="", author="", publisher=""):
        '''
        Get each one of the parameter to search the Books
        :return: A string containing all the related information
        '''
        search = set()   # avoid repeating
        titleWidth = 8
        authorWidth = 8
        publisherWidth = 11
        if title == "" and author == "" and publisher == "":
            tkinter.messagebox.showerror(title="Error", message=f"Please enter information for the Title, Author, and/or Publisher first!")
            return "No Results"
        else:
            # match the input parameter which are not ""
            for i in self.__books.values():
                if title in i.getTitle() and title != "":  # filter the ""
                    search.add(i)
                if author in i.getAuthors() and author != "":
                    search.add(i)
                if publisher in i.getPublisher() and publisher != "":
                    search.add(i)
            if len(search) == 0: return "No Results"   # if there is no related books
            for i in search:  # i -> <target object>
                if len(i.getTitle()) > titleWidth: titleWidth = len(i.getTitle())
                if len(i.getAuthors()) > authorWidth: authorWidth = len(i.getAuthors())
                if len(i.getPublisher()) > publisherWidth: publisherWidth = len(i.getPublisher())

            searchresult = f"{"Title":<{titleWidth + 3}}{"Author":<{authorWidth + 3}}{"Publisher":<{publisherWidth + 3}}\n"
            for i in search:
                searchresult += f"{i.getTitle():<{titleWidth + 3}}{i.getAuthors():<{authorWidth + 3}}{i.getPublisher():<{publisherWidth + 3}}\n"
            return searchresult

    def getRecommendations(self, type="", title=""):
        '''
        Find the associated information and then print out
        :return: A String containing associated information OR "No result"
        '''
        recommendInfo = ""
        if type in ["Movies", "TV Shows"]:
            #print("show!")
            for show in self.__shows.values():
                if title == show.getTitle():  # whether the title is existing
                    showId = show.getId()  # string: show id
                    #print("show id=", showId)
                    #print(self.__associations[showId].keys())
                    for i in self.__associations[showId].keys():  # i -> "book id"
                        recommendInfo += self.__books[i].__str__()  # books[i] -> object
                    return recommendInfo
            # title not exsit
            return "No result!"

        if type == "Books":
            #print("Book!")
            for book in self.__books.values():
                if title == book.getTitle():  # whether the title is existing
                    bookId = book.getId()  # string: book id
                    #print("book id=", bookId)
                    #print(self.__associations[bookId].keys())
                    for i in self.__associations[bookId].keys():  # i -> "show id"
                        recommendInfo += self.__shows[i].__str__()  # shows[i] -> object
                    return recommendInfo
            # title no exist
            return "No result!"

        else:   #if user do not select any combobox items
            return "No result!"

    def getMovieRatings(self):
        '''
        Calculate the rates of Movie and make them into a pie chart
        :return: A Figure
        '''
        rate = {}  # {"rate": 1}
        labels = []
        sizes = []
        for show in self.__shows.values():  # show -> <object>
            if show.getType() == "Movie":

                # Rating for movies
                if show.getShowRating() not in rate:
                    rate[show.getShowRating()] = 1
                else:
                    rate[show.getShowRating()] += 1

        for i in rate.keys():
            labels.append(i)
            sizes.append(rate[i])
            # print(labels)
            # print(sizes)

        fig = Figure(figsize=(3, 3))  # 3x3 inches
        plt = fig.add_subplot(111)
        # Plotting the pie chart
        plt.pie(sizes, labels=labels, autopct='%.2f%%', textprops={'fontsize': 7})

        return fig

    def getTVRatings(self):
        '''
        Calculate the rates of TV Shows and make them into a pie chart
        :return: A Figure
        '''
        rate = {}  # {"rate": 1}
        labels = []
        sizes = []
        for show in self.__shows.values():  # show -> <object>
            if show.getType() == "TV Show":

                # Rating for TV Show
                if show.getShowRating() not in rate:
                    rate[show.getShowRating()] = 1
                else:
                    rate[show.getShowRating()] += 1

        for i in rate.keys():
            labels.append(i)
            sizes.append(rate[i])
            # print(labels)
            # print(sizes)

        fig = Figure(figsize=(3, 3))  # 3x3 inches
        plt = fig.add_subplot(111)
        # Plotting the pie chart
        plt.pie(sizes, labels=labels, autopct='%.2f%%', textprops={'fontsize': 7})

        return fig

