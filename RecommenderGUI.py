import tkinter as tk
from tkinter import ttk, messagebox
import Recommender as rec
import tkinter.messagebox
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

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

        #Refresh Movie part first
        self.Movie_upperText.configure(state='normal')
        self.Movie_lowerText.configure(state='normal')

        self.Movie_upperText.delete('1.0', tk.END)
        self.Movie_lowerText.delete('1.0',tk.END)

        # call Rec py

        self.rec.loadShows()
        self.Movie_list = self.rec.getMovieList()
        self.Movie_stats = self.rec.getMovieStats()


        self.Movie_upperText.insert(tk.END, self.Movie_list)
        self.Movie_lowerText.insert(tk.END,self.Movie_stats)

        self.Movie_upperText.configure(state='disabled')
        self.Movie_lowerText.configure(state='disabled')

        #Refresh TV part
        self.TV_upperText.configure(state='normal')
        self.TV_lowerText.configure(state='normal')

        self.TV_upperText.delete('1.0', tk.END)
        self.TV_lowerText.delete('1.0', tk.END)

        # call Rec py
        self.TV_list = self.rec.getTVList()
        self.TV_stats = self.rec.getTVStats()

        self.TV_upperText.insert(tk.END, self.TV_list)
        self.TV_lowerText.insert(tk.END, self.TV_stats)

        self.TV_upperText.configure(state='disabled')
        self.TV_lowerText.configure(state='disabled')



        #load Bonus
        #movies frist
        if self.MovieRatings_init_Label:
            self.MovieRatings_init_Label.destroy()

        self.MovieCanvas_frame = tk.Frame(self.MovieRatings_Frame,width=750,height=300)
        self.MovieCanvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        self.MoviePlot = self.rec.getMovieRatings()
        self.MovieCanvas = FigureCanvasTkAgg(self.MoviePlot,master=self.MovieCanvas_frame)
        self.MovieCanvas.draw()
        self.MovieCanvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.Y,expand=1)

        #TV
        if self.TVRatings_init_Label:
            self.TVRatings_init_Label.destroy()

        self.TVCanvas_frame = tk.Frame(self.TVRatings_Frame,width=750,height=300)
        self.TVCanvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        self.TVPlot = self.rec.getTVRatings()
        self.TVCanvas = FigureCanvasTkAgg(self.TVPlot,master=self.TVCanvas_frame)
        self.TVCanvas.draw()
        self.TVCanvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.Y, expand=1)



        return


    def loadBooks(self):
        #Calls the appropriate function from the Recommender object to read in all of the data for the books
        #Calls the appropriate function from the Recommender object to obtain the string representing the list of books and the string representing the book statistics and displays them in the appropriate text area

        self.Book_upperText.configure(state='normal')
        self.Book_lowerText.configure(state='normal')

        self.Book_upperText.delete('1.0', tk.END)
        self.Book_lowerText.delete('1.0', tk.END)

        # call Rec py
        self.rec.loadBooks()
        self.Book_list = self.rec.getBookList()
        self.Book_stats = self.rec.getBookStats()

        self.Book_upperText.insert(tk.END, self.Book_list)
        self.Book_lowerText.insert(tk.END, self.Book_stats)

        self.Book_upperText.configure(state='disabled')
        self.Book_lowerText.configure(state='disabled')


        return

    def loadAssociations(self):
        #loadAssociations() function that takes in no parameters, returns nothing, and:
        #Calls the appropriate function from the Recommender object to read in all of the data for the associations


        self.rec.loadAssociations()
        return

    def creditInfoBox(self):
        messagebox.showinfo(title="Information", message="""Contributor Names: Yiwen Lin, Yulong Yang
        20240428 still working :)""")
        return

    def searchShows(self):
        self.Search_Movies_TV_Text.configure(state='normal')
        self.Search_Movies_TV_Text.delete('1.0', tk.END)

        # call Rec py
        self.Search_Shows_input = [self.cb_Movies_TV.get(),self.Movie_TV_Title_Entry.get(),self.Movie_TV_Director_Entry.get(),self.Movie_TV_Actor_Entry.get(),self.Movie_TV_Genre_Entry.get()]
        self.Search_Shows_output= self.rec.searchTVMovies(*self.Search_Shows_input)

        self.Search_Movies_TV_Text.insert(tk.END, self.Search_Shows_output)

        self.Search_Movies_TV_Text.configure(state='disabled')

        return

    def searchBooks(self):
        self.Search_Books_Text.configure(state='normal')
        self.Search_Books_Text.delete('1.0', tk.END)

        # call Rec py
        self.Search_Books_input = [self.Book_Title_Entry.get(),self.Book_Author_Entry.get(),self.Book_Publisher_Entry.get()]
        #a = self.Book_Title_Entry.get()
        self.Search_Books_output = self.rec.searchBooks(*self.Search_Books_input)

        self.Search_Books_Text.insert(tk.END, self.Search_Books_output)

        self.Search_Books_Text.configure(state='disabled')


        return

    def getRecommendations(self):
        self.Recommendations_Text.configure(state='normal')
        self.Recommendations_Text.delete('1.0',tk.END)

        #call rec py
        self.Recommendations_input = [self.RecType_CB.get(),self.RecTitle_Entry.get()]
        self.Recommendations_output = self.rec.getRecommendations(*self.Recommendations_input)


        self.Recommendations_Text.insert(tk.END, self.Recommendations_output)

        self.Recommendations_Text.configure(state='disabled')






    def __init__(self):
        self.rec = rec.Recommender()

        self.main_window = tk.Toplevel()
        self.main_window.title("Recommender GUI")
        self.main_window.geometry("1200x800")

        #editing the TOP 7-tab Notebook

        self.Top_NB = ttk.Notebook(self.main_window)
        self.Top_NB.pack(side=tk.TOP,expand = 1, fill = tk.BOTH)


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


        self.tab_Ratings = ttk.Frame(self.Top_NB)
        self.Top_NB.add(self.tab_Ratings, text="Ratings")


        #Editing 1 Movies Tab

        self.Movie_upperText = tk.Text(self.tab_Movies, width=1100,wrap=tk.WORD)
        self.Movie_upperText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.Movie_upperText.insert(tk.END, "Please click on \"LoadShows\"to start using")
        self.Movie_upperText.configure(state=tk.DISABLED)

        self.Movie_sp = ttk.Separator(self.tab_Movies, orient=tk.HORIZONTAL)
        self.Movie_sp.pack(fill=tk.X, pady=5)

        self.Movie_lowerText = tk.Text(self.tab_Movies, width=1100,wrap=tk.WORD)
        self.Movie_lowerText.pack(side=tk.TOP, fill=tk.X,expand=True)
        self.Movie_lowerText.insert(tk.END, "Please click on \"LoadShows\"to start using")
        self.Movie_lowerText.configure(state=tk.DISABLED)



        #Editing 2 TV Shows Tab

        self.TV_upperText = tk.Text(self.tab_TV_Shows, width=1150, wrap=tk.WORD)
        self.TV_upperText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.TV_upperText.insert(tk.END, "Please click on \"LoadShows\"to start using")
        self.TV_upperText.configure(state=tk.DISABLED)

        self.TV_sp = ttk.Separator(self.tab_TV_Shows, orient=tk.HORIZONTAL)
        self.TV_sp.pack(fill=tk.X,pady=5)

        self.TV_lowerText = tk.Text(self.tab_TV_Shows, width=1150, wrap=tk.WORD)
        self.TV_lowerText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.TV_lowerText.insert(tk.END, "Please click on \"LoadShows\"to start using")
        self.TV_lowerText.configure(state=tk.DISABLED)

        # Editing 3 Books Tab

        self.Book_upperText = tk.Text(self.tab_Books, width=1100, wrap=tk.WORD)
        self.Book_upperText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.Book_upperText.insert(tk.END, "Please click on \"LoadBooks\"to start using")
        self.Book_upperText.configure(state=tk.DISABLED)

        self.Book_sp = ttk.Separator(self.tab_Books, orient=tk.HORIZONTAL)
        self.Book_sp.pack(fill=tk.X, pady=5)

        self.Book_lowerText = tk.Text(self.tab_Books, width=1100, wrap=tk.WORD)
        self.Book_lowerText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.Book_lowerText.insert(tk.END, "Please click on \"LoadBooks\"to start using")
        self.Book_lowerText.configure(state=tk.DISABLED)







        # Editing Search 4th Movie/TV Interaction frame
        # with    "Search_Movies_TV_Inter_Frame"  and   "Search_Movies_TV_Text_Frame"
        #  "Search_Movies_TV_Inter_Frame"   has 6 lines with individual frames

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

        self.Search_Movies_TV_Inter_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)



        self.Search_Movies_TV_Text_Frame = tk.Frame(self.tab_Search_Movies_TV)
        self.Search_Movies_TV_Text_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.Search_Movies_TV_Text = tk.Text(self.Search_Movies_TV_Text_Frame, width=1150, height=40, wrap=tk.WORD)
        self.Search_Movies_TV_Text.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.Search_Movies_TV_Text.insert(tk.END, "Search Movies test")
        self.Search_Movies_TV_Text.configure(state=tk.DISABLED)




        # Editing 5th Search Books Interaction frame
        # "self.tab_Search_Books" has 2 sub Frames,    "self.Search_Books_Inter_Frame"  and   "self.Search_Books_Text_Frame"
        # "self.Search_Books_Inter_Frame"   has 4 lines with individual frames


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

        self.Search_Books_Inter_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)



        self.Search_Books_Text_Frame = tk.Frame(self.tab_Search_Books)
        self.Search_Books_Text_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.Search_Books_Text = tk.Text(self.Search_Books_Text_Frame, width=1150, height=43, wrap=tk.WORD)
        self.Search_Books_Text.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.Search_Books_Text.insert(tk.END, "Search Books test")
        self.Search_Books_Text.configure(state=tk.DISABLED)





        #Editing 6th Tab Recommendations
        #"self.tab_Recommendations" ha 2 sub Frames, "self.Recommendations_Inter_Frame"   and    "self.Recommendations_Text_Frame"
        #"self.Recommendations_Inter_Frame" has 3 line Frames

        self.Recommendations_Inter_Frame = ttk.Frame(self.tab_Recommendations,width=1150,height=150)
        self.Recommendations_Inter_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.Recommendations_Text_Frame = tk.Frame(self.tab_Recommendations,width=1150,height=500)
        self.Recommendations_Text_Frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.RecLine1 = tk.Frame(self.Recommendations_Inter_Frame)
        self.RecType_label = tk.Label(self.RecLine1, text="Type:")
        self.RecType_label.pack(side=tk.LEFT)
        self.RecType_CB_options = ["Movies", "TV Shows", "Books"]
        self.RecType_CB = ttk.Combobox(self.RecLine1, values=self.RecType_CB_options)
        self.RecType_CB.pack(side=tk.LEFT)
        self.RecLine1.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.RecLine2 = tk.Frame(self.Recommendations_Inter_Frame)
        self.RecTitle_label = tk.Label(self.RecLine2,text="Title:")
        self.RecTitle_label.pack(side=tk.LEFT)
        self.RecTitle_Entry = tk.Entry(self.RecLine2)
        self.RecTitle_Entry.pack(side=tk.LEFT)
        self.RecLine2.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.RecLine3 = tk.Frame(self.Recommendations_Inter_Frame)
        self.RecSearch_Button = tk.Button(self.RecLine3, text="Get Recommendation",command=self.getRecommendations)
        self.RecSearch_Button.pack(side=tk.LEFT)
        self.RecLine3.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.Recommendations_Text = tk.Text(self.Recommendations_Text_Frame,height=45,wrap=tk.WORD)
        self.Recommendations_Text.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.Recommendations_Text.insert(tk.END,"Rec Test")
        self.Recommendations_Text.configure(state=tk.DISABLED)


        self.Recommendations_Text_Frame = tk.Frame(self.tab_Recommendations,width=1150)
        self.Recommendations_Text_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)




        #Editing Bonus
        #7th tab Ratings
        self.MovieRatings_Frame = tk.Frame(self.tab_Ratings,width=1150)
        self.MovieRatings_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.TVRatings_Frame = tk.Frame(self.tab_Ratings,width=1150)
        self.TVRatings_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.MovieRatings_Label = tk.Label(self.MovieRatings_Frame, text="Movies Stats",font=(None,24))
        self.MovieRatings_Label.config(width=15)
        self.MovieRatings_Label.pack(side=tk.LEFT,fill=tk.Y,expand=1)
        self.MovieRatings_init_Label = tk.Label(self.MovieRatings_Frame, text="Movies not Loaded.\nClick LoadShows to show graph",font=(None,20))
        self.MovieRatings_init_Label.pack(side=tk.LEFT,fill=tk.Y,expand=1)

        self.TVRatings_Label = tk.Label(self.TVRatings_Frame, text="TV Stats",font=(None,24))
        self.TVRatings_Label.config(width=15)
        self.TVRatings_Label.pack(side=tk.LEFT,fill=tk.Y,expand=1)
        self.TVRatings_init_Label = tk.Label(self.TVRatings_Frame, text="TV Not Loaded.\nClick LoadShows to show graph",font=(None, 20))
        self.TVRatings_init_Label.pack(side=tk.LEFT,fill=tk.Y,expand=1)






        #Editing Bottom Button Frame, including 5 Buttons
        self.Bottom_Button_Frame = ttk.Frame(self.main_window)
        self.Bottom_Button_Frame.pack(side=tk.BOTTOM, fill=tk.X, expand=1,padx=150,pady=10)

        self.Button_LoadShows=tk.Button(self.Bottom_Button_Frame, text="Loadshows", command=self.loadShows)
        self.Button_LoadShows.pack(side=tk.LEFT, padx=30, expand=1)

        self.Button_LoadBooks=tk.Button(self.Bottom_Button_Frame, text="LoadBooks", command=self.loadBooks)
        self.Button_LoadBooks.pack(side=tk.LEFT, padx=30, expand=1)

        self.Button_LoadRecommendations=tk.Button(self.Bottom_Button_Frame, text="LoadRecommendations", command=self.loadAssociations)
        self.Button_LoadRecommendations.pack(side=tk.LEFT, padx=30, expand=1)

        self.Button_Information=tk.Button(self.Bottom_Button_Frame, text="Information", command=self.creditInfoBox)
        self.Button_Information.pack(side=tk.LEFT, padx=30, expand=1)

        self.Botton_Quit=tk.Button(self.Bottom_Button_Frame, text="Quit", command=quit)
        self.Botton_Quit.pack(side=tk.LEFT, padx=30, expand=1)



def main():
    root = tk.Tk()
    root.withdraw()
    app = RecommenderGUI()
    root.mainloop()


if __name__ == "__main__":
    main()