"""AI 구현: 원 → 사각형 → 삼각형을 반복한다. X 또는 ESC로 종료한다."""
import math
from pathlib import Path
import time

from pico2d import (
    open_canvas, close_canvas, load_image, clear_canvas, update_canvas,
    get_events, delay, SDL_QUIT, SDL_KEYDOWN, SDLK_ESCAPE,
)

WIDTH, HEIGHT = 800, 600
SPEED = 250  # 초당 이동 거리(픽셀)
CENTER = (400, 300)
RADIUS = 200
RECTANGLE = [(50, 550), (750, 550), (750, 50), (50, 50)]
TRIANGLE = [(100, 100), (700, 100), (400, 500)]


def perimeter(vertices):
    return sum(math.dist(vertices[i], vertices[(i + 1) % len(vertices)])
               for i in range(len(vertices)))


def polygon_position(vertices, distance):
    """다각형의 변을 따라 distance만큼 이동한 위치를 계산한다."""
    distance %= perimeter(vertices)
    for i, (x0, y0) in enumerate(vertices):
        x1, y1 = vertices[(i + 1) % len(vertices)]
        length = math.hypot(x1 - x0, y1 - y0)
        if distance <= length:
            t = distance / length
            return x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
        distance -= length
    return vertices[0]


def position(phase, distance):
    if phase == 0:
        angle = distance / RADIUS
        return (CENTER[0] + RADIUS * math.cos(angle),
                CENTER[1] + RADIUS * math.sin(angle))
    return polygon_position(RECTANGLE if phase == 1 else TRIANGLE, distance)


def main():
    lengths = [2 * math.pi * RADIUS, perimeter(RECTANGLE), perimeter(TRIANGLE)]
    phase = 0
    distance = 0.0
    open_canvas(WIDTH, HEIGHT)
    try:
        character = load_image(str(Path(__file__).with_name('character.png')))
        previous = time.perf_counter()
        while True:
            events = get_events()
            if any(event.type == SDL_QUIT or
                   (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE)
                   for event in events):
                break

            now = time.perf_counter()
            # 잠깐 멈췄다 돌아와도 한 프레임에 크게 건너뛰지 않는다.
            distance += SPEED * min(max(now - previous, 0), 0.05)
            previous = now
            while distance >= lengths[phase]:
                distance -= lengths[phase]
                phase = (phase + 1) % 3

            x, y = position(phase, distance)
            clear_canvas()
            character.draw(x, y)
            update_canvas()
            delay(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
