# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

# Your code here.
window = turtle.Screen()
window.bgcolor("yellow")

brow = turtle.Turtle()
brow.shape("turtle")
brow.speed(2)

def draw_square(length, color):
    brow.color(color)
    for counter in range(4):
        brow.forward(length)
        brow.right(90)

def draw_circle(radius, color):
    brow.color(color)
    brow.circle(radius)

def draw_triangle(cor1, cor2, color):
    brow.color(color)
    brow.goto(cor1)
    brow.goto(cor2)
    brow.goto(0,0)

draw_square(100, "red")
draw_circle(100, "green")
draw_triangle((150,50), (-50, -150), "blue")
# window.exitonclick()
