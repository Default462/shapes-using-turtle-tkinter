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
    shape.bk(100)
    shape.left(90)
    shape.fd(100)
    shape.right(90)
    shape.fd(100)
    shape.bk(100)
    shape.right(90)
    shape.fd(200)
    shape.left(90)
    shape.fd(100)


def _F():
    shape.bk(100)
    shape.left(90)
    shape.fd(100)
    shape.right(90)
    shape.fd(100)
    shape.bk(100)
    shape.right(90)
    shape.fd(200)

def _G():
    shape.pu()
    shape.sety(200)
    shape.pd()
    shape.left(180)
    shape.circle(200, 260)
    shape.left(100)
    shape.forward(200)

def _H():
    shape.bk(100)
    shape.left(90)
    shape.forward(100)
    shape.bk(200)
    shape.forward(100)
    shape.right(90)
    shape.forward(100)
    shape.left(90)
    shape.forward(100)
    shape.bk(200)

def _I():
    shape.left(90)
    shape.fd(100)
    shape.right(90)
    shape.forward(60)
    shape.bk(120)
    shape.forward(60)
    shape.right(90)
    shape.forward(200)
    shape.left(90)
    shape.fd(60)
    shape.bk(120)

def _J():
    shape.left(90)
    shape.forward(100)
    shape.right(90)
    shape.forward(60)
    shape.bk(140)
    shape.forward(80)
    shape.right(90)
    shape.forward(150)
    shape.pu()
    shape.right(90)
    shape.forward(100)
    shape.left(180)
    shape.pd()

    shape.right(90)
    shape.circle(50,180)
turtle_area.pack()
shape = turtle.RawTurtle(turtle_area)
shape.width(10)
_J()



root.mainloop()
