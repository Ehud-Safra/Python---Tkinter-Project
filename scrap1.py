from tkinter import *
import tkinter.messagebox
import requests
from bs4 import BeautifulSoup

URL = 'https://mail.google.com/mail/u/1/#inbox'
page = requests.get(URL)



win = Tk()
win.title("Scrap Me")
win.geometry("400x300")

# define click function for search button
def myclick():

    show_text = "Searching " + search_entry.get()
    my_label = Label(win, text=show_text)
    my_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    

# make search label
search_label = Label(win, text="Search Text")
search_label.place(relx=0.5, anchor = N)

# make text input box
search_entry = Entry(win, width=50)
search_entry.place(relx=0.5, rely=0.1, anchor=CENTER)



# make search button and place it in the window
search_Button = Button(win, text="Search", command=myclick)
search_Button.pack(side= BOTTOM)


win.mainloop()
