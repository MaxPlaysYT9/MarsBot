from __future__ import annotations

from ursina import Ursina


def _create_app() -> Ursina:
    return Ursina(title="SpaceBot", size=(1024, 768))


def main() -> None:
    """Launch the SpaceBot application window and enter the main run loop."""
    app = _create_app()
    app.run()


if __name__ == "__main__":
    main()
