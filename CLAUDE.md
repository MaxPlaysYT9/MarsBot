# SpaceBot — Claude Code Guidelines

## Code style

- **[STYLE-1] Keep methods short and focused.** Each method does one thing. Extract helpers rather than letting a method grow. Avoid duplicating logic — if the same pattern appears twice, pull it out.
- **[STYLE-2] Mark internal methods private or protected.** Prefix with `_` for protected, `__` for private. Public API surface should be intentional and minimal.
- **[STYLE-3] Always use type hints.** Every function and method must annotate its parameters and return type. Use `from __future__ import annotations` at the top of each file for forward-reference support.
- **[STYLE-4] Use dataclasses instead of plain dicts.** Structured data must be represented as `@dataclass` (or `@dataclass(frozen=True)` for immutable value objects). Never pass naked `dict` across function boundaries where a typed structure is appropriate.
- **[STYLE-5] Document all public methods.** Every public method and function must have a docstring describing what it does, its parameters, and its return value. Internal (`_`/`__`) methods do not require docstrings.

## Workflow

- **[WORKFLOW-1] Plan non-trivial changes with OpenSpec before writing code.** Any change that touches more than one file, introduces a new abstraction, or modifies existing behaviour must have an OpenSpec plan agreed upon first. Do not write implementation code until the plan is approved.
- **[WORKFLOW-2] Experiment before applying.** Before writing code into the actual source files, create a throwaway `experiment_<topic>.py` file and verify the approach works. If the experiment succeeds, apply the logic to the real codebase and delete the experiment file. If it fails, iterate on the experiment until it works.
- **[WORKFLOW-3] Run experiment files with `uv`.** Every `experiment_<topic>.py` file must be executed via `uv run experiment_<topic>.py`, never with `python` directly.
- **[WORKFLOW-4] Add dependencies with `uv`, never `pip`.** All package installations must use `uv add <package>`. Never use `pip install`.

## Architecture Decision Records (ADRs)

- **[ADR-1] Record every decision under `docs/adr/`.** Every architectural, design, or process decision must be captured as an ADR file inside `docs/adr/`. No decision is final until its ADR exists.
- **[ADR-2] Name ADRs as `NNN-<slug>.md`.** Use a zero-padded three-digit sequence number followed by a short kebab-case slug (e.g., `001-gui-decision.md`, `002-storage-backend.md`). Numbers are assigned in order and never reused.
- **[ADR-3] Include a Table of Contents.** Each ADR must begin with a ToC linking to its sections (e.g., Context, Decision, Consequences, Alternatives, Diagrams). The ToC must stay in sync with the actual section headings.
- **[ADR-4] Include ASCII diagrams for important flows.** Each ADR must contain ASCII-based diagrams illustrating the most important flows, components, or interactions involved in the decision. Diagrams live inline in the ADR (no external image files).
