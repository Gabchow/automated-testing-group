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

    page.get_by_role("link", name="Completed", exact=True).click()

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



### EXTRA TEST 1 ###
# Scenario: Deleting a task removes it from the list.
# Condition: Fresh session and empty list.
# Values: "Study Python" and "Complete assignment".
# Description: Add both tasks, then delete "Study Python".
# Expected outcome: Only "Complete assignment" remains.
def test_delete_active_task(page: Page):
    page.goto(URL)

    task_items = page.locator(".todo-list li")

    # Add two tasks
    add_task(page, "Study Python")
    add_task(page, "Complete assignment")

    # Verify both exist
    expect(task_items).to_have_count(2)

    # Delete the first task
    first_task = task_items.filter(has_text="Study Python")
    first_task.hover()
    first_task.locator(".destroy").click()

    # Verify only the second task remains
    expect(task_items).to_have_count(1)
    expect(task_items.locator("label")).to_have_text(
        ["Complete assignment"]
    )

    # Save screenshot evidence
    page.screenshot(
        path="docs/evidence/member-2/extra-test-1-delete-task.png",
        full_page=True,
    )



### EXTRA TEST 2 ###
# Scenario: Active shows unfinished tasks only.
# Condition: Fresh session and empty list.
# Values: "Revise DevOps" and "Submit homework".
# Description: Add both tasks, complete the first, then select Active.
# Expected outcome: Only "Submit homework" appears.
def test_active_filter(page: Page):
    page.goto(URL)

    task_items = page.locator(".todo-list li")

    # Add two tasks
    add_task(page, "Revise DevOps")
    add_task(page, "Submit homework")

    # Verify both tasks were added
    expect(task_items).to_have_count(2)

    # Mark the first task as completed
    first_task = task_items.filter(has_text="Revise DevOps")
    first_task.get_by_role("checkbox").check()

    # Verify task is completed
    expect(first_task.get_by_role("checkbox")).to_be_checked()

    # Select the Active filter
    page.get_by_role(
        "link", name="Active", exact=True
    ).click()

    # Only the unfinished task should appear
    expect(task_items).to_have_count(1)
    expect(task_items.locator("label")).to_have_text(
        ["Submit homework"]
    )

    # Save screenshot evidence
    page.screenshot(
        path="docs/evidence/member-2/extra-test-2-active-filter.png",
        full_page=True,
    )
