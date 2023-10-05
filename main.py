from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# Draw a square
# for x in range(4):
    # timmy_the_turtle.forward(100)
    # timmy_the_turtle.right(90)

# Draw a dashed line
# for x in range(50):
    # timmy_the_turtle.forward(10)
    # timmy_the_turtle.penup()
    # timmy_the_turtle.forward(10)
    # timmy_the_turtle.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# triangle

# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
# for x in range(3):
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.right(120)
#
# # square
# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
# for x in range(4):
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.right(90)
#
# # pentagon
# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
# for x in range(5):
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.right(72)
#
#
# # hexagon
# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
# for x in range(6):
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.right(60)
#
#
# # heptagon
# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
# for x in range(7):
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.right(51.43)
#
#
# # octagon
# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
# for x in range(8):
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.right(45)
#
#
# # nonagon
# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
# for x in range(9):
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.right(40)
#
#
# # decagon
# timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
# for x in range(10):
#     timmy_the_turtle.forward(40)
#     timmy_the_turtle.right(36)


# random walk
x = 0
while x < 100:
    timmy_the_turtle.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    direction = randint(0, 3)
    if direction == 0:
        timmy_the_turtle.forward(30)
    elif direction == 1:
        timmy_the_turtle.right(90)
    elif direction == 2:
        timmy_the_turtle.left(90)
    else:
        timmy_the_turtle.back(30)

    x += 1


screen.exitonclick()
