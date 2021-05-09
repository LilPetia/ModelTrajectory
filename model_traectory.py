from math import cos, sin, pi


class trajectory:
    def __init__(self):
        pass

    # start direction(alpha = 0) is direction is vector from center to enemy`s
    # goal. x0, y0 is coordinates from field`s center
    @staticmethod
    def make_coordinates1(x0: float, y0: float, alpha: float,
                          dist: float) -> [int, int]:
        x1 = x0 + dist * cos(alpha)
        y1 = y0 + dist * sin(alpha)
        return [x1, y1]

    @staticmethod
    def make_coordinates2(x0: float, y0: float, alpha: float,
                          dist: float, coefficients: [float, float, float,
                                                      float]) -> [int, int]:
        # List of coefficients for all directions. First direction is vector
        # from center to enemу`s goal, the following follow  clockwise
        if alpha < pi / 2 and alpha > pi / 2:
            x1 = x0 + coefficients[0] * dist * cos(alpha)
            pass
        else:
            x1 = x0 + coefficients[2] * dist * cos(alpha)
            pass
        if (alpha > 0 and alpha < pi):
            y1 = y0 + coefficients[1] * dist * sin(alpha)
        else:
            y1 = y0 + coefficients[3] * dist * sin(alpha)
        return [x1, y1]
