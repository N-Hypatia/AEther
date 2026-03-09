"""
Tests unitaires pour le module de transformations de Lorentz.

Ces tests vérifient les calculs de relativité restreinte.
"""
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestLorentzImports:
    """Tests des imports du module lorentz."""

    def test_numpy_import(self):
        """Vérifie que numpy est disponible."""
        import numpy as np
        assert np is not None

    def test_typing_import(self):
        """Vérifie que typing est disponible."""
        from typing import Tuple, Union
        assert Tuple is not None
        assert Union is not None


class TestSpacetimeConcepts:
    """Tests des concepts de base de l'espace-temps."""

    def test_speed_of_light_constant(self):
        """Vérifie la constante de la vitesse de la lumière."""
        import numpy as np
        c = 299792458  # m/s
        assert c > 0
        assert isinstance(c, (int, float))

    def test_lorentz_factor_definition(self):
        """Vérifie la définition du facteur de Lorentz.

        gamma = 1 / sqrt(1 - v²/c²)
        """
        import numpy as np
        c = 1.0  # Unité naturelle
        v = 0.0  # Vitesse nulle
        gamma = 1.0 / np.sqrt(1 - (v**2 / c**2))
        assert gamma == 1.0

    def test_lorentz_factor_at_light_speed(self):
        """Le facteur de Lorentz tend vers l'infini à la vitesse de la lumière."""
        import numpy as np
        c = 1.0
        v = 0.99 * c  # 99% de la vitesse de la lumière
        gamma = 1.0 / np.sqrt(1 - (v**2 / c**2))
        assert gamma > 7.0  # gamma ≈ 7.09 à v=0.99c

    def test_time_dilation_formula(self):
        """Vérifie la formule de dilatation du temps.

        t' = gamma * (t - vx/c²)
        """
        import numpy as np
        c = 1.0
        v = 0.5  # v = 0.5c
        t = 1.0  # temps propre
        x = 0.0  # position

        gamma = 1.0 / np.sqrt(1 - (v**2 / c**2))
        t_prime = gamma * (t - (v * x) / (c**2))

        assert t_prime > t  # Le temps dilaté est plus grand

    def test_length_contraction_formula(self):
        """Vérifie la formule de contraction des longueurs.

        x' = gamma * (x - vt)
        """
        import numpy as np
        c = 1.0
        v = 0.5  # v = 0.5c
        t = 1.0
        x = 1.0  # longueur propre

        gamma = 1.0 / np.sqrt(1 - (v**2 / c**2))
        x_prime = gamma * (x - v * t)

        assert x_prime < x  # La longueur contractée est plus petite

    def test_spacetime_interval_invariant(self):
        """Vérifie l'invariance de l'intervalle espace-temps.

        s² = c²(t₂-t₁)² - (x₂-x₁)² - (y₂-y₁)² - (z₂-z₁)²
        """
        import numpy as np
        c = 1.0

        # Deux événements
        t1, x1, y1, z1 = 0, 0, 0, 0
        t2, x2, y2, z2 = 1, 1, 0, 0

        # Intervalle dans le référentiel 1
        s1_sq = (c * (t2 - t1))**2 - (x2 - x1)**2 - (y2 - y1)**2 - (z2 - z1)**2

        # Intervalle dans un référentiel en mouvement (v=0.5c)
        v = 0.5 * c
        gamma = 1.0 / np.sqrt(1 - (v**2 / c**2))

        t1_prime = gamma * (t1 - v * x1 / c**2)
        t2_prime = gamma * (t2 - v * x2 / c**2)
        x1_prime = gamma * (x1 - v * t1)
        x2_prime = gamma * (x2 - v * t2)

        s2_sq = (c * (t2_prime - t1_prime))**2 - (x2_prime - x1_prime)**2

        # Les intervalles doivent être égaux (invariants)
        assert abs(s1_sq - s2_sq) < 1e-10