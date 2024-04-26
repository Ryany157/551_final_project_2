import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.messagebox

class RecommenderGUI:

    def loadShows(self):
        # call Recommender.Calls the appropriate function from the Recommender object to read in all of the data
        # for the shows
        # ▪ Calls the appropriate function from the Recommender object to obtain the string
        # representing the list of movies and the string representing the movie statistics and
        # displays them in the appropriate text area
        # ▪ Calls the appropriate function from the Recommender object to obtain the string
        # representing the list of tv shows and the string representing the tv show statistics and
        # displays them in the appropriate text area

        return


    def loadBook(self):
        #Calls the appropriate function from the Recommender object to read in all of the data for the books
        #Calls the appropriate function from the Recommender object to obtain the string representing the list of books and the string representing the book statistics and displays them in the appropriate text area
        return

    def loadAssociations(self):
        #loadAssociations() function that takes in no parameters, returns nothing, and:
        #Calls the appropriate function from the Recommender object to read in all of the data for the associations
        #
        return

    def creditInfoBox(self):
        messagebox.showinfo(title="Infomation", message="""Contributor Names: Yiwen Lin, Yulong Yang
        20240425 still working :)""")
        return

    def searchShows(self):
        return

    def searchBooks(self):
        return






    def __init__(self):
        self.main_window = tk.Toplevel()
        self.main_window.title("Recommender GUI")
        self.main_window.geometry("1200x800")

        self.Top_NB = ttk.Notebook(self.main_window)
        self.Top_NB.pack(side=tk.TOP,expand = 1, fill = tk.X,padx = 10)


        self.tab_Movies = ttk.Frame(self.Top_NB)
        self.Top_NB.add(self.tab_Movies, text="Movies")

        self.tab_TV_Shows = ttk.Frame(self.Top_NB)
        self.Top_NB.add(self.tab_TV_Shows, text="TV Shows")

        self.tab_Books = ttk.Frame(self.Top_NB)
        self.Top_NB.add(self.tab_Books, text="Books")

        self.tab_Search_Movies_TV = ttk.Frame(self.Top_NB)
        self.Top_NB.add(self.tab_Search_Movies_TV, text="Search Movies/TV")

        self.tab_Search_Books = ttk.Frame(self.Top_NB)
        self.Top_NB.add(self.tab_Search_Books, text="Search Books")

        self.tab_Recommendations = ttk.Frame(self.Top_NB)
        self.Top_NB.add(self.tab_Recommendations, text="Recommendations")
        self.options_cb_Recommendations = ["Movies","TV Shows","Books"]
        self.cb_Recommandations = ttk.Combobox(self.tab_Recommendations,values=self.options_cb_Recommendations)
        self.cb_Recommandations.pack()

        #Editing Search Movie/TV Interaction frame
        #6 lines with individual frames

        self.Search_Movies_TV_Inter_Frame = ttk.Frame(self.tab_Search_Movies_TV)

        self.MovieLine1 = ttk.Frame(self.Search_Movies_TV_Inter_Frame)
        self.TypeLabel = ttk.Label(self.MovieLine1, text="Type:")
        self.TypeLabel.pack(side=tk.LEFT)
        self.options_cb_Movies_TV = ["Movies", "TV Shows"]
        self.cb_Movies_TV = ttk.Combobox(self.MovieLine1, values=self.options_cb_Movies_TV,)
        self.cb_Movies_TV.pack(side=tk.LEFT)
        self.MovieLine1.pack(side=tk.TOP,fill=tk.X,expand=1)

        self.MovieLine2 = ttk.Frame(self.Search_Movies_TV_Inter_Frame)
        self.MovieTitleLabel = ttk.Label(self.MovieLine2, text="Title:")
        self.MovieTitleLabel.pack(side=tk.LEFT)
        self.Movie_TV_Title_Entry = ttk.Entry(self.MovieLine2)
        self.Movie_TV_Title_Entry.pack(side=tk.LEFT)
        self.MovieLine2.pack(side=tk.TOP,fill=tk.X,expand=1)

        self.MovieLine3 = ttk.Frame(self.Search_Movies_TV_Inter_Frame)
        self.MovieDirectorLabel = ttk.Label(self.MovieLine3, text="Director:")
        self.MovieDirectorLabel.pack(side=tk.LEFT)
        self.Movie_TV_Director_Entry = ttk.Entry(self.MovieLine3)
        self.Movie_TV_Director_Entry.pack(side=tk.LEFT)
        self.MovieLine3.pack(side=tk.TOP,fill=tk.X,expand=1)

        self.MovieLine4 = ttk.Frame(self.Search_Movies_TV_Inter_Frame)
        self.MovieActorLabel = ttk.Label(self.MovieLine4, text="Actor:")
        self.MovieActorLabel.pack(side=tk.LEFT)
        self.Movie_TV_Actor_Entry = ttk.Entry(self.MovieLine4)
        self.Movie_TV_Actor_Entry.pack(side=tk.LEFT)
        self.MovieLine4.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.MovieLine5 = ttk.Frame(self.Search_Movies_TV_Inter_Frame)
        self.MovieGenreLabel = ttk.Label(self.MovieLine5, text="Genre:")
        self.MovieGenreLabel.pack(side=tk.LEFT)
        self.Movie_TV_Genre_Entry = ttk.Entry(self.MovieLine5)
        self.Movie_TV_Genre_Entry.pack(side=tk.LEFT)
        self.MovieLine5.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.MovieLine6 = ttk.Frame(self.Search_Movies_TV_Inter_Frame)
        self.MovieSearchButton = tk.Button(self.MovieLine6, text="Search",command=self.searchShows)
        self.MovieSearchButton.pack(side=tk.LEFT)
        self.MovieLine6.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.Search_Movies_TV_Inter_Frame.pack()

        # Editing Search Books Interaction frame
        # 4 lines with individual frames
        self.Search_Books_Inter_Frame = tk.Frame(self.tab_Search_Books)

        self.BookLine1 = ttk.Frame(self.Search_Books_Inter_Frame)
        self.BooksTitleLabel = ttk.Label(self.BookLine1, text="Title:")
        self.BooksTitleLabel.pack(side=tk.LEFT)
        self.Book_Title_Entry = ttk.Entry(self.BookLine1)
        self.Book_Title_Entry.pack(side=tk.LEFT)
        self.BookLine1.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.BookLine2 = ttk.Frame(self.Search_Books_Inter_Frame)
        self.BooksAuthorLabel = ttk.Label(self.BookLine2, text="Author:")
        self.BooksAuthorLabel.pack(side=tk.LEFT)
        self.Book_Author_Entry = ttk.Entry(self.BookLine2)
        self.Book_Author_Entry.pack(side=tk.LEFT)
        self.BookLine2.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.BookLine3 = ttk.Frame(self.Search_Books_Inter_Frame)
        self.BooksPublisherLabel = ttk.Label(self.BookLine3, text="Publisher:")
        self.BooksPublisherLabel.pack(side=tk.LEFT)
        self.Book_Publisher_Entry = ttk.Entry(self.BookLine3)
        self.Book_Publisher_Entry.pack(side=tk.LEFT)
        self.BookLine3.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.BookLine4 = ttk.Frame(self.Search_Books_Inter_Frame)
        self.BookSearchButton = tk.Button(self.BookLine4, text="Search", command=self.searchBooks)
        self.BookSearchButton.pack(side=tk.LEFT)
        self.BookLine4.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.Search_Books_Inter_Frame.pack()



        #Editing Bottom Button Frame, including 5 Buttons
        self.Bottom_Button_Frame = ttk.Frame(self.main_window)
        self.Bottom_Button_Frame.pack(side=tk.BOTTOM, fill=tk.X, expand=1,padx=150,pady=10)

        self.Button_LoadShows=tk.Button(self.Bottom_Button_Frame, text="Loadshows", command=None)
        self.Button_LoadShows.pack(side=tk.LEFT, padx=30)

        self.Button_LoadBooks=tk.Button(self.Bottom_Button_Frame, text="LoadBooks", command=None)
        self.Button_LoadBooks.pack(side=tk.LEFT, padx=30)

        self.Button_LoadRecommendations=tk.Button(self.Bottom_Button_Frame, text="LoadRecommendations", command=None)
        self.Button_LoadRecommendations.pack(side=tk.LEFT, padx=30)

        self.Button_Information=tk.Button(self.Bottom_Button_Frame, text="Information", command=self.creditInfoBox)
        self.Button_Information.pack(side=tk.LEFT, padx=30)

        self.Botton_Quit=tk.Button(self.Bottom_Button_Frame, text="Quit", command=quit)
        self.Botton_Quit.pack(side=tk.LEFT, padx=30)
















def main():
    root = tk.Tk()
    root.withdraw()
    app = RecommenderGUI()
    root.mainloop()


if __name__ == "__main__":
    main()