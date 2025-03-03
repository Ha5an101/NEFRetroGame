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
        for cell_list in self.current_level.play_grid.cells:
            for cell in cell_list:
                cell.DrawSurface()
        
        return False

    def UpdateGame(self):
        keys = pg.key.get_pressed()
    
        def IsPlayerAlive():
            if self.lives == 0:
                self.EndGame()
                return False
            return True
        
        def CheckCollisionWithPlayer():
            if self.player.rect.collidelist([ghost.rect for ghost in self.ghosts]):
                self.lives -= 1
        CheckCollisionWithPlayer()

        def MoveObjects():
            inp = [(1 if keys[pg.K_UP] or keys[pg.K_w] else -1 if keys[pg.K_DOWN] or keys[pg.K_s] else 0), (1 if keys[pg.K_RIGHT] or keys[pg.K_d] else -1 if keys[pg.K_LEFT] or keys[pg.K_a] else 0)]
            self.player.ChangePosition(inp) # Input

            for ghost in self.ghosts:
                ghost.ChangePosition([ghost.target_col - ghost.current_col, ghost.target_row - ghost.current_row])
        MoveObjects()
        
        
        def DrawObjects():
            self.player.DrawSurface(self.screen_view)

            for ghost in self.ghosts:
                ghost.DrawSurface(self.screen_view)
        DrawObjects()

        return IsPlayerAlive()

    def RestartGame(self):
        self.lives = self.start_lives
        self.score = 0
        
        for cell_list in self.current_level.play_grid.cells:
            for cell in cell_list:
                cell.DrawSurface()

        return self.UpdateGame()

    def EndGame(self):
        # Do something
        return False

    def AccumilateScore(self, points: int):
        self.score += self.point.value


# Saved list of points
class PointValue(Enum):
    Empty = 0
    Basic = 10
    Energizer = 50
    Cherry = 100