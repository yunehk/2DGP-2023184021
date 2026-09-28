from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

def move_circle():

    for degree in range(0,360,5):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.05)
    pass

def move_rectangle():
    print("rectangle")
    pass

def move_triangle():
    print("triangle")
    pass    



while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass



close_canvas()
