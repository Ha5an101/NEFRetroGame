import pygame as pg
from enum import Enum
from LevelManager import Level
import Player
import Ghosts

"""
Game Rules:
"""

class Game:
    current_points = 0

    def __init__(self):
        self.current_level = Level("", None)
    
    def StartGame(self):
        pass

    def UpdateGame(self):
        pass

    def RestartGame(self):
        pass

    def EndGame(self):
        pass

    def AccumilatePoints(points: int):
        self.current_points += point.value


# Saved list of points
class PointValue(Enum):
    Empty = 0
    Basic = 10
    Energizer = 50
    Cherry = 100