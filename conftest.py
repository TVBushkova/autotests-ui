import pytest

pytest_plugins = (
    "fixtures.pages", # Подключаем фикстуры страниц
    "fixtures.allure",
    "fixtures.browsers" # Подключали ранее в предыдущих уроках
)