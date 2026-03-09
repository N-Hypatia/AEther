# AEther - Visualiseur de l'Espace-Temps de Minkowski

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](requirements.txt)
[![Test Coverage](https://img.shields.io/badge/Coverage-60%25%20min-green)](pytest.ini)
[![Security: Bandit](https://img.shields.io/badge/Security-Bandit-red)](.pre-commit-config.yaml)

Un outil de visualisation interactive de l'espace-temps de Minkowski avec des représentations graphiques des cônes de lumière et des transformations de Lorentz.

## Fonctionnalités

- **Visualisation 3D** : Représentation graphique de l'espace-temps quadridimensionnel
- **Cônes de lumière** : Affichage des cônes passés et futurs
- **Transformations de Lorentz** : Simulation des effets relativistes
- **Événements spatio-temporels** : Création et visualisation d'événements dans l'espace-temps

## Structure du Projet

```
AEther/
├── Minkowski's Space-Time Visualizer/
│   └── Space-time Event.py          # Visualiseur d'événements de base
├── light-cone-plot/
│   └── src/
│       └── light_cone_plot.py       # Tracé des cônes de lumière 3D
├── 3d-light-cone-plot/
│   └── src/
│       └── light_cone_plot.py       # Alternative de visualisation 3D
└── src/                              # Module principal (à créer)
    └── lorentz.py                    # Transformations de Lorentz
```

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

### Visualisation de base

```python
from Minkowski's Space-Time Visualizer.Space_time_Event import generate_events
time, space_x, space_y = generate_events()
```

### Tracé du cône de lumière

```python
from light_cone_plot.src.light_cone_plot import plot_light_cone
plot_light_cone(t_max=10, num_points=100)
```

### Transformations de Lorentz

```python
from src.lorentz import LorentzTransformation
lt = LorentzTransformation(velocity=0.5)  # v/c = 0.5
transformed_event = lt.transform(t=1, x=0, y=0, z=0)
```

## Concepts Physiques

### Intervalle Espace-Temps

L'intervalle invariant entre deux événements est donné par :

$s^2 = c^2(t_2 - t_1)^2 - (x_2 - x_1)^2 - (y_2 - y_1)^2 - (z_2 - z_1)^2$

### Transformation de Lorentz

Les coordonnées transformées pour un observateur en mouvement à la vitesse v :

$t' = \gamma(t - \frac{vx}{c^2})$
$x' = \gamma(x - vt)$
$y' = y$
$z' = z$

où $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$

## Tests

Exécuter les tests avec coverage :

```bash
pytest --cov=src --cov-report=html
```

Le coverage minimum requis est de 60% selon les règles de développement.

## Sécurité

Scanner de sécurité (bandit) :

```bash
bandit -r src/
```

Vérification des dépendances (safety) :

```bash
safety check
```

## Règles de Développement

Ce projet suit les règles Kuro définies dans :
- [AI_GUIDELINES.md](AI_GUIDELINES.md) - Principes généraux
- [.cursorrules](.cursorrules) - Règles spécifiques à l'IDE
- [CODEBASE_GUIDE.md](CODEBASE_GUIDE.md) - Architecture du projet

## Licence

MIT License - Voir le fichier [LICENSE](LICENSE)
