# Group Test Choices

Each member must complete two additional automated tests beyond the eight guided cases.

| Member | First Scenario | Second Scenario | Evidence Folder |
|---|---|---|---|
| 1 | Save edited task using Enter | Mark all tasks as complete | `docs/evidence/member-1/` |
| 2 | Delete an active task | Clear completed tasks while keeping unfinished tasks | `docs/evidence/member-2/` |
| 3 | Tasks remain after refreshing the page | Cancel task editing using Escape | `docs/evidence/member-3/` |
| 4 | Active filter shows unfinished tasks only | Reject login with an incorrect username | `docs/evidence/member-4/` |
| 5 | Tasks remain after refreshing the page | Cancel task editing using Escape | `docs/evidence/member-5/` |

## Unavoidable Repeats

No repeats confirmed. The group must check all members' additional scenarios before final submission.



## Member 2 Additional Test Details

### Test 1: Delete an Active Task
- Test function: `test_delete_active_task`
- Description: Add two tasks, delete "Study Python", and verify that the other task remains.
- Expected result: "Study Python" is removed and only "Complete assignment" remains.
- Actual result: Passed in the previous Member 2 run; reconfirm after the final group run.
- Evidence: `docs/evidence/member-2/extra-test-1-delete-task.png`
### Test 2: Clear Completed Tasks
- Test function: `test_clear_completed_tasks`
- Description: Add three tasks, mark "Study Python" and "Finish assignment" as completed, then click Clear completed.
- Expected result: Both completed tasks are removed, and only the unfinished task, "Revise DevOps", remains.
- Actual result: To confirm after running the replacement test.
- Evidence: `docs/evidence/member-2/extra-test-2-clear-completed.png`


## Member 5 Additional Test Details

### Test 1: Refresh Persistence
- Test function: `test_task_persists_after_refresh`
- Description: Add two tasks, refresh the browser, and verify both tasks remain.
- Expected result: Both tasks remain visible after refreshing.
- Actual result: Passed.
- Evidence: `docs/evidence/member-5/extra-test-1-refresh.png`

### Test 2: Cancel Task Editing
- Test function: `test_cancel_task_edit_with_escape`
- Description: Edit an existing task and press Escape.
- Expected result: Editing is cancelled and the original task name remains unchanged.
- Actual result: Passed.
- Evidence: `docs/evidence/member-5/extra-test-2-cancel-edit.png`

