# Contributing

Thank you for your interest in improving this project.

## Before Making Changes

1. Fork or clone the repository.
2. Create a new branch for your change.
3. Create a Python virtual environment.
4. Install the dependencies from `requirements.txt`.
5. Run the notebooks in order when your change affects the ML workflow.

## Project Guidelines

Please keep the repository simple and notebook-focused.

- Do not add a `src/` directory.
- Do not create separate preprocessing or data-loader modules.
- Keep experiments reproducible.
- Prefer lightweight CPU-friendly solutions.
- Keep notebook code readable and explain important steps.
- Avoid committing generated model files or MLflow runs unless specifically required.
- Keep Flask changes small and understandable.

## Pull Requests

A useful pull request should include:

- A clear description of the change
- The reason for the change
- Any notebook or application behavior affected
- Updated documentation when necessary

Please test the relevant notebook or Flask functionality before submitting a pull request.
