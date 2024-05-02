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
        self.__Movie_upperText.configure(state='normal')
        self.__Movie_lowerText.configure(state='normal')

        self.__Movie_upperText.delete('1.0', tk.END)
        self.__Movie_lowerText.delete('1.0', tk.END)

        # call Rec py

        self.rec.loadShows()
        Movie_list = self.rec.getMovieList()
        Movie_stats = self.rec.getMovieStats()


        self.__Movie_upperText.insert(tk.END, Movie_list)
        self.__Movie_lowerText.insert(tk.END,Movie_stats)

        self.__Movie_upperText.configure(state='disabled')
        self.__Movie_lowerText.configure(state='disabled')

        #Refresh TV part
        self.__TV_upperText.configure(state='normal')
        self.__TV_lowerText.configure(state='normal')

        self.__TV_upperText.delete('1.0', tk.END)
        self.__TV_lowerText.delete('1.0', tk.END)

        # call Rec py
        TV_list = self.rec.getTVList()
        TV_stats = self.rec.getTVStats()

        self.__TV_upperText.insert(tk.END, TV_list)
        self.__TV_lowerText.insert(tk.END, TV_stats)

        self.__TV_upperText.configure(state='disabled')
        self.__TV_lowerText.configure(state='disabled')



        #load Bonus
        #movies frist
        if self.__MovieRatings_init_Label:
            self.__MovieRatings_init_Label.destroy()
        if self._RatingMovieCanvas_Indicator ==1:
            self.__MovieCanvas_frame.destroy()

        self.__MovieCanvas_frame = tk.Frame(self.__MovieRatings_Frame,width=750,height=300)
        self.__MovieCanvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        MoviePlot = self.rec.getMovieRatings()
        self.__MovieCanvas = FigureCanvasTkAgg(MoviePlot,master=self.__MovieCanvas_frame)
        self.__MovieCanvas.draw()
        self.__MovieCanvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.Y,expand=1)

        self._RatingMovieCanvas_Indicator = 1

        #TV
        if self.__TVRatings_init_Label:
            self.__TVRatings_init_Label.destroy()
        if self._RatingTVCanvas_Indicator ==1:
            self.__TVCanvas_frame.destroy()

        self.__TVCanvas_frame = tk.Frame(self.__TVRatings_Frame,width=750,height=300)
        self.__TVCanvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        TVPlot = self.rec.getTVRatings()
        self.__TVCanvas = FigureCanvasTkAgg(TVPlot,master=self.__TVCanvas_frame)
        self.__TVCanvas.draw()
        self.__TVCanvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.Y, expand=1)

        self._RatingTVCanvas_Indicator = 1

        return


    def loadBooks(self):
        #Calls the appropriate function from the Recommender object to read in all of the data for the books
        #Calls the appropriate function from the Recommender object to obtain the string representing the list of books and the string representing the book statistics and displays them in the appropriate text area

        self.__Book_upperText.configure(state='normal')
        self.__Book_lowerText.configure(state='normal')

        self.__Book_upperText.delete('1.0', tk.END)
        self.__Book_lowerText.delete('1.0', tk.END)

        # call Rec py
        self.rec.loadBooks()
        self.__Book_list = self.rec.getBookList()
        self.__Book_stats = self.rec.getBookStats()

        self.__Book_upperText.insert(tk.END, self.__Book_list)
        self.__Book_lowerText.insert(tk.END, self.__Book_stats)

        self.__Book_upperText.configure(state='disabled')
        self.__Book_lowerText.configure(state='disabled')


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
        self.__Search_Movies_TV_Text.configure(state='normal')
        self.__Search_Movies_TV_Text.delete('1.0', tk.END)

        # call Rec py

        #test
        print(self._cb_Movies_TV.get())
        print("debug01")


        Search_Shows_input = [self._cb_Movies_TV.get(),self._Movie_TV_Title_Entry.get(),self._Movie_TV_Director_Entry.get(),self._Movie_TV_Actor_Entry.get(),self._Movie_TV_Genre_Entry.get()]
        Search_Shows_output= self.rec.searchTVMovies(*Search_Shows_input)

        self.__Search_Movies_TV_Text.insert(tk.END, Search_Shows_output)

        self.__Search_Movies_TV_Text.configure(state='disabled')

        return

    def searchBooks(self):
        self.__Search_Books_Text.configure(state='normal')
        self.__Search_Books_Text.delete('1.0', tk.END)

        # call Rec py
        Search_Books_input = [self._Book_Title_Entry.get(),self._Book_Author_Entry.get(),self._Book_Publisher_Entry.get()]

        Search_Books_output = self.rec.searchBooks(*Search_Books_input)

        self.__Search_Books_Text.insert(tk.END, Search_Books_output)

        self.__Search_Books_Text.configure(state='disabled')


        return

    def getRecommendations(self):
        self.__Recommendations_Text.configure(state='normal')
        self.__Recommendations_Text.delete('1.0',tk.END)

        #call rec py
        Recommendations_input = [self._RecType_CB.get(),self._RecTitle_Entry.get()]
        Recommendations_output = self.rec.getRecommendations(*Recommendations_input)


        self.__Recommendations_Text.insert(tk.END, Recommendations_output)

        self.__Recommendations_Text.configure(state='disabled')






    def __init__(self):
        self.rec = rec.Recommender()

        self.__main_window = tk.Tk()
        self.__main_window.title("Recommender GUI")
        self.__main_window.geometry("1200x800")

        #editing the TOP 7-tab Notebook

        self.__Top_NB = ttk.Notebook(self.__main_window)
        self.__Top_NB.pack(side=tk.TOP,expand = 1, fill = tk.BOTH)


        self.__tab_Movies = ttk.Frame(self.__Top_NB)
        self.__Top_NB.add(self.__tab_Movies, text="Movies")

        self.__tab_TV_Shows = ttk.Frame(self.__Top_NB)
        self.__Top_NB.add(self.__tab_TV_Shows, text="TV Shows")

        self.__tab_Books = ttk.Frame(self.__Top_NB)
        self.__Top_NB.add(self.__tab_Books, text="Books")

        self.__tab_Search_Movies_TV = ttk.Frame(self.__Top_NB)
        self.__Top_NB.add(self.__tab_Search_Movies_TV, text="Search Movies/TV")

        self.__tab_Search_Books = ttk.Frame(self.__Top_NB)
        self.__Top_NB.add(self.__tab_Search_Books, text="Search Books")

        self.__tab_Recommendations = ttk.Frame(self.__Top_NB)
        self.__Top_NB.add(self.__tab_Recommendations, text="Recommendations")


        self.__tab_Ratings = ttk.Frame(self.__Top_NB)
        self.__Top_NB.add(self.__tab_Ratings, text="Ratings")


        #Editing 1 Movies Tab

        self.__Movie_upperText = tk.Text(self.__tab_Movies, width=1100,wrap=tk.WORD)
        self.__Movie_upperText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.__Movie_upperText.insert(tk.END, "Please click on \"LoadShows\"to start using")
        self.__Movie_upperText.configure(state=tk.DISABLED)

        self.__Movie_sp = ttk.Separator(self.__tab_Movies, orient=tk.HORIZONTAL)
        self.__Movie_sp.pack(fill=tk.X, pady=5)

        self.__Movie_lowerText = tk.Text(self.__tab_Movies, width=1100,wrap=tk.WORD)
        self.__Movie_lowerText.pack(side=tk.TOP, fill=tk.X,expand=True)
        self.__Movie_lowerText.insert(tk.END, "Please click on \"LoadShows\"to start using")
        self.__Movie_lowerText.configure(state=tk.DISABLED)



        #Editing 2 TV Shows Tab

        self.__TV_upperText = tk.Text(self.__tab_TV_Shows, width=1150, wrap=tk.WORD)
        self.__TV_upperText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.__TV_upperText.insert(tk.END, "Please click on \"LoadShows\"to start using")
        self.__TV_upperText.configure(state=tk.DISABLED)

        self.__TV_sp = ttk.Separator(self.__tab_TV_Shows, orient=tk.HORIZONTAL)
        self.__TV_sp.pack(fill=tk.X,pady=5)

        self.__TV_lowerText = tk.Text(self.__tab_TV_Shows, width=1150, wrap=tk.WORD)
        self.__TV_lowerText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.__TV_lowerText.insert(tk.END, "Please click on \"LoadShows\"to start using")
        self.__TV_lowerText.configure(state=tk.DISABLED)

        # Editing 3 Books Tab

        self.__Book_upperText = tk.Text(self.__tab_Books, width=1100, wrap=tk.WORD)
        self.__Book_upperText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.__Book_upperText.insert(tk.END, "Please click on \"LoadBooks\"to start using")
        self.__Book_upperText.configure(state=tk.DISABLED)

        self.__Book_sp = ttk.Separator(self.__tab_Books, orient=tk.HORIZONTAL)
        self.__Book_sp.pack(fill=tk.X, pady=5)

        self.__Book_lowerText = tk.Text(self.__tab_Books, width=1100, wrap=tk.WORD)
        self.__Book_lowerText.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.__Book_lowerText.insert(tk.END, "Please click on \"LoadBooks\"to start using")
        self.__Book_lowerText.configure(state=tk.DISABLED)







        # Editing Search 4th Movie/TV Interaction frame
        # with    "Search_Movies_TV_Inter_Frame"  and   "Search_Movies_TV_Text_Frame"
        #  "Search_Movies_TV_Inter_Frame"   has 6 lines with individual frames

        self.__Search_Movies_TV_Inter_Frame = ttk.Frame(self.__tab_Search_Movies_TV)

        self.__MovieLine1 = ttk.Frame(self.__Search_Movies_TV_Inter_Frame)
        self.__TypeLabel = ttk.Label(self.__MovieLine1, text="Type:")
        self.__TypeLabel.pack(side=tk.LEFT)
        self._options_cb_Movies_TV = ["Movies", "TV Shows"]
        self._cb_Movies_TV = ttk.Combobox(self.__MovieLine1, values=self._options_cb_Movies_TV)
        self._cb_Movies_TV.pack(side=tk.LEFT)
        self.__MovieLine1.pack(side=tk.TOP,fill=tk.X,expand=1)

        self.__MovieLine2 = ttk.Frame(self.__Search_Movies_TV_Inter_Frame)
        self.__MovieTitleLabel = ttk.Label(self.__MovieLine2, text="Title:")
        self.__MovieTitleLabel.pack(side=tk.LEFT)
        self._Movie_TV_Title_Entry = ttk.Entry(self.__MovieLine2)
        self._Movie_TV_Title_Entry.pack(side=tk.LEFT)
        self.__MovieLine2.pack(side=tk.TOP,fill=tk.X,expand=1)

        self.__MovieLine3 = ttk.Frame(self.__Search_Movies_TV_Inter_Frame)
        self.__MovieDirectorLabel = ttk.Label(self.__MovieLine3, text="Director:")
        self.__MovieDirectorLabel.pack(side=tk.LEFT)
        self._Movie_TV_Director_Entry = ttk.Entry(self.__MovieLine3)
        self._Movie_TV_Director_Entry.pack(side=tk.LEFT)
        self.__MovieLine3.pack(side=tk.TOP,fill=tk.X,expand=1)

        self.__MovieLine4 = ttk.Frame(self.__Search_Movies_TV_Inter_Frame)
        self.__MovieActorLabel = ttk.Label(self.__MovieLine4, text="Actor:")
        self.__MovieActorLabel.pack(side=tk.LEFT)
        self._Movie_TV_Actor_Entry = ttk.Entry(self.__MovieLine4)
        self._Movie_TV_Actor_Entry.pack(side=tk.LEFT)
        self.__MovieLine4.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__MovieLine5 = ttk.Frame(self.__Search_Movies_TV_Inter_Frame)
        self.__MovieGenreLabel = ttk.Label(self.__MovieLine5, text="Genre:")
        self.__MovieGenreLabel.pack(side=tk.LEFT)
        self._Movie_TV_Genre_Entry = ttk.Entry(self.__MovieLine5)
        self._Movie_TV_Genre_Entry.pack(side=tk.LEFT)
        self.__MovieLine5.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__MovieLine6 = ttk.Frame(self.__Search_Movies_TV_Inter_Frame)
        self.__MovieSearchButton = tk.Button(self.__MovieLine6, text="Search",command=self.searchShows)
        self.__MovieSearchButton.pack(side=tk.LEFT)
        self.__MovieLine6.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__Search_Movies_TV_Inter_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)



        self.__Search_Movies_TV_Text_Frame = tk.Frame(self.__tab_Search_Movies_TV)
        self.__Search_Movies_TV_Text_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__Search_Movies_TV_Text = tk.Text(self.__Search_Movies_TV_Text_Frame, width=1150, height=40, wrap=tk.WORD)
        self.__Search_Movies_TV_Text.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.__Search_Movies_TV_Text.insert(tk.END, "Search Movies test")
        self.__Search_Movies_TV_Text.configure(state=tk.DISABLED)




        # Editing 5th Search Books Interaction frame
        # "self.tab_Search_Books" has 2 sub Frames,    "self.Search_Books_Inter_Frame"  and   "self.Search_Books_Text_Frame"
        # "self.Search_Books_Inter_Frame"   has 4 lines with individual frames


        self.__Search_Books_Inter_Frame = tk.Frame(self.__tab_Search_Books)

        self.__BookLine1 = ttk.Frame(self.__Search_Books_Inter_Frame)
        self.__BooksTitleLabel = ttk.Label(self.__BookLine1, text="Title:")
        self.__BooksTitleLabel.pack(side=tk.LEFT)
        self._Book_Title_Entry = ttk.Entry(self.__BookLine1)
        self._Book_Title_Entry.pack(side=tk.LEFT)
        self.__BookLine1.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__BookLine2 = ttk.Frame(self.__Search_Books_Inter_Frame)
        self.__BooksAuthorLabel = ttk.Label(self.__BookLine2, text="Author:")
        self.__BooksAuthorLabel.pack(side=tk.LEFT)
        self._Book_Author_Entry = ttk.Entry(self.__BookLine2)
        self._Book_Author_Entry.pack(side=tk.LEFT)
        self.__BookLine2.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__BookLine3 = ttk.Frame(self.__Search_Books_Inter_Frame)
        self.__BooksPublisherLabel = ttk.Label(self.__BookLine3, text="Publisher:")
        self.__BooksPublisherLabel.pack(side=tk.LEFT)
        self._Book_Publisher_Entry = ttk.Entry(self.__BookLine3)
        self._Book_Publisher_Entry.pack(side=tk.LEFT)
        self.__BookLine3.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__BookLine4 = ttk.Frame(self.__Search_Books_Inter_Frame)
        self.__BookSearchButton = tk.Button(self.__BookLine4, text="Search", command=self.searchBooks)
        self.__BookSearchButton.pack(side=tk.LEFT)
        self.__BookLine4.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__Search_Books_Inter_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)



        self.__Search_Books_Text_Frame = tk.Frame(self.__tab_Search_Books)
        self.__Search_Books_Text_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__Search_Books_Text = tk.Text(self.__Search_Books_Text_Frame, width=1150, height=43, wrap=tk.WORD)
        self.__Search_Books_Text.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.__Search_Books_Text.insert(tk.END, "Search Books test")
        self.__Search_Books_Text.configure(state=tk.DISABLED)





        #Editing 6th Tab Recommendations
        #"self.tab_Recommendations" ha 2 sub Frames, "self.Recommendations_Inter_Frame"   and    "self.Recommendations_Text_Frame"
        #"self.Recommendations_Inter_Frame" has 3 line Frames

        self.__Recommendations_Inter_Frame = ttk.Frame(self.__tab_Recommendations,width=1150,height=150)
        self.__Recommendations_Inter_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.__Recommendations_Text_Frame = tk.Frame(self.__tab_Recommendations,width=1150,height=500)
        self.__Recommendations_Text_Frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.__RecLine1 = tk.Frame(self.__Recommendations_Inter_Frame)
        self.__RecType_label = tk.Label(self.__RecLine1, text="Type:")
        self.__RecType_label.pack(side=tk.LEFT)
        self._RecType_CB_options = ["Movies", "TV Shows", "Books"]
        self._RecType_CB = ttk.Combobox(self.__RecLine1, values=self._RecType_CB_options)
        self._RecType_CB.pack(side=tk.LEFT)
        self.__RecLine1.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__RecLine2 = tk.Frame(self.__Recommendations_Inter_Frame)
        self.__RecTitle_label = tk.Label(self.__RecLine2,text="Title:")
        self.__RecTitle_label.pack(side=tk.LEFT)
        self._RecTitle_Entry = tk.Entry(self.__RecLine2)
        self._RecTitle_Entry.pack(side=tk.LEFT)
        self.__RecLine2.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__RecLine3 = tk.Frame(self.__Recommendations_Inter_Frame)
        self.__RecSearch_Button = tk.Button(self.__RecLine3, text="Get Recommendation",command=self.getRecommendations)
        self.__RecSearch_Button.pack(side=tk.LEFT)
        self.__RecLine3.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__Recommendations_Text = tk.Text(self.__Recommendations_Text_Frame,height=45,wrap=tk.WORD)
        self.__Recommendations_Text.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.__Recommendations_Text.insert(tk.END,"Rec Test")
        self.__Recommendations_Text.configure(state=tk.DISABLED)


        self.__Recommendations_Text_Frame = tk.Frame(self.__tab_Recommendations,width=1150)
        self.__Recommendations_Text_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)




        #Editing Bonus
        #7th tab Ratings
        self.__MovieRatings_Frame = tk.Frame(self.__tab_Ratings,width=1150)
        self.__MovieRatings_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)
        self.__TVRatings_Frame = tk.Frame(self.__tab_Ratings,width=1150)
        self.__TVRatings_Frame.pack(side=tk.TOP, fill=tk.X, expand=1)

        self.__MovieRatings_Label = tk.Label(self.__MovieRatings_Frame, text="Movies Stats",font=(None,24))
        self.__MovieRatings_Label.config(width=15)
        self.__MovieRatings_Label.pack(side=tk.LEFT,fill=tk.Y,expand=1)
        self.__MovieRatings_init_Label = tk.Label(self.__MovieRatings_Frame, text="Movies not Loaded.\nClick LoadShows to show graph",font=(None,20))
        self.__MovieRatings_init_Label.pack(side=tk.LEFT,fill=tk.Y,expand=1)

        self.__TVRatings_Label = tk.Label(self.__TVRatings_Frame, text="TV Stats",font=(None,24))
        self.__TVRatings_Label.config(width=15)
        self.__TVRatings_Label.pack(side=tk.LEFT,fill=tk.Y,expand=1)
        self.__TVRatings_init_Label = tk.Label(self.__TVRatings_Frame, text="TV Not Loaded.\nClick LoadShows to show graph",font=(None, 20))
        self.__TVRatings_init_Label.pack(side=tk.LEFT,fill=tk.Y,expand=1)

        self._RatingMovieCanvas_Indicator = 0
        self._RatingTVCanvas_Indicator = 0






        #Editing Bottom Button Frame, including 5 Buttons
        self.__Bottom_Button_Frame = ttk.Frame(self.__main_window)
        self.__Bottom_Button_Frame.pack(side=tk.BOTTOM, fill=tk.X, expand=1,padx=150,pady=10)

        self.__Button_LoadShows=tk.Button(self.__Bottom_Button_Frame, text="Loadshows", command=self.loadShows)
        self.__Button_LoadShows.pack(side=tk.LEFT, padx=30, expand=1)

        self.__Button_LoadBooks=tk.Button(self.__Bottom_Button_Frame, text="LoadBooks", command=self.loadBooks)
        self.__Button_LoadBooks.pack(side=tk.LEFT, padx=30, expand=1)

        self.__Button_LoadRecommendations=tk.Button(self.__Bottom_Button_Frame, text="LoadRecommendations", command=self.loadAssociations)
        self.__Button_LoadRecommendations.pack(side=tk.LEFT, padx=30, expand=1)

        self.__Button_Information=tk.Button(self.__Bottom_Button_Frame, text="Information", command=self.creditInfoBox)
        self.__Button_Information.pack(side=tk.LEFT, padx=30, expand=1)

        self.__Botton_Quit=tk.Button(self.__Bottom_Button_Frame, text="Quit", command=quit)
        self.__Botton_Quit.pack(side=tk.LEFT, padx=30, expand=1)

        mainloop()





def main():

    RecommenderGUI()



if __name__ == "__main__":
    main()