# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Открываем порт для FastAPI
EXPOSE 8080

# Запускаем uvicorn сервер
CMD ["uvicorn", "web_api:app", "--host", "0.0.0.0", "--port", "8080"]