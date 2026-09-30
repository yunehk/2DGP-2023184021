"""Elapsed-time playback with five cycles and a one-second final-frame hold."""
from dataclasses import dataclass
import math


@dataclass
class Playback:
    animations: tuple
    repeats: int = 5
    hold_seconds: float = 1.0
    animation_index: int = 0
    frame_index: int = 0
    completed_cycles: int = 0
    elapsed: float = 0.0
    holding: bool = False

    def __post_init__(self):
        if not self.animations or self.repeats < 1 or self.hold_seconds <= 0:
            raise ValueError('Animations, repeats, and hold duration must be positive')

    @property
    def animation(self):
        return self.animations[self.animation_index]

    @property
    def frame(self):
        return self.animation.frames[self.frame_index]

    def update(self, seconds):
        if not math.isfinite(seconds) or seconds < 0:
            raise ValueError('Elapsed time must be finite and nonnegative')
        self.elapsed += seconds
        while True:
            duration = self.hold_seconds if self.holding else self.animation.frame_seconds
            if self.elapsed + 1e-10 < duration:
                break
            self.elapsed = max(0.0, self.elapsed - duration)
            if self.holding:
                self.animation_index = (self.animation_index + 1) % len(self.animations)
                self.frame_index = 0
                self.completed_cycles = 0
                self.holding = False
            elif self.frame_index + 1 < len(self.animation.frames):
                self.frame_index += 1
            else:
                self.completed_cycles += 1
                if self.completed_cycles == self.repeats:
                    self.holding = True
                else:
                    self.frame_index = 0
