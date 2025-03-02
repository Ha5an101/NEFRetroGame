from IObject import GridBasedObject, SurfaceObject

"""
Player Rules:
The player can move though the maze and accumilate points be eating dots and energizers
The player is chades by ghosts that once in contact stop the player and takes a life
When a life is taken, if there are more lives remaining the player is transported to the cage to continue else the gam is over
When eating an energizer all ghosts will run a way from you and you can eat them
The player can stop moving by coliding with awil in the direction of motion
The player cannot change directions if thre is a wall but the change will be applied whan there is an available wall
There are horizontal holes in the maze that allow the player to teleport between the sides of the maze
"""

class PacMan(GridBasedObject, SurfaceObject):
    def __init__(self, position: list[int], direction: list[int], grid: GridObject, surface: SurfaceObject):
        GridBasedObject.__init__(self, position, direction)
        self.target_row: int
        self.target_col: int
        
        SurfaceObject.__init__(self, surface.get_width(), surface.get_height())
        self.Rect(center=(0,0))