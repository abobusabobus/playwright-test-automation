Проект: playwright-test-automation
Автоматизация UI тестирования главной страницы effective-mobile.ru
Описание
Автоматизированные UI тесты на Python + Playwright для проверки главных разделов сайта effective-mobile.ru. В проекте реализован паттерн Page Object, интеграция с Allure для генерации отчетов, поддерживается запуск в Docker.

Структура проекта
tests/ — тесты (например, test_homepage.py)

pages/ — Page Object классы (homepage.py, base_page.py)

requirements.txt — зависимости Python

Dockerfile — инструкция сборки окружения

docker-compose.yml — быстрый запуск тестов и Allure через Docker

pytest.ini — (если есть) настройки pytest

README.md — эта инструкция

Требования
Python 3.10+

Playwright

Allure (для отчетов)

Docker (опционально)

Установка и запуск локально
Клонируйте проект:

git clone https://github.com/abobusabobus/playwright-test-automation.git
cd playwright-test-automation
Cоздайте виртуальное окружение и активируйте:

python -m venv venv
.\venv\Scripts\activate         # Windows
source venv/bin/activate        # Linux/Mac
Установите зависимости:

pip install -r requirements.txt
playwright install
Запустите тесты и соберите Allure-отчёт:

pytest -v --alluredir=allure-results
allure serve allure-results
Запуск с помощью Docker
Соберите контейнер:

docker-compose build
Запустите тесты:

docker-compose up playwright-tests
Для отчета Allure:

docker-compose up allure-report
Откройте http://localhost:5050

Что тестируется
Проверка переходов по главным навигационным разделам (“О нас”, “Услуги”, “Контакты”)

Проверка видимости и доступности основных элементов страницы

Поддержка отчётов Allure с шагами и скриншотами

Автор
GitHub: abobusabobus

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
