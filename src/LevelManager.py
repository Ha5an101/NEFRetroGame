from GridManager import Grid

class Level:
    def __init__(self, name: str, presetGrid: Grid):
        self.name = name

        if presetGrid is None:
            self.grid = Grid(28, 36)
        else:
            self.grid = presetGrid
