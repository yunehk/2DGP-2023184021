from pico2d import *
import math
from pathlib import Path


open_canvas(800, 600)
character = load_image(str(Path(__file__).with_name('character.png')))
running = True

def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_character(x, y):
    handle_events()
    if not running:
        return False
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
        if not draw_character(x, y):
            return

def move_top():
    for x in range(50, 751, 5):
        if not draw_character(x, 550):
            return

def move_right():
    for y in range(550, 49, -5):
        if not draw_character(750, y):
            return

def move_bottom():
    for x in range(750, 49, -5):
        if not draw_character(x, 50):
            return

def move_left():
    for y in range(50, 551, 5):
        if not draw_character(50, y):
            return

def move_rectangle():
    if not running:
        return
    move_top()
    if not running:
        return
    move_right()
    if not running:
        return
    move_bottom()
    if not running:
        return
    move_left()

def triangle_base():
    for step in range(101):
        t = step / 100
        x = 100 + (700 - 100) * t
        y = 100 + (100 - 100) * t
        if not draw_character(x, y):
            return

def triangle_up():
    for step in range(101):
        t = step / 100
        x = 700 + (400 - 700) * t
        y = 100 + (500 - 100) * t
        if not draw_character(x, y):
            return

def triangle_down():
    for step in range(101):
        t = step / 100
        x = 400 + (100 - 400) * t
        y = 500 + (100 - 500) * t
        if not draw_character(x, y):
            return

def move_triangle():
    if not running:
        return
    triangle_base()
    if not running:
        return
    triangle_up()
    if not running:
        return
    triangle_down()

def run_cycle():
    if not running:
        return
    move_circle()
    if not running:
        return
    move_rectangle()
    if not running:
        return
    move_triangle()

try:
    while running:
        handle_events()
        run_cycle()
except KeyboardInterrupt:
    pass
finally:
    close_canvas()
