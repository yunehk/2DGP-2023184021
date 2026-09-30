"""Sprite coordinates use a top-left origin, as in image editors."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Frame:
    x: int
    y: int
    width: int
    height: int


@dataclass(frozen=True)
class Animation:
    name: str
    label: str
    frame_seconds: float
    frames: tuple[Frame, ...]


def load_animations(path):
    import json
    import math

    data = json.loads(path.read_text(encoding='utf-8-sig'))
    width, height = data['image_width'], data['image_height']
    if not all(type(v) is int and v > 0 for v in (width, height)):
        raise ValueError('Invalid sprite sheet dimensions')
    animations = []
    names = set()
    for item in data['animations']:
        name = item['name']
        if not name or name in names:
            raise ValueError('Animation names must be nonempty and unique')
        names.add(name)
        seconds = item['frame_seconds']
        if not math.isfinite(seconds) or seconds <= 0:
            raise ValueError('Frame duration must be positive and finite')
        frames = tuple(Frame(**rect) for rect in item['frames'])
        if not frames:
            raise ValueError(f'{name}: missing frames')
        for frame in frames:
            values = (frame.x, frame.y, frame.width, frame.height)
            if not all(type(v) is int for v in values):
                raise ValueError(f'{name}: frame coordinates must be integers')
            if (frame.x < 0 or frame.y < 0 or frame.width <= 0
                    or frame.height <= 0 or frame.x + frame.width > width
                    or frame.y + frame.height > height):
                raise ValueError(f'{name}: frame outside sprite sheet')
        animations.append(Animation(name, item['label'], seconds, frames))
    if not animations:
        raise ValueError('No animations supplied')
    return data, tuple(animations)
