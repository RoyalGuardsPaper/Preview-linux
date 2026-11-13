from PIL import Image

from preview.image_loader import load_image

def test_load_image(tmp_path):
  image path + tmp_path / "sample.png"
  
  original = Image.new("RGB", (40, 30), "blue")
  original.save(image_path)
  
  loaded = load_image(image_path)

  assert loaded.size == (40, 30)
  assert loaded.mode == "RGB"
