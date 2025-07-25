from config import settings
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from allure_commons.types import Severity

import pytest
import allure

from tools.roots import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.COURSES) # Добавили feature
@allure.story(AllureStory.COURSES) # Добавили story
@allure.suite(AllureFeature.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.sub_suite(AllureStory.COURSES)
class TestCourse:
    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.CREATE_COURSE)

        create_course_page.create_course_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.create_course_exercises_toolbar.check_visible()
        create_course_page.create_course_exercises_toolbar.click_create_exercise_button()

        create_course_page.create_course_form.check_visible(
            title='',
            description='',
            estimated_time='',
            max_score='0',
            min_score='0'
        )

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title='Playwright',
            description='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)  # Добавили severity
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)
        # Добавили проверку Navbar компонента на странице Courses
        courses_list_page.navbar.check_visible("username")
        # Добавили проверку Sidebar компонента на странице Courses
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)  # Добавили severity
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.CREATE_COURSE)

        create_course_page.create_course_exercises_toolbar.click_create_exercise_button()
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title='Playwright',
            description='Playwright',
            estimated_time='2 weeks',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title='Playwright_updated',
            description='Playwright_updated',
            estimated_time='5 weeks',
            max_score='245',
            min_score='101'
        )
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright_updated", max_score="245", min_score="101", estimated_time="5 weeks"
        )





