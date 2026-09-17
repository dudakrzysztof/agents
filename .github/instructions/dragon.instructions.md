# Dragon Project Instructions

## Scope and sources of truth

The Dragon project is an MVP business-requirements exercise, not game
development. Keep the sources of truth separate:

- `.github/copilot-instructions.md` contains repository-wide engineering rules.
- The selected `.github/instructions/sprint/sprint-NN.md` contains the
  sprint-specific behavior and acceptance scenario.
- The agent files in `.github/agents/` define role ownership and handoffs.
- `.github/prompts/my-prompt.prompt.md` defines the structure of an
  implementation brief.
- This file defines the shared project workflow and delivery policy.

Sprint requirements are cumulative: a new sprint adds to the previous behavior
unless it explicitly changes it. If a sprint file is missing, ask the user to
create it; do not fetch requirements from the web.

## Workflow

1. **Establish the baseline.** Review `dragon/README.md`, the relevant
   implementation, and existing tests. From the repository root, run:
   `python -m unittest dragon.dragon_tests -v`. Report pre-existing failures
   before proceeding.
2. **Define the scope.** Read the selected sprint file and prepare a concise
   brief with the prompt template. The sprint file is authoritative for the
   requested behavior.
3. **Implement.** Developer owns the production implementation phase.
4. **Verify.** Tester owns test changes and the relevant existing test suite.
5. **Finalize.** Orchestrator reviews the diff, status, acceptance criteria,
   tests, and `dragon/README.md`.

## Definition of done

A task is complete only when all applicable conditions are satisfied:

- The baseline was recorded, including any pre-existing test failures.
- Every acceptance criterion is covered by a test or an explicit verification
  step.
- Targeted validation passed, followed by the full existing suite when
  appropriate. Pre-existing failures are documented separately.
- `dragon/README.md` is updated when supported behavior changes.
- The final diff and `git status` contain only in-scope changes and no
  generated artifacts.
- Sprint work has a local commit using the `Sprint NN: ...` prefix.
- Changes are never pushed without an explicit user request.

## Failure handling

- Classify each failure as pre-existing, a regression, or missing coverage.
- Report the exact command, expected result, actual result, and relevant file or
  test name.
- Orchestrator may send one precise correction request to Developer. If the
  correction fails again, or the requirement is ambiguous, stop the loop and
  surface the issue to the user.

## Handoff report

Every agent uses this structure for handoffs and final reports:

```text
Summary:
Changed files:
Validation:
Requirements covered:
Risks or blockers:
Next action:
```

Use `None` when a field does not apply.

## Project-specific expectations

- Implement only the requested change and keep the solution focused.
- Extend the existing Dragon implementation rather than replacing unrelated
  behavior.
- If a structural change is necessary, update the repository structure
  documented below and the related documentation.

## Repository structure

```text
dragon/
├── __init__.py          - public package API
├── dragon.py            - core domain objects
├── dragon_tests.py      - unit tests
└── README.md            - current capabilities
```

## Related guidance

- [Reusable task brief](../prompts/my-prompt.prompt.md)
- [Orchestrator role](../agents/orchestrator.agent.md)
- [Developer role](../agents/developer.agent.md)
- [Tester role](../agents/tester.agent.md)
