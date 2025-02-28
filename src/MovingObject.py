class MovingObject:
    def __init__(self, speed):
        self.speed = speed
        
        """
        Player direction is determined by the binary list:
        0001 = 1 = up
        0010 = 2 = right
        0100 = 4 = down
        1000 = 8 = left
        """
        self.dir = 0

        self.current_cell = []
    
    def ChangeDirection(self, dir: int):
        self.dir = dir