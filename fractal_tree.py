from turtle import *

setheading(90)
penup()
setpos(0,-250)
pendown()

def fractal_tree(length,level):
    pensize(length/10)

    if length < 20:
        pencolor("green")
    else:
        pencolor("brown")

    speed(1)
    if level > 0:
        fd(length)
        rt(30)
        fractal_tree(length*0.7,level-1)
        lt(90)
        fractal_tree(length*0.5,level-1)
        rt(60)
        penup()
        bk(length)
        pendown()

def main():
    fractal_tree(200,10)

if __name__=='__main__':
    main()
