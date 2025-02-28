from enum import Enum

# Saved list of points
class PointValue(Enum):
    Empty = 0
    Basic = 10
    Energizer = 50
    Cherry = 100


CurrentPoints = 0

def accumilatePoint(point: PointValue):
    CurrentPoints += point.value

def accumilateValue(value: int):
    CurrentPoints += value
