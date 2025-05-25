from playwright.sync_api import Page, expect
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):  # Создаем тестовую функцию
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = chromium_page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    username_input = chromium_page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")

    password_input = chromium_page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("password")

    registration_button = chromium_page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    dashboard_title = chromium_page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")