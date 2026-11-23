import os
from PIL import Image
from tqdm import tqdm

INPUT_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\real\uncompressed"
OUTPUT_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\real\tiles_256"
LOG_FILE = r"C:\Users\polina\Desktop\нир_упб\AI_Research\real\processed_real.txt"

os.makedirs(OUTPUT_DIR, exist_ok=True)
TILE_SIZE = 256
OVERLAP = 64

# Просто читаем лог 
processed = set()
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        processed = set(line.strip() for line in f if line.strip())

files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.tiff', '.tif'))]
new_files = [f for f in files if f not in processed]

print(f"Всего TIFF: {len(files)}. Новых для нарезки: {len(new_files)}")

if new_files:
    # Ищем максимальный номер, чтобы не перезаписать старые
    existing_tiles = [f for f in os.listdir(OUTPUT_DIR) if f.startswith('real_') and f.endswith('.png')]
    if existing_tiles:
        last_num = max(int(f.split('_')[1].split('.')[0]) for f in existing_tiles)
        counter = last_num + 1
    else:
        counter = 0

    for fname in tqdm(new_files):
        path = os.path.join(INPUT_DIR, fname)
        try:
            img = Image.open(path)
            w, h = img.size
            step = TILE_SIZE - OVERLAP

            for y in range(0, h - TILE_SIZE + 1, step):
                for x in range(0, w - TILE_SIZE + 1, step):
                    tile = img.crop((x, y, x + TILE_SIZE, y + TILE_SIZE))
                    tile.save(os.path.join(OUTPUT_DIR, f"real_{counter:06d}.png"))
                    counter += 1
            
            # Записываем в лог
            with open(LOG_FILE, 'a', encoding='utf-8') as f:
                f.write(f"{fname}\n")
                
        except Exception as e:
            print(f"Ошибка с {fname}: {e}")

    print(f"Готово! Нарезаны новые фрагменты.")
else:
    print("Нет новых файлов для обработки.")