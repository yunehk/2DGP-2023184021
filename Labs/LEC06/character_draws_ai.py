from pico2d import *


open_canvas(800, 600)
character = load_image('character.png')

clear_canvas()
character.draw(400, 300)
update_canvas()
delay(0.1)
close_canvas()
