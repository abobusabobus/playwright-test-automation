from playwright.sync_api import Page, expect
import allure
from .base_page import BasePage


class HomePage(BasePage):
    """Page Object для главной страницы effective-mobile.ru"""

    URL = "https://effective-mobile.ru"

    def __init__(self, page: Page):
        super().__init__(page)
        # Используем локаторы только для элементов, которые реально есть на сайте
        self.about_link = page.locator("a:visible:has-text('О нас')").first
        self.services_link = page.locator("a:visible:has-text('Услуги')").first
        self.contacts_link = page.locator("a:visible:has-text('Контакты')").first

    @allure.step("Открытие главной страницы")
    def open(self):
        """Открыть главную страницу"""
        self.navigate(self.URL)

    @allure.step("Клик по ссылке 'О нас'")
    def click_about(self):
        """Кликнуть на ссылку О нас"""
        self.about_link.click()

    @allure.step("Клик по ссылке 'Услуги'")
    def click_services(self):
        """Кликнуть на ссылку Услуги"""
        self.services_link.click()

    @allure.step("Клик по ссылке 'Контакты'")
    def click_contacts(self):
        """Кликнуть на ссылку Контакты"""
        self.contacts_link.click()

    @allure.step("Проверка видимости навигационного меню")
    def verify_navigation_menu(self):
        """Проверить, что все элементы навигации видимы"""
        expect(self.about_link).to_be_visible()
        expect(self.services_link).to_be_visible()
        expect(self.contacts_link).to_be_visible()
