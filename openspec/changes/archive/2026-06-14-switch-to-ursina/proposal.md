## Why

The current Tkinter scaffold has no GPU-accelerated 3D capability, which is incompatible with the project's goal of an AI-driven 3D Mars simulation. Ursina provides a Python-native 3D engine with a simple API that allows rapid iteration on simulation and AI agent logic without fighting low-level rendering concerns.

## What Changes

- Replace `tkinter` dependency with `ursina` in the project
- Rewrite `main.py` to launch an Ursina `App` window instead of a `tk.Tk()` window
- Add ADR `docs/adr/002-3d-gui-library.md` documenting the library decision

## Capabilities

### New Capabilities

- `ursina-app-scaffold`: A minimal Ursina App entry point with title, window size, and run loop — the foundation all future 3D simulation features will build on

### Modified Capabilities

<!-- No existing spec-level requirements are changing — this replaces the scaffold before any simulation behaviour was specified -->

## Impact

- **`main.py`**: Complete rewrite; Tkinter removed, Ursina App introduced
- **`docs/adr/`**: New file `002-3d-gui-library.md`
- **Dependencies**: `tkinter` (stdlib, removed from usage) → `ursina` (must be installed via `pip install ursina`)
- No external APIs or data contracts affected
