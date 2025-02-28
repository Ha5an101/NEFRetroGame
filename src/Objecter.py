import numpy as np

class GameObject:
    def __init__(self, pos: list[int], dirc: list[int]):
        self.position = pos
        self.direction = dirc
    
    def SetPosition(self, new_pos: list[int]):
        self.position = new_pos

    def SetDirection(self, new_dir: list[int]):
        self.direction = new_dir

    def ChangePosition(self, vector: list[int]):
        self.position = [(x + y) for x, y in zip(self.position, vector)]

class GridObject(GameObject):
    def __init__(self, pos: list[int], dirc: list[int], cols: int, rows: int):
        super.__init__(pos, dirc)
        if cols <= 0 or rows <= 0:
            raise ValueError("Cannot have negative number of columns or rows")

        self.cells = np.empty((cols, rows), dtype=CellObject)
        
        for c in range(cols):
            for r in range(rows):
                self.cells[c][r] = Cell(0, 0)


class CellObject(GameObject):
    def __init__(self, pos: list[int], dirc: list[int], walls: list[int]):
        super.__init__(pos, dirc)
        self.walls = walls
    
    def UpdateWalls(self, walls: list[int]):
        self.walls = walls