from math import cos, sin


class trajectory:
    def __init__(self):
        pass

    @staticmethod
    def make_coordinates(self, x0: float, y0: float, alpha: float,
                         dist: float) -> [int, int]:
        x1 = x0 + dist * cos(alpha)
        y1 = y0 + dist * sin(alpha)
        return [x1, y1]
