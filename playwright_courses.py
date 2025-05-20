from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    #Сохранеятся состояние браузера
    context.storage_state(path="browser-state.json")

    #Открывается страница курсов без повторной авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    #Проверяется заголовок раздела
    courses_toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_toolbar_title).to_be_visible()
    expect(courses_toolbar_title).to_have_text("Courses")

    # Проверяется наличие иконки
    courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    # Проверяется текст заголовка при отсутствии курсов
    courses_empty_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_empty_list_title).to_be_visible()
    expect(courses_empty_list_title).to_have_text("There is no results")

    # Проверяется описание раздела при отсутствии курсов
    courses_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_description).to_be_visible()
    expect(courses_description).to_have_text("Results from the load test pipeline will be displayed here")

    page.wait_for_timeout(5000)