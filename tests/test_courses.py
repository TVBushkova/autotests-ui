from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title='',
        description='',
        estimated_time='',
        max_score='0',
        min_score='0'
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image(file='./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title='Playwright',
        description='Playwright',
        estimated_time='2 weeks',
        max_score='100',
        min_score='10'
    )
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index='0',
        title='Playwright',
        estimated_time='2 weeks',
        max_score='100',
        min_score='10'
    )


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    # Добавили проверку Navbar компонента на странице Courses
    courses_list_page.navbar.check_visible("username")
    # Добавили проверку Sidebar компонента на странице Courses
    courses_list_page.sidebar.check_visible()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()

