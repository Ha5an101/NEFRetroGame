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

    def GetRect(self, **kwargs):
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
        self.direction = direction # The first item is horizontal axis and the second item is vertical
    
    def SetPosition(self, new_pos: list[int]):
        self.position = new_pos

    def SetDirection(self, new_dir: list[int]):
        self.direction = new_dir

    def ChangePosition(self, vector: list[int]):
        self.position = [(x + y) for x, y in zip(self.position, vector)]

class GridObject(GameObject):
    def __init__(self, position: list[int], direction: list[int], cols: int, rows: int):
        super().__init__(self, position, direction)
        if cols <= 0 or rows <= 0:
            raise ValueError("Cannot have negative number of columns or rows")

        self.cells = np.empty((cols, rows), dtype=CellObject)
        
        for c in range(cols):
            for r in range(rows):
                self.cells[c][r] = CellObject(0, 0)

class CellObject(GameObject):
    def __init__(self, position: list[int], direction: list[int], walls: list[int]):
        super().__init__(self, position, direction)
        self.walls = walls
    
    def UpdateWalls(self, walls: list[int]):
        self.walls = walls

    def DoDirectionsAlign(self, game_object: GameObject, direction_index: int):
        if game_object.direction[direction_index] == self.walls[direction_index]
            return True
        return False

class GridBasedObject(GameObject):
    def __init__(self, position: list[int], direction: list[int], grid_base: GridObject):
        super().__init__(self, position, direction)
        self.base = grid_base
        self.current_row = 0
        self.current_col = 0
        self.SetPosition(self.base.cells[current_col][current_row].position)

    def CanMoveOnward(self):
        if self.direction[0] == 0 and self.direction[1] == 0:
            return False

        if sorted(self.direction) == [-1, 1]:
            return False

        # Find the leading direction to head to with the directional priority being up, right, down and left
        up_priority = lst == [0, 1]  # up
        right_priority = lst == [1, 0]  # right
        down_priority = lst == [0, -1]  # down
        left_priority = lst == [-1, 0]  # left
        lead_direction = [0, 1] if up_priority else [1, 0] if right_priority else [0, -1] if down_priority else [-1, 0]
        lead_direction_index = 1 if lead_direction[0] == 0 else 0
        # Check if the object is not runnin into the cells wall
        if self.base.cells[current_col][current_row].DoDirectionsAlign(lead_direction_index):
            return False

        return True

    def SetPosition(self, position: list[int])
        self.current_row += position[0]
        self.current_col += position[1]

        super().SetPosition(self.base.cells[current_col][current_row].position)

    def ChangePosition(self, vector: list[int]):
        super().ChangePosition(self, vector)

        self.current_row += self.direction[0] * vector[0]
        self.current_col += self.direction[1] * vector[1]
