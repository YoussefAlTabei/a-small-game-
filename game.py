from tkinter import  *
from tkinter import messagebox
def gamest():
    X.lift()
    X.state("normal")    
def bttn1():
    first.destroy()
    second.place(relx=.9, rely=.9, anchor="c")
def bttn2():
    second.destroy()
    third.place(relx=.9, rely=.1, anchor="c")
def bttn3():
    third.destroy()
    fourth.place(relx=.1, rely=.9, anchor="c")
def bttn4():
    fourth.destroy()
    fifth.place(relx=.5 , rely=.5 , anchor="c")
def finish():
    messagebox.showinfo('congrats', 'u have beatten the game')
    X.state("withdraw")
A=Tk()
A.state("withdraw")                                                                                                                      
##################################Game start codes##############################################
X=Toplevel(height =550 , width=550 , bg="dodgerblue" , cursor="dotbox" ,  bd=40 , relief="ridge")
X.title("game is on!")
X.minsize(500,500)
X.state("withdraw")
Y=Toplevel(height =550 , width=550 , bg="dodgerblue" , cursor="dotbox" ,  bd=40 , relief="ridge")
Y.title("welcome to the game")
gameint=Label(Y,text="welcome to my first game it's kinda dumb and won't take a lot of ur time ")
gameint.grid(column=0, row=0)
Y.minsize(500,500)
gamestart=Label(Y,text="to start press here --->")
gamestart.grid(column=0, row=2)
gamestbt= Button(Y, text="Start" , bg="aqua" , fg="black", activebackground="red" , command=gamest)
gamestbt.place(relx=.7, rely=.1, anchor="c")
#################################### In game btn ###############################################
first= Button(X,text="shoot me" , bg="aqua" , fg="black", activebackground="red" , command=bttn1)
first.place(relx=.1, rely=.1, anchor="c")
second= Button(X,text="shoot me" , bg="aqua" , fg="black", activebackground="red" , command=bttn2)
third= Button(X,text="shoot me" , bg="aqua" , fg="black", activebackground="red" , command=bttn3)
fourth= Button(X,text="shoot me" , bg="aqua" , fg="black", activebackground="red" , command=bttn4)
fifth= Button(X,text="finish" , bg="aqua" , fg="black", activebackground="red" , command=finish)
