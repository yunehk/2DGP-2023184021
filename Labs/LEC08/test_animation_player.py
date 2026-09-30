from pathlib import Path
import unittest
from unittest.mock import patch

from animation_data import Frame, load_animations
from animation_player import Playback
from animation_render import display_scale, source_rect


class PlaybackTests(unittest.TestCase):
    def setUp(self):
        _, self.animations = load_animations(Path(__file__).with_name('sonic_frames.json'))
        self.player = Playback(self.animations)

    def test_exactly_five_cycles_before_hold(self):
        for animation in self.animations:
            for cycle in range(5):
                for frame in range(len(animation.frames)):
                    self.assertEqual(self.player.animation, animation)
                    self.assertEqual(self.player.frame_index, frame)
                    self.assertFalse(self.player.holding)
                    self.player.update(animation.frame_seconds)
            self.assertTrue(self.player.holding)
            self.assertEqual(self.player.frame_index, len(animation.frames) - 1)
            self.player.update(0.999)
            self.assertEqual(self.player.animation, animation)
            self.assertTrue(self.player.holding)
            self.player.update(0.001)
            self.assertFalse(self.player.holding)
        self.assertEqual(self.player.animation_index, 0)
        self.assertEqual(self.player.frame_index, 0)

    def test_full_sequence_wrap_with_long_elapsed_time(self):
        total = sum(len(a.frames) * a.frame_seconds * 5 + 1 for a in self.animations)
        self.player.update(total * 3 + 0.25)
        self.assertEqual(self.player.animation_index, 0)
        self.assertEqual(self.player.frame_index, 2)
        self.assertAlmostEqual(self.player.elapsed, 0.05)

    def test_invalid_elapsed_time(self):
        for seconds in (-1, float('nan'), float('inf')):
            with self.assertRaises(ValueError):
                self.player.update(seconds)

    def test_bottom_origin_conversion(self):
        self.assertEqual(source_rect(Frame(12, 40, 20, 35), 525), (12, 450, 20, 35))

    def test_enlargement_and_no_clipping(self):
        scale = display_scale(self.animations, 800, 600)
        for animation in self.animations:
            for frame in animation.frames:
                self.assertGreaterEqual(frame.height * scale, 300)
                self.assertLessEqual(frame.height * scale, 492.001)
                self.assertLessEqual(frame.width * scale, 656.001)

    def test_close_and_escape_during_playback_and_hold(self):
        import types
        import animation_viewer as viewer
        for holding in (False, True):
            for event in (types.SimpleNamespace(type=viewer.p.SDL_QUIT),
                          types.SimpleNamespace(type=viewer.p.SDL_KEYDOWN, key=viewer.p.SDLK_ESCAPE)):
                player = Playback(self.animations)
                player.holding = holding
                with patch.object(viewer, 'Playback', return_value=player), \
                     patch.object(viewer.p, 'open_canvas'), \
                     patch.object(viewer.p, 'close_canvas') as close, \
                     patch.object(viewer.p, 'hide_lattice'), \
                     patch.object(viewer.p, 'load_image', return_value=types.SimpleNamespace(w=399, h=525)), \
                     patch.object(viewer, 'optional_font', return_value=None), \
                     patch.object(viewer.p, 'get_events', return_value=[event]):
                    viewer.main()
                    close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
