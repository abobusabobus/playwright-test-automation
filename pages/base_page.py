from playwright.sync_api import Page
import allure


class BasePage:
    
    def __init__(self, page: Page):
        self.page = page
    
    @allure.step("Переход на URL: {url}")
    def navigate(self, url: str):
        self.page.goto(url, timeout=10000)
    
    @allure.step("Проверка текущего URL")
    def get_current_url(self) -> str:
        return self.page.url
    
    @allure.step("Скриншот страницы")
    def take_screenshot(self, name: str):
        screenshot_bytes = self.page.screenshot()
        allure.attach(
            screenshot_bytes,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )