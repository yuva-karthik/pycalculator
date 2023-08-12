from tkinter import *

#window setup
win = Tk()
win.title("CALCULATOR")
win.geometry("373x438")
win.resizable(False,False)
win.configure(bg="#292e2b")

#image
logo = PhotoImage(file = "calculatorlogo.png")
win.iconphoto(False, logo)

#workspace
l_space = Label(win,
                background="#bfc9c2",
                width=380,
                height=2,
                text="",
                font=('impress',30))

#functions
equation = ""
def display(thing):
    global equation
    equation += thing
    l_space.config(text=equation)

def sweep():
    global equation
    equation = ""
    l_space.config(text=equation)

def operation():
    global result
    global equation
    result = ""
    if equation != "":
       try:
        result = eval(equation)
        result = str(result)
       except:
        result = "ERROR"
        equation = ""
    l_space.config(text=result)   

#buttons
Button(win,
       text="clear",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: sweep()).place(x=0,y=100)

Button(win,
       text="X",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("*")).place(x=100,y=100)

Button(win,
       text="/",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("/")).place(x=200,y=100)

Button(win,
       text="^",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("**")).place(x=300,y=100)

Button(win,
       text="7",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("7")).place(x=0,y=170)

Button(win,
       text="8",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("8")).place(x=100,y=170)

Button(win,
       text="9",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("9")).place(x=200,y=170)

Button(win,
       text="+",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("+")).place(x=300,y=170)

Button(win,
       text="4",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("4")).place(x=0,y=240)

Button(win,
       text="5",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("5")).place(x=100,y=240)

Button(win,
       text="6",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("6")).place(x=200,y=240)

Button(win,
       text="-",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("-")).place(x=300,y=240)

Button(win,
       text="1",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("1")).place(x=0,y=310)

Button(win,
       text="2",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("2")).place(x=100,y=310)

Button(win,
       text="3",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("3")).place(x=200,y=310)

Button(win,
       text=".",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display(".")).place(x=0,y=380)

Button(win,
       text="0",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("0")).place(x=100,y=380)

Button(win,
       text="00",
       width=4,
       height=1,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: display("00")).place(x=200,y=380)

Button(win,
       text="=",
       width=4,
       height=3,
       font=('impress',20),
       bg="#050505",
       fg="#990505",
       relief="raised",
       activebackground="#4287f5",
       command=lambda: operation()).place(x=300,y=315)
#pack
l_space.pack()
win.mainloop()

###<--- --->###