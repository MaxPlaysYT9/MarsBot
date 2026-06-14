## 1. ADR Documentation

- [x] 1.1 Create `docs/adr/` directory if it does not exist
- [x] 1.2 Write `docs/adr/002-3d-gui-library.md` with ToC, Context, Decision, Consequences, Alternatives Considered, and ASCII architecture diagram showing the Ursina app structure

## 2. Ursina Scaffold

- [x] 2.1 Write experiment file `experiment_ursina_window.py` verifying that `ursina.App` opens a titled 1024×768 window and `app.run()` enters the run loop without errors
- [x] 2.2 Rewrite `main.py`: remove `tkinter`, add `from __future__ import annotations`, implement `_create_app() -> App` helper and `main() -> None` with docstring and type hints
- [x] 2.3 Delete `experiment_ursina_window.py` after confirming the approach works
- [x] 2.4 Manually run `python main.py` and confirm a 1024×768 window titled "SpaceBot" opens and closes cleanly
