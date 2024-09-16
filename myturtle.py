from turtle import *

def square(length):
    for i in range(4):
        forward(length)
        right(90)

def square_spiral():
    length=5
    for i in range(100):
        square(length)
        right(5)
        length+=5

def equi_triangle(side):
    forward(side)
    left(120)
    forward(side)
    left(120)
    forward(side)

def polygon(n_sides):
    angle=360/n_sides
    for i in range(n_sides):
        forward(100)
        left(angle)
        
def star(size):
    forward(size)

    for i in range(4):
        right(145)
        forward(size)

def star_spiral():
    size=5
    for i in range(100):
        star(size)
        right(150)
        size+=5
def triangle_spiral():
    size=20
    for i in range(60):
        equi_triangle(size)
        size+=5
        right(125)

def main():
    shape('turtle')
    star_spiral()

if __name__=='__main__':
    main()