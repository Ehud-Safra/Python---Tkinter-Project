from tkinter import *
import tkinter.messagebox



win = Tk()
win.title("Login 4")
win.geometry("400x250")

# define click function for login button
def myclick():

    greeting_user = "Hello " + user_entry.get()
    my_label = Label(win, text=greeting_user)
    my_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    

# make user name label
user_label = Label(win, text="User Name")
user_label.grid(column=0, row=0)
# make user name input box
user_entry = Entry(win, width=10)
user_entry.grid(column=1, row=0)

# make password label
password_label = Label(win, text="Password")
password_label.grid(column=0, row=1, sticky=W)
# make password input box
password_entry = Entry(win, width=10)
password_entry.grid(column=1, row=1)

# make login button and place it in the window
logIn_Button = Button(win, text="Login", command=myclick)
logIn_Button.place(relx=0.5, rely=0.5, anchor=CENTER)


win.mainloop()