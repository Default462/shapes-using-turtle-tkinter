from tkinter import *
from tkinter import ttk, messagebox
import turtle



root = Tk()
root.geometry('800x800')

turtle_area = Canvas(root,height = 500, width= 800 , bg= "red", cursor='dot')

#asterix shape creation
def _create_asterix():

    for i in range(8):
        if i ==1 or i==3:
            shape.left(45)
            pass
        else:
            shape.fd(100)
            shape.bk(100)
            shape.left(45)
def _A():
    shape.left(90)
    shape.fd(200)
    shape.bk(100)
    shape.right(90)
    shape.fd(100)
    shape.left(90)
    shape.fd(100)
    shape.bk(200)

def _B():
    shape.circle(100,180)
    shape.left(90)
    shape.fd(400)
    shape.left(90)
    shape.circle(100,180)

def _C():

    shape.pu()
    shape.sety(200)
    shape.pd()
    shape.left(180)
    shape.circle(200,180)


def _D():
    shape.pu()
    shape.setpos(x=-100,y=200)
    shape.pd()
    shape.left(270)
    shape.fd(400)
    shape.left(90)
    shape.circle(200,180)

def _E():
    pass

turtle_area.pack()
shape = turtle.RawTurtle(turtle_area)
shape.width(10)
_D()



root.mainloop()
