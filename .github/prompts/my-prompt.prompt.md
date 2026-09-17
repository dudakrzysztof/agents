# Writing Prompts

## Principles

Keep prompts focused, clear, and actionable:

1. **State the goal** - What needs to be done?
2. **Define success criteria** - How do we verify it's complete?
3. **Scope clearly** - What is included/excluded?
4. **Set constraints** - Implementation limits (standard library, no extra features)
5. **Request validation** - How should the solution be tested?
6. **Avoid redundancy** - Reference guidelines instead of repeating them

## Prompt Template

```
[Task Name]

Description:
- Clear statement of what needs to be implemented

Requirements:
- Specific feature/change requested
- Any acceptance criteria
- Scope boundaries

Constraints:
- Implementation limits (e.g., standard library only)
- Code style preferences if needed

Validation:
- How to test/verify the solution
- Which tests should pass
- Any edge cases to consider

Reference:
- Link to relevant documentation/guidelines
- Previous work/commits if applicable
```

## Best Practices

- **Be specific**: "Add health attribute to Dragon" not "improve Dragon"
- **Reference existing work**: Extend previous features, don't rewrite
- **Mention constraints early**: Standard library, no external dependencies
- **Ask for tests**: Behavior verification is essential
- **Keep it brief**: Detail matters, verbosity doesn't

## Reference

- Implementation guidelines: [copilot-instructions.md](../copilot-instructions.md)
- Project-specific details: [DRAGON.md](../instructions/dragon.instructions.md)


