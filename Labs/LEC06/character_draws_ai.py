from pico2d import *
import math


open_canvas(800, 600)
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.02)
    return True

def move_circle():
    for degree in range(361):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)

def move_top():
    for x in range(50, 751, 5):
        draw_character(x, 550)

def move_right():
    for y in range(550, 49, -5):
        draw_character(750, y)

def move_bottom():
    for x in range(750, 49, -5):
        draw_character(x, 50)

def move_left():
    for y in range(50, 551, 5):
        draw_character(50, y)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def triangle_base():
    for step in range(101):
        t = step / 100
        x = 100 + (700 - 100) * t
        y = 100 + (100 - 100) * t
        draw_character(x, y)

def triangle_up():
    for step in range(101):
        t = step / 100
        x = 700 + (400 - 700) * t
        y = 100 + (500 - 100) * t
        draw_character(x, y)

def triangle_down():
    for step in range(101):
        t = step / 100
        x = 400 + (100 - 400) * t
        y = 500 + (100 - 500) * t
        draw_character(x, y)

def move_triangle():
    triangle_base()
    triangle_up()
    triangle_down()

def run_cycle():
    move_circle()
    move_rectangle()
    move_triangle()

run_cycle()
close_canvas()
