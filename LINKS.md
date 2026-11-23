# Ссылки на базы данных

Из-за ограничений GitHub на размер файлов, сами изображения хранятся на Google Диске.
## Расширенная база данных `dataset_extended`

Основной набор данных для обучения, валидации и тестирования детекторов (15 524 фрагмента размером `256×256` пикселей: 8 068 реальных и 7 456 синтетических от 6 генераторов — SD 1.5, SDXL, StyleGAN2-ADA, DDPM, VAE, YandexART), а также сжатые выборки JPEG (95%, 90%, 80%) доступны на Google Диске:

* **Ссылка для скачивания:** [dataset_extended](https://drive.google.com/drive/folders/1ILgTBHOLH9Nm1rqpZAKv0NRrubqx_kR6?usp=sharing)
* **Состав архивов:**
  * `real_tiles.zip`, `ai_tiles.zip` — базовые фрагменты без сжатия (PNG).
  * `real_jpeg_95.zip`, `ai_jpeg_95.zip` — фрагменты со сжатием JPEG 95%.
  * `real_jpeg_90.zip`, `ai_jpeg_90.zip` — фрагменты со сжатием JPEG 90%.
  * `real_jpeg_80.zip`, `ai_jpeg_80.zip` — фрагменты со сжатием JPEG 80%.

---

База данных `my_own_dataset` (260 изображений, 224x224) доступна для скачивания по следующей ссылке:
https://drive.google.com/drive/folders/1mAEGlH-hix1FKf8BhjKUqnTfPGqbYy_8?usp=sharing


## Датасет Tiny GenImage

Tiny GenImage — это урезанная версия эталонного бенчмарка GenImage, использованная в работе для проверки обобщающей способности детекторов.

- **Источник:** [tiny-genimage на Kaggle](https://www.kaggle.com/datasets/yangsangtai/tiny-genimage/data)
- **Описание:** 5000 изображений (5000 real + 5000 fake) для каждого из 8 генеративных моделей (Midjourney, Stable Diffusion, BigGAN и др.). Изображения приведены к размеру 224×224 пикселя.
- **Использование в работе:** Из этого датасета были взяты выборки по 100 real и 100 fake для 7 генераторов (Midjourney, BigGAN, VQDM, Stable Diffusion v1.5, Glide, ADM).
  
