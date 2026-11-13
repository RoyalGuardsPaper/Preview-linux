# image loading helpers
from pathlib import Path

from PIL import Image

def load_image(path: str | Path) -> Image.Image:
  # Open image file and return it as a pillow image
  image = Image.open(path)
  image.load()
  return image
