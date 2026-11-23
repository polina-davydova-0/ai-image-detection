import os
import shutil
from PIL import Image
from tqdm import tqdm

SOURCE_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\ai\tiles_256"
QUALITIES = [95, 90, 80]
GENERATORS = ['ddpm'] 

# # Удаляем старые папки со сжатием
# for q in QUALITIES:
#     old_dir = rf"C:\Users\polina\Desktop\нир_упб\AI_Research\ai\jpeg_{q}"
#     if os.path.exists(old_dir):
#         shutil.rmtree(old_dir)
#         print(f"Удалена старая папка jpeg_{q}")

# Проходим по каждой подпапке-генератору
for gen in GENERATORS:
    src_path = os.path.join(SOURCE_DIR, gen)
    if not os.path.exists(src_path):
        continue
    
    files = [f for f in os.listdir(src_path) if f.endswith('.png')]
    if not files:
        print(f"{gen}: пусто, пропускаем")
        continue

    print(f"\n{gen}: {len(files)} файлов")
    
    for q in QUALITIES:
        # Создаем папку jpeg_95/sd15, jpeg_95/sdxl и т.д.
        out_dir = rf"C:\Users\polina\Desktop\нир_упб\AI_Research\ai\jpeg_{q}\{gen}"
        os.makedirs(out_dir, exist_ok=True)
        
        for fname in tqdm(files, desc=f"{gen} JPEG {q}%"):
            img = Image.open(os.path.join(src_path, fname)).convert('RGB')
            out_name = os.path.splitext(fname)[0] + '.jpg'
            img.save(os.path.join(out_dir, out_name), "JPEG", quality=q, optimize=True)

print("\nГотово! Сжатые версии для ddpm созданы.")