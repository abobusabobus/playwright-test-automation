import pytest
from playwright.sync_api import Page
import allure


@pytest.fixture(scope="function")
def page(page: Page):
    yield page
    # Teardown: делаем скриншот если тест упал
    if hasattr(page, 'video'):
        video_path = page.video.path()
        allure.attach.file(
            video_path,
            name="video",
            attachment_type=allure.attachment_type.WEBM
        )


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "record_video_dir": "videos/",
    }