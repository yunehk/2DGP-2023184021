"""Compatibility entry point; the assignment lives in Labs/LEC08."""
from pathlib import Path
import runpy
import sys

folder = Path(__file__).resolve().parent.parent / 'LEC08'
sys.path.insert(0, str(folder))
if __name__ == '__main__':
    runpy.run_path(str(folder / 'animation_viewer.py'), run_name='__main__')
