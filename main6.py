class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Vector):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __str__(self):
        return  f"({self.x}, {self.y})"



print(Vector(1, 2) + Vector(1, 2))