"""Drawing helpers; retain each source rectangle's aspect ratio."""


def source_rect(frame, sheet_height):
    return (frame.x, sheet_height - frame.y - frame.height,
            frame.width, frame.height)


def draw_frame(image, frame, scale, center):
    image.clip_draw(*source_rect(frame, image.h), *center,
                    frame.width * scale, frame.height * scale)


def display_scale(animations, canvas_width, canvas_height):
    frames = [frame for animation in animations for frame in animation.frames]
    widest = max(frame.width for frame in frames)
    tallest = max(frame.height for frame in frames)
    return min(canvas_width * 0.82 / widest, canvas_height * 0.82 / tallest)
