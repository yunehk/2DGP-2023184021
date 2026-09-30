"""Drill 8: four irregular-sheet animations, five loops each, one-second holds."""
from pathlib import Path
import time
import os
import argparse

import pico2d as p

from animation_data import load_animations
from animation_player import Playback
from animation_render import display_scale, draw_frame


WIDTH, HEIGHT = 800, 600
FOLDER = Path(__file__).resolve().parent


def optional_font():
    fonts = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts'
    for name in ('arial.ttf', 'malgun.ttf'):
        path = fonts / name
        if path.is_file():
            return p.load_font(str(path), 20)
    return None


def main():
    data, animations = load_animations(FOLDER / 'sonic_frames.json')
    player = Playback(animations)
    p.open_canvas(WIDTH, HEIGHT)
    try:
        p.hide_lattice()
        image = p.load_image(str(FOLDER / data['image']))
        if (image.w, image.h) != (data['image_width'], data['image_height']):
            raise ValueError('Sprite sheet dimensions do not match metadata')
        font = optional_font()
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
            if font is not None:
                cycle = min(player.completed_cycles + 1, player.repeats)
                state = 'HOLD 1 second' if player.holding else f'Cycle {cycle}/5'
                font.draw(20, HEIGHT - 22,
                          f'{player.animation.label} | {state} | '
                          f'Frame {player.frame_index + 1}/{len(player.animation.frames)}')
                font.draw(20, 22, 'Walk > Run > Spin > Tumble     ESC: exit')
            p.update_canvas()
            p.delay(0.01)
    finally:
        p.close_canvas()


def validate():
    data, animations = load_animations(FOLDER / 'sonic_frames.json')
    if not (FOLDER / data['image']).is_file():
        raise FileNotFoundError(data['image'])
    scale = display_scale(animations, WIDTH, HEIGHT)
    sizes = {(f.width, f.height) for a in animations for f in a.frames}
    print(f'{len(animations)} motions; {len(sizes)} source sizes; scale={scale:.2f}')
    for animation in animations:
        count = len(animation.frames)
        seconds = count * animation.frame_seconds * 5 + 1
        print(f'{animation.label}: {count} frames, 5 cycles + 1s hold = {seconds:.1f}s')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate', action='store_true', help='Check frame data without a window')
    args = parser.parse_args()
    if args.validate:
        validate()
    else:
        main()
