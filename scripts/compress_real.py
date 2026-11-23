import os
from PIL import Image
from tqdm import tqdm

SOURCE_DIR = r"C:\Users\polina\Desktop\нир_упб\AI_Research\real\tiles_256"
LOG_FILE = r"C:\Users\polina\Desktop\нир_упб\AI_Research\real\compressed_real.txt"
QUALITIES = [95, 90, 80]

# Просто читаем лог 
compressed = set()
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        compressed = set(line.strip() for line in f if line.strip())

all_files = [f for f in os.listdir(SOURCE_DIR) if f.lower().endswith('.png')]
new_files = [f for f in all_files if f not in compressed]

print(f"Всего реальных фрагментов: {len(all_files)}. Новых для сжатия: {len(new_files)}")

if new_files:
    for q in QUALITIES:
        out_dir = rf"C:\Users\polina\Desktop\нир_упб\AI_Research\real\jpeg_{q}"
        os.makedirs(out_dir, exist_ok=True)
        
        for fname in tqdm(new_files, desc=f"Real JPEG {q}%"):
            img = Image.open(os.path.join(SOURCE_DIR, fname)).convert('RGB')
            out_name = os.path.splitext(fname)[0] + '.jpg'
            img.save(os.path.join(out_dir, out_name), "JPEG", quality=q, optimize=True)
            
    # Записываем в лог
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        for fname in new_files:
            f.write(f"{fname}\n")
    print("Готово! Новые фрагменты сжаты и добавлены в общие папки.")
else:
    print("Нет новых фрагментов для сжатия.")