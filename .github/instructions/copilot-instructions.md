# GitHub Copilot Instructions

This file contains customization instructions for GitHub Copilot within this repository.

## Repository Context

This is a Python AI project.
Task instructions follow the Dragon "About" brief: treat the scenario as an MVP business requirements exercise, not game development, and avoid adding unrequested features or using non-standard-library modules.

## Guidelines for Code Assistance

### General Principles
- Provide clear, well-documented code
- Follow Python best practices and PEP 8 guidelines
- Use modern Python (3.14 or later).
- Include type hints where applicable
- Write meaningful variable and function names
- solution must be in English.
- solution must meet the acceptance criteria.
- Do not use modules from outside the standard library.
 - Respect the brief: you are the programmer, the PO does not advise on architecture, and future changes may require flexibility.

### Project Structure
The repository contains:
- dragon directory, all files in this directory are related to the dragon project
- directory dragon contains the following files:
  - dragon.py: main implementation of the dragon project
  - dragon_utils.py: utility functions for the dragon project
  - dragon_tests.py: test cases for the dragon project
  - README.md: documentation for the dragon project
  - more if needed

### Dragon Brief
- Do not read ahead into later parts of the task.
- Keep the solution focused on the stated requirements and acceptance criteria.
- Prefer TDD, KISS, DRY, SOLID, and avoid over-engineering.

### Code Style
- Use consistent indentation (4 spaces for Python)
- Add docstrings to functions and classes
- Include comments for complex logic
- Keep functions focused and modular

### Testing
- Write tests alongside implementations
- Use descriptive test case names
- Include edge case testing