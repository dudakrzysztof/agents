# Prompt Guidelines

## Writing Effective Prompts

Keep prompts focused and concise:

1. **State the goal clearly** - What needs to be done?
2. **Define acceptance criteria** - How do we know it's done?
3. **Scope narrowly** - Limit to current sprint/requested change
4. **Mention constraints** - Standard library only, no extra features
5. **Ask for validation** - Prefer smallest valid verification step
6. **Avoid redundancy** - Reference guidelines, don't repeat them

## Prompt Structure Example

```
Sprint 03: Add health points to Dragon

Requirements:
- Random health 50-100 on creation
- Use random.randint()
- Extend previous sprint code

Validation:
- All existing tests pass
- New tests cover health generation
- Health varies between dragons
```

See [GENERAL.md](../instructions/GENERAL.md) and [DRAGON.md](../instructions/DRAGON.md) for implementation guidelines.
