from turtle import Turtle, Screen
import random

palette = [(0, 0, 0), (82, 61, 43), (231, 232, 236), (228, 233, 230),
           (201, 162, 92), (165, 66, 51), (158, 58, 73), (128, 163, 190), (213, 84, 55),
           (224, 206, 120), (64, 36, 54), (201, 136, 161), (57, 50, 105), (42, 38, 67),
           (65, 82, 148), (195, 80, 119), (129, 178, 157), (158, 170, 69), (81, 153, 114),
           (75, 127, 96), (112, 44, 37), (117, 42, 51), (97, 107, 167), (160, 200, 217),
           (219, 175, 186), (225, 176, 168), (181, 186, 212), (175, 203, 189), (82, 150, 152), (237, 230, 233)]

# print(len(palette))

start_x = -180
start_y = -180

s = Screen()
s.colormode(255)

t = Turtle()
t.shape("turtle")
t.penup()
t.hideturtle()

for x in range(10):
    t.setposition(start_x, start_y)
    for y in range(10):
        t.dot(15, random.choice(palette))
        t.forward(40)
    start_y += 40

s.exitonclick()