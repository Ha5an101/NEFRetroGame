import numpy as np
from PointManager import PointValue

class Grid:
    def __init__(self, cols: int, rows: int):
        if cols <= 0 or rows <= 0:
            raise ValueError("Cannot have negative number of columns or rows")

        self.grid_cols, self.gird_rows = np.meshgrid(np.arrange(0, cols), np.arrange(0, rows), indexing='xy')
        
        self.cells = np.empty((cols, rows), dtype=Cell)
        
        for c in range(cols):
            for r in range(rows):
                self.cells[c][r] = Cell(0, 0)
    
    def UpdateCellPoints(self, col: int, row: int, points: PointValue):
        self.cells[col][row].point = points
    
    def UpdateCellWall(self, col: int, row: int, walls: int):
        self.cells[col][row].walls = walls


class Cell:
    """
    Walls Logic:
    0001 = 1 = up
    0100 = 4 = down
    0010 = 2 = right
    1000 = 8 = left
    """
    def __init__(self, walls: int, points: PointValue):
        self.walls = walls
        self.point = points