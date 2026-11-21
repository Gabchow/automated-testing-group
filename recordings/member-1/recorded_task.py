import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").fill("try the recorder")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    expect(page.get_by_test_id("todo-title")).to_contain_text("try the recorder")
