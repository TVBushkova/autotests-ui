from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    #1
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    #2
    create_course_page.check_visible_create_course_title()
    #3
    create_course_page.check_disabled_create_course_button()
    #4
    create_course_page.check_visible_image_preview_empty_view()
    #5
    create_course_page.check_visible_image_upload_view()
    #6
    create_course_page.check_visible_create_course_form(title='', description='', estimated_time='', max_score='0', min_score='0')
    #7
    create_course_page.check_visible_exercises_title()
    #8
    create_course_page.check_visible_create_exercise_button()
    #9
    create_course_page.check_visible_exercises_empty_view()
    #10
    create_course_page.upload_preview_image(file='./testdata/files/image.png')
    #11
    create_course_page.check_visible_image_upload_view()
    #12
    create_course_page.fill_create_course_form(title='Playwright', description='Playwright', estimated_time='2 weeks', max_score='100', min_score='10')
    #13
    create_course_page.click_create_course_button()
    #14
    courses_list_page.check_visible_courses_title()
    #15
    courses_list_page.check_visible_create_course_button()
    #16
    courses_list_page.check_visible_course_card(index='0', title='Playwright', estimated_time='2 weeks', max_score='100', min_score='10')


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    empty_view_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text('There is no results')

    empty_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')
