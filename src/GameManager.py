import pygame as pg
from LevelManager import Level
from PointManager import PointValue

"""
Game Rules:
"""

class Game:
    def __init__(self):
        self.current_level = Level("", None)
    pass