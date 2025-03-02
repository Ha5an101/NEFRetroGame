import pygame as pg
from enum import Enum
from LevelManager import Level
from Player import PacMan
from Ghosts import Blinky, Pinky, Inky, Clyde

class Game:
    score = 0
    start_lives = 3
    lives = start_lives

    def __init__(self, screen):
        self.current_level = Level("", None)
        self.player = PacMan()
        self.ghosts = [Blinky(), Pinky(), Inky(), Clyde()]
        self.screen_view = screen
    
    def StartGame(self):
        # Do something
        self.UpdateGame()
        return False

    def UpdateGame(self):
        if self.lives == 0:
            self.EndGame()
            return False
        
        def CheckCollisionWithPlayer():
            if self.player.rect.collidelist([ghost.rect for ghost in self.ghosts]):
                # Decrease Lives
                pass

        def MoveObjects():
            self.player.ChangePosition() # Input

            for ghost in self.ghosts:
                ghost.ChangePosition([ghost.target_col, ghost.target_row])3

        self.player.DrawSurface(self.screen_view)

        for ghost in self.ghosts:
            ghost.DrawSurface(self.screen_view)

        return True

    def RestartGame(self):
        self.lives = self.start_lives
        self.score = 0

        self.UpdateGame()
        return False

    def EndGame(self):
        # Do something
        return False

    def AccumilateScore(points: int):
        self.score += point.value


# Saved list of points
class PointValue(Enum):
    Empty = 0
    Basic = 10
    Energizer = 50
    Cherry = 100