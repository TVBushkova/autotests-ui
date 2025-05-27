import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()

pytest_plugins = (
    "fixtures.pages", # Подключаем фикстуры страниц
    "fixtures.browsers" # Подключали ранее в предыдущих уроках
)
