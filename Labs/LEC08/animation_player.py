"""Playback state independent of the graphics window."""
from dataclasses import dataclass


@dataclass
class Playback:
    animations: tuple
    repeats: int = 5
    animation_index: int = 0
    frame_index: int = 0
    completed_cycles: int = 0
    elapsed: float = 0.0

    @property
    def animation(self):
        return self.animations[self.animation_index]

    @property
    def frame(self):
        return self.animation.frames[self.frame_index]

    def update(self, seconds):
        self.elapsed += seconds
        while self.elapsed >= self.animation.frame_seconds:
            self.elapsed -= self.animation.frame_seconds
            self.frame_index += 1
            if self.frame_index == len(self.animation.frames):
                self.frame_index = 0
                self.completed_cycles += 1
                if self.completed_cycles == self.repeats:
                    self.completed_cycles = 0
                    self.animation_index = (self.animation_index + 1) % len(self.animations)
