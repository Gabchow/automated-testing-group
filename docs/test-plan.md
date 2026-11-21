# Group test choices

Each member creates two additional tests and captures their own PNG for each.
Prefer different scenarios. Record unavoidable repeats and meaningful code differences.
Cosmetic changes to copied code are not sufficient.

| Member | First scenario | Second scenario | Evidence folder |
| --- | --- | --- | --- |
| 1 | | | `docs/evidence/member-1/` |
| 2 | | | `docs/evidence/member-2/` |
| 3 | | | `docs/evidence/member-3/` |
| 4, if present | | | `docs/evidence/member-4/` |
| 5, if present | | | `docs/evidence/member-5/` |

## Unavoidable repeats, if any

| Scenario | Members | Why no suitable alternative is available | Meaningful implementation differences |
| --- | --- | --- | --- |

# Group Test Choices

Each member must complete two additional automated tests beyond the eight guided cases.

| Member | First Scenario | Second Scenario | Evidence Folder |
|---|---|---|---|
| 1 | To be confirmed | To be confirmed | `docs/evidence/member-1/` |
| 2 | To be confirmed | To be confirmed | `docs/evidence/member-2/` |
| 3 | To be confirmed | To be confirmed | `docs/evidence/member-3/` |
| 4 | To be confirmed | To be confirmed | `docs/evidence/member-4/` |
| 5 | Refresh after adding tasks | Cancel task editing with Escape | `docs/evidence/member-5/` |

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

## Unavoidable Repeats

No repeats confirmed. The group must check all members' additional scenarios before final submission.
