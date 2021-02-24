from turtle import Turtle, Screen
import time


def create_snake() -> list:
    """ Creates a snake body from Turtle objects in the center of screen """
    x = -40
    y = 0
    s_segments = []
    for _ in range(3):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(x, y)
        s_segments.append(new_segment)

        x += 20

    return s_segments


# Screen properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


s_segments = create_snake()
screen.update()

print("resetted again")
print("resetted again")
print("resetted again")

screen.exitonclick()