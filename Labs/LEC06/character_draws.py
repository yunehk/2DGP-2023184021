from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

def move_triangle_bottom():
    print("triangle bottom")
    for x in range(100, 701, 5):
        draw_character(x, 100)


def move_triangle_up():
    print("triangle up")


def move_triangle_down():
    print("triangle down")

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)
    return True

def move_circle():
    print("circle")

    for degree in range(0,360,5):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_character(x, y)
    pass

def move_top():
    print("top")
    for x in range(50, 751, 5):
        draw_character(x, 550)
    pass

def move_right():
    print("right")
    for y in range(550, 49, -5):
        draw_character(750, y)

def move_bottom():
    print("bottom")
    for x in range(750, 49, -5):
        draw_character(x, 50)

def move_left():
    print("left")
    for y in range(50, 551, 5):
        draw_character(50, y)

def move_rectangle():
    print("rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_triangle():
    print("triangle")
    move_triangle_bottom()
    move_triangle_up()
    move_triangle_down()



while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass



close_canvas()
