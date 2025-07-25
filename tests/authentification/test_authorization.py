import allure
import pytest
import allure_pytest

from config import settings
from pages.authentification.login_page import LoginPage
from pages.authentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity

from tools.roots import AppRoute


@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.AUTHORIZATION) # Добавили story
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @allure.title("User login with correct email and password")
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage,
            login_page: LoginPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()
        login_page.login_form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.title('User gets login with wrong email or password')
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title("Navigation from login page to registration page")
    @allure.tag(AllureTag.NAVIGATION)
    @allure.severity(Severity.NORMAL)  # Добавили severity
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email="", username="", password="")