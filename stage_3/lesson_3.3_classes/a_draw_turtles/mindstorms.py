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
window.bgcolor("white")

brow = turtle.Turtle()
brow.shape("turtle")
brow.speed(20)

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

def draw_art():
    brow.color("red")
    j = 0
    angle = 360
    rotate = 5
    while j < angle:
        draw_square(150, "red")
        j += rotate
        brow.right(rotate)
    window.exitonclick()

def draw_flower():
    pen1 = turtle.Turtle()
    pen2 = turtle.Turtle()
    pen3 = turtle.Turtle()

    pen1.color("yellow")
    pen1.speed(20)

    pen2.color("red")
    pen2.speed(20)
    pen2.pensize(5)

    pen3.color("green")
    pen3.speed(20)
    pen3.pensize(5)

    for i in range(0, 360, 10):
        pen1.down()
        pen1.home() # move to origin
        pen1.right(i); pen1.forward(70)
        pen1.up()
        pen1.right(45); pen1.forward(70)
        pen1.right(135); pen1.forward(70)

        pen2.up()
        pen2.home()
        pen2.right(i); pen2.forward(70)
        pen2.down()
        pen2.right(45); pen2.forward(70)
        pen2.right(135); pen2.forward(70)

    pen1.ht()
    pen1.up(); pen2.up(); pen3.up()
    
    pen3.home(); pen3.goto(0, -100)
    pen3.down(); pen3.goto(0, -150)
    pen3.right(10); pen3.forward(70)
    pen3.right(45); pen3.forward(70)
    pen3.right(135); pen3.forward(70)
    pen3.goto(0, -150)
    pen3.goto(0, -300)
    pen3.right(80)

    window.exitonclick()
# draw_square(100, "red")
# draw_circle(100, "green")
# draw_triangle((150,50), (-50, -150), "blue")
# draw_art()
draw_flower()
# window.exitonclick()
