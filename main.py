from tkinter import *
from tkinter import ttk, messagebox
import turtle



root = Tk()
root.geometry('800x800')

turtle_area = Canvas(root,height = 500, width= 800 , bg= "red", cursor='dot')

#asterix shape creation
def _create_asterix():
    shape.width(10)
    for i in range(8):
        if i ==1 or i==3:
            shape.left(45)
            pass
        else:
            shape.fd(100)
            shape.bk(100)
            shape.left(45)



turtle_area.pack()
shape = turtle.RawTurtle(turtle_area)

_create_asterix()



root.mainloop()
