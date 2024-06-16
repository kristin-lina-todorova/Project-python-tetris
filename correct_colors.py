#correct_colors.py
class Colors:
    """A class to define colors"""

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    thistle = (216, 191, 216)
    grid_color = (100, 149, 237)
    screen_background = (245, 245, 245)

    def get_color():
        """Return a list of predefined colors"""
        return [
            Colors.red,
            Colors.green,
            Colors.blue,
            Colors.thistle,
            Colors.grid_color,
            Colors.screen_background
        ]
