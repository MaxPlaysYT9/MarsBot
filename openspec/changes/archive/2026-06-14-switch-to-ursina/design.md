## Context

SpaceBot currently has a minimal Tkinter scaffold (`main.py`) with no 3D capability. The project goal is an AI-driven 3D Mars simulation. Tkinter's canvas is CPU-rendered and cannot support real-time 3D. Ursina is a Python-first 3D engine built on top of Panda3D that provides GPU-accelerated rendering while keeping the API surface small enough to maintain rapid iteration.

An ADR (`docs/adr/002-3d-gui-library.md`) must be written alongside the code change to satisfy the project's ADR-1 through ADR-4 requirements.

## Goals / Non-Goals

**Goals:**
- Replace the Tkinter window with an Ursina `App` entry point
- Keep `main.py` as the single entry point; it must remain runnable with `python main.py`
- Produce ADR `002-3d-gui-library.md` with ToC, context, decision, alternatives, consequences, and ASCII architecture diagram
- All code in `main.py` must comply with CLAUDE.md: type hints, docstrings on public functions, short focused methods

**Non-Goals:**
- Implementing any Mars terrain, AI agents, or simulation logic (future changes)
- Adding configuration files or dependency managers (e.g., `pyproject.toml`, `requirements.txt` changes are out of scope for this change — Ursina install is a manual `pip install ursina` step)
- Changing any file other than `main.py` and adding `docs/adr/002-3d-gui-library.md`

## Decisions

### Decision 1: Ursina over Panda3D directly

**Choice**: Use Ursina rather than raw Panda3D.

**Rationale**: Ursina wraps Panda3D with a dramatically simpler API (entity-component model, one-liner window creation) at the cost of some low-level control. For a project at scaffold stage where AI agent iteration speed matters most, Ursina wins. Panda3D can be reached through Ursina's `.model`, `.texture`, and `base` escape hatches if fine-grained control is needed later.

**Alternatives considered**:
- **Raw Panda3D**: Full control, steeper API, requires manual ShowBase setup — revisit if rendering requirements exceed what Ursina exposes
- **PyQt6 + PyOpenGL**: Best for hybrid GUI/3D apps (menus, panels, 3D viewport); overkill for a simulation-first app with no form-heavy UI
- **Tkinter**: Retained as stdlib fallback, but cannot render GPU-accelerated 3D — ruled out

### Decision 2: `main.py` stays the sole entry point

**Choice**: No launcher scripts or secondary entry points.

**Rationale**: The project is at scaffold stage. Introducing a `run.py` or `__main__.py` adds indirection with no benefit. Ursina's `App` + `app.run()` pattern fits naturally in a `main()` function.

### Decision 3: ADR written before implementation

**Choice**: ADR file written as part of this change, not after.

**Rationale**: CLAUDE.md ADR-1 requires every decision to be captured. Writing it first forces clarity on the rationale before the code is locked in.

## Risks / Trade-offs

- **Ursina version API drift** → Pin the version in a `requirements.txt` (or document the tested version in the ADR) to avoid breakage on `pip install ursina` upgrades
- **Ursina's Panda3D dependency is heavyweight (~300 MB)** → Acceptable for a simulation project; document in ADR as a known consequence
- **Limited widget toolkit** → Ursina has basic UI primitives (Text, Button); complex HUD work may require dropping to Panda3D's DirectGUI or adding a second library. Not a concern at scaffold stage.

## Migration Plan

1. Write `docs/adr/002-3d-gui-library.md`
2. Rewrite `main.py`: remove `tkinter`, add `ursina` App scaffold
3. Verify `python main.py` opens a 1024×768 window titled "SpaceBot" without errors
4. No rollback complexity — change is confined to one file; reverting is a single `git revert`

## Open Questions

- None blocking this change. Terrain rendering approach will be decided in a future ADR.
