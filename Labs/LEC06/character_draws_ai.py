from pico2d import *


open_canvas(800, 600)
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.02)
    return True

draw_character(400, 300)
close_canvas()
