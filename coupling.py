"""
This contains classes depending on each other.
The aim is exercise the coupling mesures of those classes.
The measures are:
    - Afferent Coupling (Ca)
    - Efferent Coupling (Ce)
    - Instability (I)
    - Abstractness (A)
    - Distance (D)
"""
from typing import Iterable


class Moteur:
    def __init__(self):
        pass


class Roue:
    def __init__(self):
        pass


class Voiture:
    def __init__(self, moteur: Moteur, roues: Iterable[Roue]):
        self.moteur = moteur
        self.roues = roues


class Routes:
    def __init__(self, voitures: Iterable[Voiture]):
        self.voitures = voitures
