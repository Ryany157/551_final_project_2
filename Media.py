class Media:
    def __init__(self, id, title, averageRating):
        self._id = id
        self._title = title
        self._averageRating = averageRating

    # Getter
    def getId(self):
        return self._id

    def getTitle(self):
        return self._title

    def getAverageRating(self):
        return self._averageRating

    # Setter
    def setId(self, newId):
        self._id = newId

    def setTitle(self, newTitle):
        self._title = newTitle

    def setAverageRating(self, newAverageRating):
        self._averageRating = newAverageRating
