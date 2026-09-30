import json
from pathlib import Path
import tempfile
import unittest

from animation_data import load_animations


class AnimationDataTests(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).with_name('sonic_frames.json')
        self.data, self.animations = load_animations(self.path)

    def test_four_motions_and_different_frame_counts(self):
        self.assertEqual([a.name for a in self.animations],
                         ['walk', 'run', 'spin', 'tumble'])
        self.assertEqual([len(a.frames) for a in self.animations], [8, 12, 9, 8])

    def test_genuinely_different_source_sizes(self):
        sizes = {(f.width, f.height) for a in self.animations for f in a.frames}
        self.assertGreater(len(sizes), 10)

    def test_out_of_bounds_rejected(self):
        self.data['animations'][0]['frames'][0]['x'] = self.data['image_width']
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'bad.json'
            path.write_text(json.dumps(self.data))
            with self.assertRaises(ValueError):
                load_animations(path)

    def test_empty_animation_rejected(self):
        self.data['animations'][0]['frames'] = []
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'bad.json'
            path.write_text(json.dumps(self.data))
            with self.assertRaises(ValueError):
                load_animations(path)


if __name__ == '__main__':
    unittest.main()
