from Media import Media
# self, id, type, title, directors, actors, averageRating, country, date, year, showRating, duration, genres, description
class Show(Media):
    def __init__(self, id, type, title, directors, actors, averageRating, country, date, year, showRating, duration, genres, description):
        Media.__init__(self, id, title, averageRating)
        self.__type = type
        self.__directors = directors
        self.__actors = actors
        self.__country = country
        self.__date = date
        self.__year = year
        self.__showRating = showRating
        self.__duration = duration
        self.__genres = genres
        self.__description = description

        # Getter
    def getType(self):
        return self.__type

    def getDirectors(self):
        return self.__directors

    def getActors(self):
        return self.__actors

    def getCountry(self):
        return self.__country

    def getDate(self):
        return self.__date

    def getYear(self):
        return self.__year

    def getShowRating(self):
        return self.__showRating

    def getDuration(self):
        return self.__duration

    def getGenres(self):
        return self.__genres

    def getDescription(self):
        return self.__description

    # Setter
    def setType(self, newType):
        return self.__type

    def setDirectors(self, newDirectors):
        self.__directors = newDirectors

    def setActors(self, newActors):
        self.__actors = newActors

    def setCountry(self, newCountry):
        self.__country = newCountry

    def setDate(self, newDate):
        self.__date = newDate

    def setYear(self, newYear):
        self.__year = newYear

    def setShowRating(self, newShowRating):
        self.__showRating = newShowRating

    def setDuration(self, newDuration):
        self.__duration = newDuration

    def setGenres(self, newGenres):
        self.__genres = newGenres

    def setDescription(self, newDescription):
        self.__description = newDescription

    def __str__(self):
        return (f"Type:\n{self.__type}\n"
                f"Title:\n{self._title}\n"
                f"Director:\n{self.__directors}\n"
                f"Actor:\n{self.__directors}\n"
                f"Average Rating:\n{self._averageRating}\n"
                f"Country:\n{self.__country}\n"
                f"Publication Date:\n{self.__date}\n"
                f"Release Year::\n{self.__year}\n"
                f"Rating Count:\n{self.__showRating}\n"
                f"Duration:\n{self.__duration}\n"
                f"Genre:\n{self.__genres}\n"
                f"Description:\n{self.__description}\n"
                f"\n\n****************************************************\n\n")


