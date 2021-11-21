#Hello World Program
#<Author> Bongani Detiilis
#<Date> 20/07/2020

#Modules
from turtle import *

#Writing a program that draws HELLO WORLD on a canvas using turlte graphics
#constructing the neccesary alphabets

#function for letter H
def draw_H(x,y):
    penup()
    setposition(x,y)
    pendown()
    left(90)
    forward(200)
    backward(100)
    right(90)
    forward(50)
    left(90)
    forward(100)
    backward(200)
    right(90)
    
#Function for the letter E
def draw_E(x,y):
    penup()
    setposition(x,y)
    pendown()
    left(90)
    forward(200)
    b = 0
    for i in range(3):
        b+=1
        right(90)
        forward(50)
        backward(50)
        left(90)
        if(b==3):
            break
        backward(200/2)
    right(90)
              
#Function for the letter L
def draw_L(x,y):
    penup()
    setposition(x,y)
    pendown()
    left(90)
    forward(200)
    backward(200)
    right(90)
    forward(50)

#Function for the letter O
def draw_O(x,y):
    penup()
    setposition(x,y)
    pendown()
    for i in range(2):
        forward(50)
        left(90)
        forward(200)
        left(90)

#Function for the letter W
def draw_W(x,y):
    penup()
    setposition(x,y)
    pendown()
    left(90)
    forward(200)
    backward(200)
    right(30)
    forward(50)
    right(120)
    forward(50)
    left(150)
    forward(200)
    backward(200)
    right(90)

#Function for the letter R
def draw_R(x,y):
    penup()
    setposition(x,y)
    pendown()
    left(90)
    forward(2*(200/3))
    right(90)
    for i in range(4):
        forward(200/3)
        left(90)
    right(63.43494882)   
    forward(150)
    left(63.43494882) 

#Function for the letter D
def draw_D(x,y):
    penup()
    setposition(x,y)
    pendown()
    left(90)
    forward(200)
    backward(200)
    right(90)
    circle(100, 180)


#interface

#Write Hello
draw_H(-300,0)
draw_E(-200,0)
draw_L(-100,0)
draw_L(0,0)
draw_O(100,0)


#Write world
draw_W(-300,-250)
draw_O(-200,-250)
draw_R(-100,-250)
draw_L(0,-250)
draw_D(100,-250)




    
    
    
    
    
