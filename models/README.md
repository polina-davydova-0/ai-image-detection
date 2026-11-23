# Модели детекторов, использованные в работе

## 1. Обученные модели на базе ResNet50V2 (Семестр 7)

Из-за ограничения GitHub на размер загружаемых файлов (до 25 МБ через веб-интерфейс) веса моделей, обученных в рамках работы, размещены на Google Диске:

* **Ссылка для скачивания весов:** [dataset_extended (Google Диск)](https://drive.google.com/drive/folders/1ILgTBHOLH9Nm1rqpZAKv0NRrubqx_kR6?usp=sharing)

| Файл модели | Размер | Задача | Архитектура выхода | Точность (Accuracy) |
| :--- | :---: | :--- | :--- | :---: |
| `best_ai_detector.keras` | 91,3 МБ | Бинарная классификация (`Real` vs `Fake`) | `Dense(32, relu)` + `Dense(1, sigmoid)` | **95,84%** |
| `model_multi.keras` | 92,0 МБ | Атрибуция источника (7 классов: `Real` + 6 генераторов) | `Dense(64, relu)` + `Dense(7, softmax)` | **94,43%** |

### Как загрузить обученную модель в Python (TensorFlow / Keras)

```python
import tensorflow as tf

# Пример загрузки бинарного детектора
model = tf.keras.models.load_model('best_ai_detector.keras')
```

---

## 2. Предобученные детекторы с Hugging Face Hub (этап сравнительного анализа)

Все три готовых детектора загружаются с Hugging Face Hub через библиотеку `transformers`.

| Детектор | Hugging Face ID | Ссылка на модель |
| :--- | :--- | :--- |
| AIorNot-SigLIP2 | `prithivMLmods/AIorNot-SigLIP2` | [ссылка](https://huggingface.co/prithivMLmods/AIorNot-SigLIP2) |
| AI-image-detector | `umm-maybe/AI-image-detector` | [ссылка](https://huggingface.co/umm-maybe/AI-image-detector) |
| AI-vs-Deepfake-vs-Real-Siglip2 | `prithivMLmods/AI-vs-Deepfake-vs-Real-Siglip2` | [ссылка](https://huggingface.co/prithivMLmods/AI-vs-Deepfake-vs-Real-Siglip2) |

### Как загрузить любую из моделей Hugging Face

```python
from transformers import pipeline

# Пример загрузки AIorNot-SigLIP2
model = pipeline("image-classification", model="prithivMLmods/AIorNot-SigLIP2")
```
