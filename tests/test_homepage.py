import pytest
import allure
from playwright.sync_api import Page, expect
from pages.homepage import HomePage


@allure.feature("Главная страница")
@allure.story("Навигация")
class TestHomePage:
    """Тесты для главной страницы effective-mobile.ru"""

    @allure.title("Проверка перехода по всем блокам навигации")
    @allure.description("Тест проверяет переходы по навигационным ссылкам: О нас, Услуги, Контакты")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigation_links(self, page: Page):
        """UI тест: проверка навигационных ссылок"""

        with allure.step("Инициализация HomePage"):
            home_page = HomePage(page)

        with allure.step("Открытие главной страницы"):
            home_page.open()
            page.wait_for_load_state("networkidle")
            allure.attach(
                home_page.get_current_url(),
                name="Current URL",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверка видимости навигационного меню"):
            home_page.verify_navigation_menu()
            home_page.take_screenshot("navigation_menu")

        with allure.step("Тест клика по 'О нас'"):
            home_page.click_about()
            page.wait_for_timeout(1000)
            home_page.take_screenshot("about_section")

        with allure.step("Тест клика по 'Услуги'"):
            home_page.click_services()
            page.wait_for_timeout(1000)
            home_page.take_screenshot("services_section")

        with allure.step("Тест клика по 'Контакты'"):
            home_page.click_contacts()
            page.wait_for_timeout(1000)
            home_page.take_screenshot("contacts_section")

        with allure.step("Проверка итогового URL"):
            current_url = home_page.get_current_url()
            assert "effective-mobile.ru" in current_url, \
                f"Ожидается URL с 'effective-mobile.ru', получен: {current_url}"

    @allure.title("Проверка загрузки главной страницы")
    @allure.description("Простой тест проверки успешной загрузки главной страницы")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_homepage_loads(self, page: Page):
        """UI тест: проверка загрузки главной страницы"""

        home_page = HomePage(page)

        with allure.step("Открытие главной страницы"):
            home_page.open()
            page.wait_for_load_state("networkidle")

        with allure.step("Проверка загрузки страницы"):
            expect(page).to_have_url("https://effective-mobile.ru/")
            home_page.take_screenshot("homepage_loaded")
