from enum import Enum

class Face(Enum):
    R = 0  # Right
    L = 1  # Left
    U = 2  # Up
    D = 3  # Down
    F = 4  # Front
    B = 5  # Back

    def __str__(self):
        if self.value == 0:
            return "R"
        if self.value == 1:
            return "L"
        if self.value == 2:
            return "U"
        if self.value == 3:
            return "D"
        if self.value == 4:
            return "F"
        if self.value == 5:
            return "B"


class Rotation(Enum):

    c = 0  # Clockwise
    a = 1  # Anti-Clockwise

    def __str__(self):
        if self.value == 0:
            return "c"
        if self.value == 1:
            return "a"