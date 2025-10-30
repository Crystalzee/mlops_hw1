# ML Model API (MLOps HW1)

## Описание
REST API-сервис для обучения и использования ML-моделей.  
Реализованы функции:
- обучение (`/train`)
- предсказание (`/predict`)
- список моделей (`/models`)
- удаление модели (`/delete/{model_name}`)
- проверка состояния (`/health`)

## Запуск
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run app/dashboard.py