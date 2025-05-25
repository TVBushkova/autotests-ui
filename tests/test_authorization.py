from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.authorisation
def test_wrong_email_or_password_authorization(initialize_browser_state: Page):
    initialize_browser_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = initialize_browser_state.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    password_input = initialize_browser_state.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill("password")

    login_button = initialize_browser_state.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    wrong_email_or_password_alert = initialize_browser_state.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")