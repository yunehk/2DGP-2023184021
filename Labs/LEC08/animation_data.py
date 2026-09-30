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
