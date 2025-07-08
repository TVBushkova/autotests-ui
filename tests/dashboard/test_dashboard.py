import pytest
import allure
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from tools.roots import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.DASHBOARD) # Добавили feature
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
# Добавили story
class TestDashboard:
    @allure.title("Check displaying of dashboard page")
    @allure.severity(Severity.NORMAL)  # Добавили severity
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)

        # Добавили проверку Navbar компонента на странице Dashboard
        dashboard_page_with_state.navbar.check_visible("username")
        # Добавили проверку Sidebar компонента на странице Dashboard
        dashboard_page_with_state.sidebar.check_visible()

        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.scores_chart_view.check_visible("Scores")
        dashboard_page_with_state.students_chart_view.check_visible("Students")
        dashboard_page_with_state.activities_chart_view.check_visible("Activities")
        dashboard_page_with_state.courses_chart_view.check_visible("Courses")
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
