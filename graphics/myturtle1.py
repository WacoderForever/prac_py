from turtle import *

shape("turtle")

def mysquare(length):
    for i in range(4):
        forward(length)
        right(90)

def circle_of_squares(length_of_square):
    for i in range(72):
        mysquare(length_of_square)
        right(5)

def triangle(length):
    for i in range(3):
        right(120)
        forward(length)

def turtle_spiral():
    length = 10
    for i in range(60):
        mysquare(length)
        right(5)
        length = length + 10

def star():
    