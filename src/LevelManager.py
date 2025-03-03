from IObject import GridObject

class Level:
    def __init__(self, name: str, grid: GridObject):
        self.name = name

        if grid is None:
            self.original_grid = GridObject(28, 36)
        else:
            self.original_grid = grid
        self.RestartLevel()

    def CompleteLevel(self):
        del self

    def RestartLevel(self):
        self.play_grid = self.original_grid