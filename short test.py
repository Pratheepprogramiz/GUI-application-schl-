from tkinter import *

w_log = Tk()
w_log.title("LOGIN")
w_log.geometry("435x230")
l_logemail= Label(w_log,text="Email ID: ",font=("Helvetica",13))
l_logpass = Label(w_log,text="Password: ",font=("Helvetica",13))
e_logemail= Entry(w_log,font=("Helvetica",13),borderwidth=4,width=30)
e_logpass = Entry(w_log,font=("Helvetica",13),borderwidth=4,width=30)
l_logemail.place(x=180,y=10)
e_logemail.place(x=80,y=33)
l_logpass.place(x=180,y=90)
e_logpass.place(x=80,y=113)
b_log = Button(w_log,text="SIGN-IN",font=("helvetica",13),bg="blue",fg="white",width=10)
b_log.place(x=170,y=170)
w_log.mainloop()