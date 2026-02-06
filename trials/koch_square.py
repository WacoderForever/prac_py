from turtle import *
penup()
setpos(0,100)
pendown()
def koch(length,level):
    speed(0)

    for i in range(4):
        plotside(length,level)
        rt(90)

def plotside(length,level):

    if level==0:
        fd(length)
        return
    plotside(length/3, level - 1)
    lt(90)
    plotside(length/3, level - 1)
    rt(90)
    plotside(length/3, level - 1)
    rt(90)
    plotside(length/3, level - 1)
    lt(90)
    plotside(length/3, level - 1)

def main():
    koch(200,4)

if __name__=="__main__":
    main()