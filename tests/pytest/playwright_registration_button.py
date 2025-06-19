from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    expect(registration_button).to_be_disabled()

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    username_input.fill("username")

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("password")

    expect(registration_button).not_to_be_disabled()

    page.wait_for_timeout(5000)