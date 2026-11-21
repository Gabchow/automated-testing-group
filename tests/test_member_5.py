import pytest

from playwright.sync_api import Page, expect

URL = "https://demo.playwright.dev/todomvc/"


def test_add_task(page: Page):
    page.goto(URL)

    task_input = page.get_by_placeholder(
        "What needs to be done?",
        exact=True,
    )
    task_items = page.locator(".todo-list li")
    task_labels = task_items.locator("label")

    expect(task_items).to_have_count(0)

    task_input.fill("Read testing notes")
    task_input.press("Enter")

    expect(task_items).to_have_count(1)
    expect(task_labels).to_have_text(["Read testing notes"])
    expect(task_input).to_have_value("")


def test_complete_task(page: Page):
    page.goto(URL)

    task_input = page.get_by_placeholder(
        "What needs to be done?",
        exact=True,
    )
    task_items = page.locator(".todo-list li")

    expect(task_items).to_have_count(0)

    task_input.fill("Practise automated testing")
    task_input.press("Enter")

    expect(task_items).to_have_count(1)

    checkbox = task_items.first.get_by_role("checkbox")
    checkbox.check()
    expect(checkbox).to_be_checked()

    page.get_by_role(
        "link", name="Completed", exact=True
    ).click()

    expect(task_items).to_have_count(1)
    expect(task_items.locator("label")).to_have_text(
        ["Practise automated testing"]
    )


@pytest.mark.parametrize(
    "task_text",
    ["", " ", "   "],
    ids=["empty", "one-space", "three-spaces"],
)
def test_blank_task_is_not_added(page: Page, task_text: str):
    page.goto(URL)

    task_input = page.get_by_placeholder(
        "What needs to be done?",
        exact=True,
    )
    task_items = page.locator(".todo-list li")

    expect(task_items).to_have_count(0)

    task_input.fill(task_text)
    task_input.press("Enter")

    expect(task_items).to_have_count(0)


def test_login_with_correct_details(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_role(
            "heading",
            name="Secure Area",
            exact=True,
        )
    ).to_be_visible()


def test_login_with_incorrect_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("WrongPassword123")
    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Your password is invalid!")
    ).to_be_visible()

    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()


def add_task(page: Page, task_name: str):
    task_input = page.get_by_placeholder(
        "What needs to be done?",
        exact=True,
    )
    task_input.fill(task_name)
    task_input.press("Enter")


def test_add_two_tasks(page: Page):
    page.goto(URL)
    task_items = page.locator(".todo-list li")

    expect(task_items).to_have_count(0)

    add_task(page, "Read the instructions")
    add_task(page, "Practise the examples")

    expect(task_items).to_have_count(2)
    expect(task_items.locator("label")).to_have_text(
        ["Read the instructions", "Practise the examples"]
    )


def test_task_persists_after_refresh(page: Page):
    page.goto(URL)

    task_items = page.locator(".todo-list li")
    expect(task_items).to_have_count(0)

    add_task(page, "Prepare project presentation")
    add_task(page, "Review project documentation")

    expect(task_items).to_have_count(2)

    # Refresh the browser
    page.reload()

    # Verify both tasks remain after refreshing
    expect(task_items).to_have_count(2)
    expect(task_items.locator("label")).to_have_text([
        "Prepare project presentation",
        "Review project documentation"
    ])

    # Capture Member 5 evidence
    page.screenshot(
        path="docs/evidence/member-5/extra-test-1-refresh.png",
        full_page=True
    )


def test_cancel_task_edit_with_escape(page: Page):
    page.goto(URL)

    task_items = page.locator(".todo-list li")
    expect(task_items).to_have_count(0)

    add_task(page, "Prepare testing report")

    task_label = task_items.locator("label")
    expect(task_label).to_have_text(["Prepare testing report"])

    # Double-click the task to edit it
    task_label.dblclick()

    # Enter a different task name
    edit_input = task_items.locator("input.edit")
    expect(edit_input).to_be_visible()
    edit_input.fill("Modified testing report")

    # Press Escape to cancel editing
    edit_input.press("Escape")

    # Original task must remain unchanged
    expect(task_label).to_have_text(["Prepare testing report"])
    expect(edit_input).not_to_be_visible()
    expect(task_items).to_have_count(1)

    # Capture final evidence
    page.screenshot(
        path="docs/evidence/member-5/extra-test-2-cancel-edit.png",
        full_page=True
    )
