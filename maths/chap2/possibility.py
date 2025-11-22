from random import uniform
from vectors import add,scale
from vector_drawing import Points,draw

u=(-1,1)
v=(1,1)

def random_r():
    return uniform(-3,3)

def random_s():
    return uniform(-1,1)

possibilities = [add(scale(random_r(),u),scale(random_s(),v)) for i in range(0,500)]

draw(Points(*possibilities))
