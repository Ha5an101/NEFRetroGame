import pygame as pg
import numpy as np

class SurfaceObject:
	def __init__(self, width: int, height: int):
		self.surface = pg.Surface((width, height))
		self.rect = self.surface.get_rect(topleft=(0, 0))

    def DrawSurface(self, screen):
		screen.blit(self.surface, self.rect)

    def SetSurface(self, surface: pg.Surface):
		self.surface = surface

    def TransformRect(self, **kwargs):
		self.rect = self.surface.get_rect(kwargs)

class ImageObject(SurfaceObject):
	def __init__ (self, path: str):
		self.surface = pg.image.load(path).convert_alpha()
		self.rect = self.copy_surface.get_rect(topleft=(0, 0))
		
	def SetSurface(self, surface: pg.image):
		self.surface = surface

class TextObject(SurfaceObject):
	def __init__ (self, path: str, size: int):
		self.surface = pg.font.Font(path, size)
		self.rect = self.copy_surface.get_rect(topleft=(0, 0))
		
	def SetSurface(self, surface: pg.font):
		self.surface = surface

class GameObject:
    def __init__(self, position: list[int], direction: list[int]):
        self.position = position
        self.direction = direction
    
    def SetPosition(self, new_pos: list[int]):
        self.position = new_pos

    def SetDirection(self, new_dir: list[int]):
        self.direction = new_dir

    def ChangePosition(self, vector: list[int]):
        self.position = [(x + y) for x, y in zip(self.position, vector)]

class GridObject(GameObject):
    def __init__(self, pos: list[int], dirc: list[int], cols: int, rows: int):
        super().__init__(pos, dirc)
        if cols <= 0 or rows <= 0:
            raise ValueError("Cannot have negative number of columns or rows")

        self.cells = np.empty((cols, rows), dtype=CellObject)
        
        for c in range(cols):
            for r in range(rows):
                self.cells[c][r] = CellObject(0, 0)

class CellObject(GameObject):
    def __init__(self, pos: list[int], dirc: list[int], walls: list[int]):
        super().__init__(pos, dirc)
        self.walls = walls
    
    def UpdateWalls(self, walls: list[int]):
        self.walls = walls

class GridBasedObject(GameObject):
    def __init__(self, pos: list[int], dirc: list[int], grid_base: GridObject):
        super().__init__(pos, dirc)
        self.base = grid_base
        self.current_cell = self.base.cells[0][0]
        self.SetPosition(self.current_cell.position)