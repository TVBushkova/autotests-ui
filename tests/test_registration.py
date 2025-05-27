from playwright.sync_api import Page, expect

from fixtures.pages import dashboard_page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
import pytest

@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("user.name@gmail.com", "username", "password")
    ]
)
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, email: str, username: str, password:str):  # Создаем тестовую функцию
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email, username=username, password=password)
    # Нажимаем кнопку "Registration"
    registration_page.click_registration_button()
    dashboard_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page.check_dashboard_title()

