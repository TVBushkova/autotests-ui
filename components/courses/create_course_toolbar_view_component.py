import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-title-text', 'Title')
        self.create_course_button = Button(page, f'{identifier}-create-course-button', 'Create Course')

    @allure.step('Check visible create course toolbar')
    def check_visible(self, is_create_course_disabled: bool = True):
        self.title.check_visible()
        self.title.check_have_text('Create course')
        if is_create_course_disabled:
            self.create_course_button.check_disabled()

        if not is_create_course_disabled:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()

