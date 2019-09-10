from tkinter import*

top = Tk()
top.title("calculator")
top.geometry("180x230")
top.resizable(0,0)
top.wm_attributes("-topmost",1)

# Label
Label1 = Label(top, text="calculator app")
Label1.grid(row=0,columnspan=6)

#variables
equa = ""
equation = StringVar()
calculation = Label(top, textvariable = equation)
equation.set("Enter your expression : ")

calculation.grid(row=2, columnspan=6)

def btnpress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)

def Equalpress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""

def Clearpress():
    global equa
    equa = ""
    equation.set("")

Button0 = Button(top, text="0", command = lambda:btnpress(0),
borderwidth=1, relief=SOLID)
Button0.grid(row = 6, column = 2, padx=10, pady=10)

Button1 = Button(top, text="1", command = lambda:btnpress(1),
borderwidth=1,relief=SOLID)
Button1.grid(row = 3, column = 1, padx=10, pady=10)

Button2 = Button(top, text="2", command = lambda:btnpress(2),
borderwidth=1,relief=SOLID)
Button2.grid(row = 3, column = 2, padx=10, pady=10)

Button3 = Button(top, text="3", command = lambda:btnpress(3),
borderwidth=1,relief=SOLID)
Button3.grid(row = 3, column = 3, padx=10, pady=10)

Button4 = Button(top, text="4", command = lambda:btnpress(4),
borderwidth=1,relief=SOLID)
Button4.grid(row = 4, column = 1, padx=10, pady=10)

Button5 = Button(top, text="5", command = lambda:btnpress(5),
borderwidth=1,relief=SOLID)
Button5.grid(row = 4, column = 2, padx=10, pady=10)

Button6 = Button(top, text="6", command = lambda:btnpress(6),
borderwidth=1,relief=SOLID)
Button6.grid(row = 4, column = 3, padx=10, pady=10)

Button7 = Button(top, text="7", command = lambda:btnpress(7),
borderwidth=1,relief=SOLID)
Button7.grid(row = 5, column = 1, padx=10, pady=10)

Button8 = Button(top, text="8", command = lambda:btnpress(8),
borderwidth=1,relief=SOLID)
Button8.grid(row = 5, column = 2, padx=10, pady=10)

Button9 = Button(top, text="9", command = lambda:btnpress(9),
borderwidth=1,relief=SOLID)
Button9.grid(row = 5, column = 3, padx=10, pady=10)

Plus = Button(top,text="+",command = lambda:btnpress("+"),
borderwidth=1, relief=SOLID)
Plus.grid(row = 3, column = 4, padx=10, pady=10)

minus = Button(top, text="-",command= lambda:btnpress("-"),
borderwidth=1, relief=SOLID)
minus.grid(row = 4, column = 4,padx=10,pady=10)

Multiple = Button(top, text="*",command= lambda:btnpress("*"),
borderwidth=1, relief=SOLID)
Multiple.grid(row = 5, column = 4,padx=10,pady=10)

Divid = Button(top, text="/",command= lambda:btnpress("/"),
borderwidth=1, relief=SOLID)
Divid.grid(row = 6, column = 4,padx=10,pady=10)

Equal = Button(top, text="=",command = Equalpress,
borderwidth=1, relief=SOLID)
Equal.grid(row = 6, column = 3, padx=10, pady=10)

Clear = Button(top, text="C",command = Clearpress,
borderwidth=1, relief=SOLID)
Clear.grid(row = 6, column = 1, padx=10, pady=10)


top.mainloop()




               
               




    
