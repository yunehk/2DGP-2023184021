from pico2d import *
from pathlib import Path
import time


running = True


def check_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def pause(seconds):
    end_time = time.monotonic() + seconds
    while running and time.monotonic() < end_time:
        check_events()
        delay(0.01)


def main():
    open_canvas(800, 600)
    try:
        folder = Path(__file__).resolve().parent
        boy = load_image(str(folder.parent / 'LEC08_Animation' / 'animation_sheet.png'))

        # Top to bottom: idle right, idle left, run right, run left.
        while running:
            for row in [3, 2, 1, 0]:
                if not running:
                    break

                frame = 0
                # Eight frames per animation, repeated five times.
                for _ in range(8 * 5):
                    check_events()
                    if not running:
                        break

                    clear_canvas()
                    boy.clip_draw(
                        frame * 100, row * 100,
                        100, 100,
                        400, 300,
                        600, 600
                    )
                    update_canvas()
                    frame = (frame + 1) % 8
                    pause(0.1)

                # Hold the last frame for one second.
                pause(1.0)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
