FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy

WORKDIR /app

# Устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем браузеры Playwright
RUN playwright install chromium firefox webkit

# Копируем весь проект
COPY . .

# Создаем директории для результатов
RUN mkdir -p allure-results allure-report videos

# Команда по умолчанию для запуска тестов
CMD ["pytest", "-v", "--browser", "chromium", "--alluredir=allure-results"]
