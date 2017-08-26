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

root.mainloop()
