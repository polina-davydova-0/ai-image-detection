# Ссылки на базы данных

Из-за ограничений GitHub на размер файлов, сами изображения хранятся на Google Диске.

Полная база данных `my_own_dataset` (260 изображений, 224x224) доступна для скачивания по следующей ссылке:
https://drive.google.com/drive/folders/1mAEGlH-hix1FKf8BhjKUqnTfPGqbYy_8?usp=sharing


## Датасет Tiny GenImage

Tiny GenImage — это урезанная версия эталонного бенчмарка GenImage, использованная в работе для проверки обобщающей способности детекторов.

- **Источник:** [tiny-genimage на Kaggle](https://www.kaggle.com/datasets/yangsangtai/tiny-genimage/data)
- **Описание:** 5000 изображений (5000 real + 5000 fake) для каждого из 8 генеративных моделей (Midjourney, Stable Diffusion, BigGAN и др.). Изображения приведены к размеру 224×224 пикселя.
- **Использование в работе:** Из этого датасета были взяты выборки по 100 real и 100 fake для 7 генераторов (Midjourney, BigGAN, VQDM, Stable Diffusion v1.5, Glide, ADM).
  
