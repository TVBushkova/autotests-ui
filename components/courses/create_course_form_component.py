from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title_input = Input(page, f'{identifier}-title-input', 'Title Input')
        self.estimated_time_input = (
            Input(page,f'{identifier}-estimated-time-input', 'Estimated Time Input')
        )
        self.description_textarea = (
            Textarea(page, f'{identifier}-description-input', 'Description')
        )
        self.max_score_input = Input(page, f'{identifier}-max-score-input', 'Max Score')
        self.min_score_input = Input(page, f'{identifier}-min-score-input', 'Min Score')

    def check_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.title_input.check_visible()
        self.title_input.check_have_value(title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_have_value(description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(min_score)

    def fill(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.title_input.fill(title)
        self.title_input.check_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.fill(description)
        self.description_textarea.check_have_value(description)

        self.max_score_input.fill(max_score)
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.fill(min_score)
        self.min_score_input.check_have_value(min_score)