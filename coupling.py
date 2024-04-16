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
from abc import ABC, abstractmethod
from typing import Iterable


class Tourne(ABC):
    @abstractmethod
    def en_avant(self):
        ...

    @abstractmethod
    def en_arrière(self):
        ...


class Moteur(Tourne):
    def __init__(self):
        pass


class Roue(Tourne):
    def __init__(self):
        pass


class Voiture:
    def __init__(self, moteur: Moteur, roues: Iterable[Roue]):
        self.moteur = moteur
        self.roues = roues


class Routes:
    def __init__(self, voitures: Iterable[Voiture]):
        self.voitures = voitures
