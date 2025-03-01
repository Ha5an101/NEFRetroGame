from IObject import GridObject

class Level:
    def __init__(self, name: str, presetGrid: GridObject):
        self.name = name

        if presetGrid is None:
            self.grid = GridObject(28, 36)
        else:
            self.grid = presetGrid
