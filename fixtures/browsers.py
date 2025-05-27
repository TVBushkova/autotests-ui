import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("password")

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()
    context.storage_state(path="browser-state.json")
    browser.close()

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()