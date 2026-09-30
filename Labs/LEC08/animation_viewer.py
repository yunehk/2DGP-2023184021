"""Drill 8: four irregular-sheet animations, five loops each, one-second holds."""
from pathlib import Path
import time

import pico2d as p

from animation_data import load_animations
from animation_player import Playback
from animation_render import display_scale, draw_frame


WIDTH, HEIGHT = 800, 600
FOLDER = Path(__file__).resolve().parent


def main():
    data, animations = load_animations(FOLDER / 'sonic_frames.json')
    player = Playback(animations)
    p.open_canvas(WIDTH, HEIGHT)
    try:
        p.hide_lattice()
        image = p.load_image(str(FOLDER / data['image']))
        scale = display_scale(animations, WIDTH, HEIGHT)
        running = True
        previous = time.monotonic()
        while running:
            for event in p.get_events():
                if event.type == p.SDL_QUIT:
                    running = False
                elif event.type == p.SDL_KEYDOWN and event.key == p.SDLK_ESCAPE:
                    running = False
            if not running:
                break

            now = time.monotonic()
            player.update(now - previous)
            previous = now
            p.clear_canvas()
            draw_frame(image, player.frame, scale, (WIDTH / 2, HEIGHT / 2))
            p.update_canvas()
            p.delay(0.01)
    finally:
        p.close_canvas()


if __name__ == '__main__':
    main()
