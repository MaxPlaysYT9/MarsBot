# ADR 002 — 3D GUI Library Selection

## Table of Contents

- [Context](#context)
- [Decision](#decision)
- [Consequences](#consequences)
- [Alternatives Considered](#alternatives-considered)
- [Diagrams](#diagrams)

---

## Context

SpaceBot is an AI-driven 3D Mars simulation. The initial scaffold used Tkinter, which provides no GPU-accelerated rendering and cannot support real-time 3D at any meaningful frame rate. A 3D-capable windowing and rendering library is required before any simulation work can begin.

Key constraints:
- The library must be Python-native (no separate build step for the render engine)
- It must support an entity/scene model suitable for placing terrain, rovers, and AI agents in 3D space
- Development velocity matters more than raw rendering performance at this stage — the simulation logic and AI layer are the primary value, not photorealism
- The entire application is launched from a single `python main.py` entry point

## Decision

**Use Ursina.**

Ursina is a Python 3D game/simulation engine built on top of Panda3D. It wraps Panda3D's `ShowBase` with a dramatically simpler API: one call creates the window, entities are placed with keyword arguments, and the run loop is managed automatically. This matches the project's need for rapid iteration on AI agent and simulation logic without fighting low-level rendering boilerplate.

Ursina's escape hatches (`.model`, `.texture`, `base` global) allow direct Panda3D access when fine-grained control is needed in later development phases.

**Installation**: `pip install ursina`

## Consequences

**Positive:**
- Minimal boilerplate — `App()` + `app.run()` is the entire window setup
- Entity-component model maps naturally to simulation objects (terrain, rover, agent)
- Full Panda3D power accessible through escape hatches when needed
- Large example library; active community

**Negative / Accepted risks:**
- Ursina's Panda3D dependency is ~300 MB — acceptable for a simulation project but notable for first install
- Ursina's UI primitives (Text, Button) are limited; complex HUDs may require Panda3D's DirectGUI or a second library in future
- Ursina abstracts some Panda3D internals; if rendering requirements grow beyond what Ursina exposes, migration to raw Panda3D is required

## Alternatives Considered

### Raw Panda3D

Full access to the Panda3D scene graph, shader pipeline, and physics system without any abstraction layer. Requires manual `ShowBase` setup, task-manager wiring, and node-graph management for every object.

**Ruled out at this stage** because the overhead slows AI/simulation iteration. Revisit if Ursina's abstractions become limiting.

### PyQt6 + PyOpenGL

Best choice for apps that need a rich desktop GUI (menus, toolbars, dockable panels) with an embedded 3D viewport. Uses Qt's `QOpenGLWidget` for the render surface.

**Ruled out** because SpaceBot is a full-screen simulation, not a GUI application with panels. The Qt + OpenGL integration adds significant complexity (shader management, projection matrices, VAO/VBO setup) for no user-facing benefit at this stage.

### Tkinter (existing scaffold)

CPU-rendered canvas. No GPU acceleration, no 3D primitives, no scene graph.

**Ruled out** — fundamentally incompatible with real-time 3D requirements.

## Diagrams

### Application architecture

```
python main.py
      │
      ▼
  main() ──────────────────────────────────────┐
      │                                         │
      ▼                                         ▼
_create_app()                            (future tasks:
      │                               terrain, AI agents,
      ▼                                 simulation loop)
 ursina.App(
   title="SpaceBot",
   size=(1024, 768)
 )
      │
      ▼
  app.run()  ◄─────────────────────────────────┐
      │                                         │
      │         Ursina / Panda3D run loop        │
      │  ┌──────────────────────────────────┐   │
      └─►│  update()  ──  render frame  ──  │───┘
         │  input()   ──  handle events     │
         └──────────────────────────────────┘
```

### Library layer stack

```
┌─────────────────────────────────┐
│         SpaceBot (main.py)      │  ← application code
├─────────────────────────────────┤
│             Ursina              │  ← entity-component API
├─────────────────────────────────┤
│             Panda3D             │  ← scene graph, physics
├─────────────────────────────────┤
│    OpenGL / DirectX / Vulkan    │  ← GPU driver (via Panda3D)
└─────────────────────────────────┘
```
