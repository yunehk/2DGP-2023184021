"""Drawing helpers; retain each source rectangle's aspect ratio."""


def source_rect(frame, sheet_height):
    return (frame.x, sheet_height - frame.y - frame.height,
            frame.width, frame.height)


def draw_frame(image, frame, scale, center):
    image.clip_draw(*source_rect(frame, image.h), *center,
                    frame.width * scale, frame.height * scale)
