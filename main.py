from tkinter import *
operador = ""
root = Tk()
root.geometry("1000x500+0+0")
root.title("Dojo Python")

text_input = StringVar()

Tops = Frame(root,
    width=1600,
    height = 80,
    bg = "powder blue",
    relief=SUNKEN)
Tops.pack(side = TOP)

frame = Frame(root,
    width=300,
    height = 700,
    bg = "powder blue",
    relief=SUNKEN)
frame.pack(side = TOP)

lblinfo = Label(
    Tops,
    font=("SHOWCARD GOTHIC", 50, 'bold'),
    text= "dojo python")
lblinfo.grid(row=0,column=0)

def btnClick(numero):
    global operador
    operador = operador+str(numero)
    text_input.set(operador)

def btnEval():
    global operador
    result = str(eval(operador))
    text_input.set(result)
    operador = ""

txtDisplay = Entry(frame,
    font=("SHOWCARD GOTHIC", 50, 'bold'),
    textvariable=text_input, bg = "black")

txtDisplay.grid(columnspan = 4)

btn1 = Button(
    frame,
    font=("SHOWCARD GOTHIC", 50, 'bold'),
    command = lambda:btnClick(1)).grid(row=2,column=0)
btn2 = Button(
    frame,
    font=("SHOWCARD GOTHIC", 50, 'bold'),
    command = lambda:btnClick(2)).grid(row=2,column=1)
Addition = Button(
    frame,
    font=("SHOWCARD GOTHIC", 50, 'bold'),
    command = lambda:btnClick('+')).grid(row=2,column=3)
Equals = Button(
    frame,
    font=("SHOWCARD GOTHIC", 50, 'bold'),
    command = lambda:btnEval()).grid(row=3,column=0)

root.mainloop()
