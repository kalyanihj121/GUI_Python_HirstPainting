from turtle import Turtle, Screen
import  turtle as t

timmy = Turtle()
timmy.shape("triangle")
t.colormode(255)
#timmy.color("red")

# drawing a square
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# drawing dashed line
# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# drawing all the shapes
# import  random
# color_list = ["CadetBlue", "BlueViolet", "DeepPink", "DarkGreen", "coral"]
#
#
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_sides in range(3, 11):
#     my_color = random.choice(color_list)
#     timmy.color(my_color)
#     draw_shape(shape_sides)

# Drawing random walk
import random
# directions = [0, 90, 180, 270]
# colors = ["CadetBlue", "BlueViolet", "DeepPink", "DarkGreen", "coral"]


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# #
# #
# timmy.pensize(15)
timmy.speed(0)
# for _ in range(100):
#     #col_choice = random.choice(colors)
#     timmy.color(random_colors())
#     timmy.forward(30)
#     choice = random.choice(directions)
#     timmy.setheading(choice)

# Drawing spirograph
def draw_spirograph(size_of_gaps):

    for i in range(int(360/size_of_gaps)):
        timmy.circle(100)
        timmy.color(random_colors())
        timmy.setheading(timmy.heading() + size_of_gaps)


draw_spirograph(5) 








screen = Screen()
screen.exitonclick()