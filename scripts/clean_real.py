import os
import numpy as np
from PIL import Image
from tqdm import tqdm

TILES_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\real\tiles_256"
LOG_FILE = r"C:\Users\polina\Desktop\нир_упб\AI_Research\real\compressed_real.txt" # Файл лога

# Пороги: 
BRIGHTNESS_THRESHOLD = 25
STD_THRESHOLD = 15

# Читаем лог (файлы, которые уже сжаты и проверены)
processed = set()
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        processed = set(line.strip() for line in f if line.strip())

# Берем только те PNG, которых нет в логе (то есть новые)
all_files = [f for f in os.listdir(TILES_DIR) if f.lower().endswith('.png')]
new_files = [f for f in all_files if f not in processed]

print(f"Всего фрагментов: {len(all_files)}. Новых для проверки: {len(new_files)}")

deleted_count = 0
for fname in tqdm(new_files):
    path = os.path.join(TILES_DIR, fname)
    try:
        img = np.array(Image.open(path).convert('L')) # В оттенки серого
        mean_brightness = np.mean(img)
        std_dev = np.std(img)
        
        if mean_brightness < BRIGHTNESS_THRESHOLD or std_dev < STD_THRESHOLD:
            os.remove(path)
            deleted_count += 1
    except Exception as e:
        print(f"Ошибка с {fname}: {e}")

print(f"Удалено {deleted_count} темных/однотонных фрагментов из новых.")