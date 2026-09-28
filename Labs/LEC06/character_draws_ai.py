from pico2d import *
import math
from pathlib import Path

WIDTH, HEIGHT = 800, 600
PIXELS_PER_FRAME = 5

open_canvas(WIDTH, HEIGHT)
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

def move_line(x0, y0, x1, y1):
    distance = math.hypot(x1 - x0, y1 - y0)
    steps = max(1, math.ceil(distance / PIXELS_PER_FRAME))
    for step in range(steps + 1):
        t = step / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        if not draw_character(x, y):
            return

def move_circle():
    for degree in range(361):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        if not draw_character(x, y):
            return

def move_top():
    move_line(50, 550, 750, 550)

def move_right():
    move_line(750, 550, 750, 50)

def move_bottom():
    move_line(750, 50, 50, 50)

def move_left():
    move_line(50, 50, 50, 550)

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
    move_line(100, 100, 700, 100)

def triangle_up():
    move_line(700, 100, 400, 500)

def triangle_down():
    move_line(400, 500, 100, 100)

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
