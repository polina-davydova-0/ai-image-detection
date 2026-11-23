import os
from PIL import Image
from tqdm import tqdm

INPUT_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\ai\uncompressed"
OUTPUT_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\ai\tiles_256"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TILE_SIZE = 256
OVERLAP = 64

files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
print(f"Найдено AI-изображений: {len(files)}")

counter = 0
for fname in tqdm(files):
    path = os.path.join(INPUT_DIR, fname)
    img = Image.open(path)
    w, h = img.size
    step = TILE_SIZE - OVERLAP

    for y in range(0, h - TILE_SIZE + 1, step):
        for x in range(0, w - TILE_SIZE + 1, step):
            tile = img.crop((x, y, x + TILE_SIZE, y + TILE_SIZE))
            tile.save(os.path.join(OUTPUT_DIR, f"ai_{counter:06d}.png"))
            counter += 1

print(f"Готово! Нарезано {counter} фрагментов из AI-изображений.")