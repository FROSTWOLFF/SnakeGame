from turtle import Turtle, Screen
import time


def create_snake() -> list:
    """ Creates a snake body from Turtle objects in the center of screen """
    snake_number = 3
    x = -20 * (snake_number - 1)
    y = 0
    s_segments = []
    for _ in range(snake_number):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(x, y)
        s_segments.append(new_segment)

        x += 20

    return s_segments


def go_up():
    if s_head.heading() != 270:
        s_head.setheading(90)


def go_down():
    if s_head.heading() != 90:
        s_head.setheading(270)


def go_left():
    if s_head.heading() != 0:
        s_head.setheading(180)


def go_right():
    if s_head.heading() != 180:
        s_head.setheading(0)


def move_snake():
    """ Moves the snake body from tail to head by taking each others positions """
    for seg_num in range(len(s_segments) - 1):
        s_segments[seg_num].goto(s_segments[seg_num + 1].position())
    s_head.forward(20)


# Screen properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Creating the first snake segments
s_segments = create_snake()
s_head = s_segments[len(s_segments) - 1]  # Last segment of snake


# Screen Listening
screen.listen()
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")


# Main Game
game_on = True
while game_on:
    screen.update()
    move_snake()
    time.sleep(0.1)


screen.mainloop()