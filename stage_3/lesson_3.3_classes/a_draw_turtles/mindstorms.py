# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

# Your code here.

def draw_square():
    window = turtle.Screen()
    window.bgcolor("yellow")

    brow = turtle.Turtle()
    brow.shape("turtle")
    brow.color("red")
    brow.speed(2)

    brow.forward(100)
    brow.right(90)
    brow.forward(100)
    brow.right(90)
    brow.forward(100)
    brow.right(90)
    brow.forward(100)
    brow.right(90)

    window.exitonclick()

draw_square()
