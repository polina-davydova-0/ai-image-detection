# Модели детекторов, использованные в работе

Все три детектора загружаются с Hugging Face Hub через библиотеку `transformers`.

## Использованные модели

| Детектор | Hugging Face ID | Ссылка на модель |
|----------|----------------|------------------|
| AIorNot-SigLIP2 | `prithivMLmods/AIorNot-SigLIP2` | [ссылка](https://huggingface.co/prithivMLmods/AIorNot-SigLIP2) |
| AI-image-detector | `umm-maybe/AI-image-detector` | [ссылка](https://huggingface.co/umm-maybe/AI-image-detector) |
| AI-vs-Deepfake-vs-Real-Siglip2 | `prithivMLmods/AI-vs-Deepfake-vs-Real-Siglip2` | [ссылка](https://huggingface.co/prithivMLmods/AI-vs-Deepfake-vs-Real-Siglip2) |

## Как загрузить любую из моделей

```python
from transformers import pipeline

# Пример загрузки AIorNot-SigLIP2
model = pipeline("image-classification", model="prithivMLmods/AIorNot-SigLIP2")
