# Prompt Guidelines

## Writing Effective Prompts

Keep prompts focused and concise:

1. **State the goal clearly** - What needs to be done?
2. **Define acceptance criteria** - How do we know it's done?
3. **Scope narrowly** - Limit to current sprint/requested change
4. **Mention constraints** - Standard library only, no extra features
5. **Ask for validation** - Prefer smallest valid verification step
6. **Avoid redundancy** - Reference guidelines, don't repeat them

## Real Example: Sprint 03

**Sprint 03 Prompt:**
```
Sprint 03: Add health points to Dragon

Requirements (from https://python3.info/dragon/polish/sprint-03.html):
- Dragon has random health points (50-100) on creation
- Use random.randint(a, b)
- Extend previous sprint code (name validation still required)

Acceptance Criteria:
- Dragon.health attribute exists and is between 50-100
- All existing tests still pass
- New tests verify health generation and randomness
- README.md updated with current features
- Commit with "Sprint 03:" prefix
```

**Result:** Sprint 03 completed - Dragon now has name (validated) + health (random 50-100)

## Prompt Structure for Next Sprint

When ready for Sprint 04:
1. Check Dragon current state in `/dragon/README.md`
2. Run tests to establish baseline
3. Review new sprint requirements
4. Write focused prompt with only new requirements
5. Ensure tests pass before concluding

## Reference
- General Guidelines: [copilot-instructions.md](./copilot-instructions.md)
- Dragon Details: [DRAGON.md](./DRAGON.md)

