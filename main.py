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

def _K():
    shape.pu()
    shape.left(90)
    shape.fd(100)
    shape.pd()
    shape.bk(200)
    shape.pu()
    shape.forward(100)
    shape.pd()
    shape.right(45)
    shape.forward(130)
    shape.bk(130)
    shape.right(90)
    shape.forward(140)

def _L():
    shape.pu()
    shape.left(90)
    shape.forward(100)
    shape.pd()
    shape.backward(200)
    shape.right(90)
    shape.forward(100)

def _M():
    shape.left(90)
    shape.fd(200)
    shape.right(135)
    shape.forward(100)
    shape.left(90)
    shape.fd(100)
    shape.right(135)
    shape.forward(200)

def _N():
    shape.left(90)
    shape.fd(200)
    shape.right(150)
    shape.forward(225)
    shape.left(150)
    shape.forward(200)

def _O():
    shape.circle(100)

def _P():
    shape.circle(50, 180)
    shape.left(90)
    shape.fd(200)

def _Q():
    shape.circle(100)
    shape.circle(100,20)
    shape.right(50)
    shape.fd(70)

def _R():
    shape.circle(50, 180)
    shape.left(90)
    shape.fd(200)
    shape.bk(100)
    shape.left(35)
    shape.fd(115)

def _S():
    shape.pu()
    shape.left(90)
    shape.fd(100)
    shape.right(90)
    shape.fd(100)
    shape.circle(100, 50)
    shape.pd()
    shape.left(90)
    shape.circle(100,180)
    shape.left(30)
    shape.fd(100)
    shape.right(120)
    shape.pu()
    shape.fd(200)
    shape.pd()
    shape.left(90)
    shape.circle(100,180)

def _T():
    shape.left(90)
    shape.bk(100)
    shape.fd(200)
    shape.left(90)
    shape.fd(60)
    shape.bk(120)

def _U():
    shape.pu()
    shape.left(90)
    shape.fd(100)
    shape.left(90)
    shape.fd(100)
    shape.pd()
    shape.left(90)
    shape.fd(150)
    shape.circle(60,180)
    shape.fd(150)

def _V():
    shape.left(70)
    shape.fd(100)
    shape.bk(200)
    shape.left(40)
    shape.fd(200)

turtle_area.pack()
shape = turtle.RawTurtle(turtle_area)
shape.width(10)
_V()



root.mainloop()
