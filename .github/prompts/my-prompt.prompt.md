# Task Brief Template

Use this template to prepare the brief handed from Orchestrator to Developer.
The linked instruction files are the source of shared rules; reference them
instead of copying their contents into every brief.

```text
[Task name]

Goal:
- What outcome should the user get?

Scope:
- What is included?
- What is explicitly out of scope?

Non-goals:
- What must not be changed or added?

Requirements:
- Task-specific behavior and acceptance criteria.

Assumptions:
- Decisions made because the request or requirements are ambiguous.

Affected files:
- Existing files or areas expected to change.

Validation:
- Existing commands or checks that prove the requirements.
- Relevant edge cases.

Risks:
- Known compatibility, migration, or implementation risks.

References:
- Selected sprint file and relevant implementation or documentation.
```

## Authoring rules

- State the requested behavior precisely and keep the brief concise.
- Include only task-specific constraints; do not repeat repository or project
  instructions.
- Fill every section; write `None` when a section does not apply.
- Treat inherited sprint behavior as existing scope unless the sprint changes it.
- Reference existing implementation and documentation instead of proposing a
  rewrite.
- Make every acceptance criterion verifiable by a test or an explicit check.

## Instruction references

- [Repository standards](../copilot-instructions.md)
- [Dragon workflow](../instructions/dragon.instructions.md)
- [Orchestrator role](../agents/orchestrator.agent.md)
