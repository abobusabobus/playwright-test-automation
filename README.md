playwright-test-automation
Автоматизация UI тестирования главной страницы effective-mobile.ru
Описание проекта
Автоматизированные UI тесты написаны с использованием Python + Playwright. Применён паттерн Page Object для улучшенной поддержки тестов. Для отчетов используется Allure.

Структура
tests/ — тестовые сценарии

pages/ — Page Object классы

requirements.txt — зависимости Python

Dockerfile — сборочный скрипт окружения

docker-compose.yml — запуск тестов и отчетов в контейнерах

pytest.ini — конфигурация pytest (если есть)

README.md — этот файл

Требования
Python 3.10 и выше

Playwright

Allure (для отчетов)

Docker (опционально)

Установка локально

git clone https://github.com/abobusabobus/playwright-test-automation.git
cd playwright-test-automation

python -m venv venv
.\venv\Scripts\activate       # Windows
source venv/bin/activate      # Linux/Mac

pip install -r requirements.txt
playwright install
Запуск тестов

pytest -v --alluredir=allure-results
allure serve allure-results
Запуск через Docker

docker-compose build
docker-compose up playwright-tests
docker-compose up allure-report
Отчёты доступны по адресу http://localhost:5050

Что тестируется
Навигация по разделам сайта

Проверка видимости основных элементов

Генерация отчетов Allure с графической информацией

Исключения из репозитория
Папка venv/ для виртуального окружения не добавлена — добавлен .gitignore

Все зависимости описаны в requirements.txt

Автор и контакты
GitHub: https://github.com/abobusabobus

Логин: LyakishEg

Быстрый старт (TL;DR)
git clone https://github.com/abobusabobus/playwright-test-automation.git
cd playwright-test-automation
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest -v --alluredir=allure-results
allure serve allure-results
