from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')
running = True

def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

def move_triangle_bottom():
    print("triangle bottom")
    for step in range(121):
        t = step / 120
        x = 100 + (700 - 100) * t
        if not draw_character(x, 100):
            return


def move_triangle_up():
    print("triangle up")
    for step in range(101):
        t = step / 100
        x = 700 + (400 - 700) * t
        y = 100 + (500 - 100) * t
        if not draw_character(x, y):
            return


def move_triangle_down():
    print("triangle down")
    for step in range(101):
        t = step / 100
        x = 400 + (100 - 400) * t
        y = 500 + (100 - 500) * t
        if not draw_character(x, y):
            return

def draw_character(x, y):
    handle_events()
    if not running:
        return False
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)
    return True

def move_circle():
    print("circle")

    for degree in range(361):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        if not draw_character(x, y):
            return
    pass

def move_top():
    print("top")
    for x in range(50, 751, 5):
        if not draw_character(x, 550):
            return
    pass

def move_right():
    print("right")
    for y in range(550, 49, -5):
        if not draw_character(750, y):
            return

def move_bottom():
    print("bottom")
    for x in range(750, 49, -5):
        if not draw_character(x, 50):
            return

def move_left():
    print("left")
    for y in range(50, 551, 5):
        if not draw_character(50, y):
            return

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



while running:
    handle_events()
    move_circle()
    move_rectangle()
    move_triangle()
    pass



close_canvas()
