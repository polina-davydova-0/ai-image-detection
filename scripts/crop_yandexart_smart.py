import os
from PIL import Image
from tqdm import tqdm

# Путь к исходным картинкам с водяным знаком (JPG)
INPUT_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\ai\uncompressed\yandexart"
# Куда сохранять чистые фрагменты
OUTPUT_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\ai\tiles_256\yandexart"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TILE_SIZE = 256
OVERLAP = 64
step = TILE_SIZE - OVERLAP

# Примерные размеры области водяного знака (в пикселях от правого нижнего угла)
WM_WIDTH = 300
WM_HEIGHT = 80

files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
print(f"Найдено изображений YandexART: {len(files)}")

saved_count = 0
skipped_count = 0

for fname in tqdm(files):
    path = os.path.join(INPUT_DIR, fname)
    img = Image.open(path).convert('RGB')
    w, h = img.size
    
    # Координаты области водяного знака
    wm_x1 = w - WM_WIDTH
    wm_y1 = h - WM_HEIGHT
    wm_x2 = w
    wm_y2 = h

    for y in range(0, h - TILE_SIZE + 1, step):
        for x in range(0, w - TILE_SIZE + 1, step):
            x2 = x + TILE_SIZE
            y2 = y + TILE_SIZE
            
            # Проверяем, пересекается ли текущий фрагмент с водяным знаком
            # Логика пересечения прямоугольников: 
            # Если левый край фрагмента левее правого края ВЗ И правый край фрагмента правее левого края ВЗ
            # и аналогично по Y.
            overlaps_watermark = (x < wm_x2 and x2 > wm_x1 and y < wm_y2 and y2 > wm_y1)
            
            if overlaps_watermark:
                skipped_count += 1
                continue # Пропускаем этот фрагмент, не сохраняем
                
            # Если пересечения нет — сохраняем
            tile = img.crop((x, y, x2, y2))
            # Сохраняем в PNG, чтобы не было двойного сжатия
            tile_name = f"yandexart_{fname.split('.')[0]}_{x}_{y}.png"
            tile.save(os.path.join(OUTPUT_DIR, tile_name))
            saved_count += 1

print(f"Готово!")
print(f"Сохранено чистых фрагментов: {saved_count}")
print(f"Пропущено (с водяным знаком): {skipped_count}")