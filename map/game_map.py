import numpy as np
from tcod.console import Console
import map.tile_types as tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

    def in_bounds(self, x: int, y: int):
        """
        Return True if x and y are inside of the bounds of this map.
        """
        return 0 <= self.width and 0 <= y < self.height

    def render(self, console: Console):
        console.tiles_rgb[0 : self.width, 0 : self.height] = self.tiles["dark"]
