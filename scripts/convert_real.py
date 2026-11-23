import os
import rawpy
import imageio.v3 as iio
from tqdm import tqdm

INPUT_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\raw_photos"
OUTPUT_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\real\uncompressed"
os.makedirs(OUTPUT_DIR, exist_ok=True)

dng_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.dng') and not f.startswith('.')]
print(f"Найдено DNG-файлов: {len(dng_files)}")

for fname in tqdm(dng_files):
    path = os.path.join(INPUT_DIR, fname)
    try:
        with rawpy.imread(path) as raw:
            # Извлекаем сырые данные без сжатия и гамма-коррекции
            rgb = raw.postprocess(
                gamma=(2.2, 2.2),        
                no_auto_bright=False, 
                output_bps=8        # 8 бит на канал (чтобы TIFF не был слишком огромным)
            )
        out_path = os.path.join(OUTPUT_DIR, os.path.splitext(fname)[0] + '.tiff')
        iio.imwrite(out_path, rgb)
    except Exception as e:
        print(f"Ошибка с {fname}: {e}")

print("Готово! Все DNG конвертированы в TIFF.")