from IObject import GridBasedObject, SurfaceObject

"""
Ghost(s) Rules:
Known as Blinky (red), Pinky (pink), Inky (blue) and Clyde (orange).
The ghosts have three modes they can operate in - chase mode where they find and capture Pac-Man, scatter mode, where they head for their respective corners, and frightened mode where they run away from Pac-Man after he eats one of the four energizers.
The ghosts are prohibited from reversing their direction of travel. They can only travel the direction they are facing to take the next intersection. The ghosts only change direction when the mode changes from chase-to-scatter, chase-to-frightened, scatter-to-chase, and scatter-to-frightened.
Ghosts do not wander around aimlessly. A ghost is always trying to reach a specific tile somewhere on or off the screen. Each ghost calculates its target tile in a different manner. In chase mode, the target tile is usually related to Pac-Man’s current tile. In scatter mode, the target tile is a fixed tile located in the character’s home corner. Thus the only difference between chase mode and scatter mode is where the ghost’s target tile is located.
"""

class Ghost(GridBasedObject, SurfaceObject):
    def __init__(self, position: list[int], direction: list[int], grid_base: GridObject):
        GridBasedObject.__init__(self, position, direction)

    def TargetCell(self, player: GridBasedObject):
        pass


# Blinky’s target tile is always Pac-Man’s current tile.
class Blinky(Ghost):
    def TargetCell(self, player: GridBasedObject):
        pass

#Pinky’s does not target Pac-Man’s current tile directly. Instead, his target tile in chase mode is a tile offset four tiles away from Pac-Man in the direction Pac-Man is currently moving. If the target tile calculated by Pinky falls behind Pac-Man, Pinky will turn right before he reaches Pac-Man in an attempt to get behind him.
class Pinky(Ghost):
    def TargetCell(self, player: GridBasedObject):
        pass

# Inky’s target tile is calculated by taking the tile two spaces ahead of Pac-Man and doubling the distance Blinky is away from that point.
class Inky(Ghost):
    def TargetCell(self, player: GridBasedObject):
        pass

# Clyde’s tile-targeting scheme: If Pac-Man is more than 8 tiles away, Clyde’s target tile will be Pac-Man’s current tile. If Clyde is closer than 8 tiles to Pac-Man, he will switch to scatter-mode targeting and head for his own corner of the board until he is far enough away to target Pac-Man again.
class Clyde(Ghost):
     def TargetCell(self, player: GridBasedObject):
        pass