from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = page.get_by_test_id(f'{identifier}-title-text')
        self.create_course_button = page.get_by_test_id(f'{identifier}-create-course-button')

    def check_visible(self, is_create_course_disabled: bool = True):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Create course')
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()

        if not is_create_course_disabled:
            expect(self.create_course_button).not_to_be_disabled()

    def click_create_course_button(self):
        self.create_course_button.click()

