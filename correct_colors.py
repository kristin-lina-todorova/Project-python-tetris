# colors.py
class Colors:
    """A class to define colors"""

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    thistle = (216, 191, 216)
    grid_color = (100, 149, 237)
    screen_background = (245, 245, 245)

    @staticmethod
    def get_color():
        """Return a list of predefined colors"""
        return [
            Colors.black,
            Colors.white,
            Colors.red,
            Colors.green,
            Colors.blue,
            Colors.thistle,
            Colors.grid_color,
            Colors.screen_background
        ]
