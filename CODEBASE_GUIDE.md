# AEther Codebase Guide

## Project Overview

AEther est un visualiseur de l'espace-temps de Minkowski avec des représentations graphiques des cônes de lumière et des transformations de Lorentz.

## Architecture (Hub & Spokes)

```
AEther/
├── Minkowski's Space-Time Visualizer/   # Spoke: Visualiseur d'événements
│   └── Space-time Event.py
├── light-cone-plot/                     # Spoke: Tracé des cônes de lumière 2D/3D
│   └── src/
│       └── light_cone_plot.py
├── 3d-light-cone-plot/                 # Spoke: Alternative visualisation 3D
│   └── src/
│       └── light_cone_plot.py
└── src/                                 # Hub: Transformations de Lorentz (core)
    └── lorentz.py
```

## Key Concepts

### Intervalle Espace-Temps
L'intervalle invariant entre deux événements :
```
s² = c²(t₂ - t₁)² - (x₂ - x₁)² - (y₂ - y₁)² - (z₂ - z₁)²
```

### Transformation de Lorentz
Coordonnées transformées pour un observateur en mouvement à la vitesse v :
```
t' = γ(t - vx/c²)
x' = γ(x - vt)
y' = y
z' = z
```
où γ = 1 / sqrt(1 - v²/c²)

## Entry Points

### Pour les cônes de lumière
```python
from light_cone_plot.src.light_cone_plot import plot_light_cone
plot_light_cone(t_max=10, num_points=100)
```

### Pour les transformations de Lorentz
```python
from src.lorentz import LorentzTransformation
lt = LorentzTransformation(velocity=0.5)  # v/c = 0.5
transformed_event = lt.transform(t=1, x=0, y=0, z=0)
```

## Technology Stack

| Category | Tool |
|----------|------|
| Language | Python 3.10+ |
| Visualization | Matplotlib, NumPy |
| Testing | pytest, pytest-cov |
| Security | bandit, safety |

## Development Rules

Voir AI_GUIDELINES.md et .cursorrules pour les règles de développement.