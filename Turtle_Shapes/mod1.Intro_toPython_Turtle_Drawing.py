#Module 1 Assignment INFO 1020
#Please use this template and fill in code after each comment

#Import the turtle module (see page 19, section 1.5 of text 4th ed.)
import turtle
bri = turtle.Turtle()


#Have the turtle draw something interesting.
#The turtle must use a loop to repeat some aspect of the drawing.
#Use at least two different shapes.  You _can_ use the drawPolygon() 
#and drawCircle() functions from the book.
#If you aren't sure what to draw, do Programming Exercise 1.1 in the book.


def drawSquare(myTurtle, sideLength):
    for x in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)

def drawCircle(myTurtle, radius):
    myTurtle.circle(50)
    
drawSquare(bri, 100)
drawCircle(bri,100)
bri.up()
bri.goto(0,200)
bri.down()
drawSquare(bri, 100)
drawCircle(bri,100)

turtle.done()

#When finished, submit both this .py file and a png screenshot of your drawing.
#this program draws circles and squares stacked upon each other as if they may fall over.
