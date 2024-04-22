"""CQ08 - Introduction To Object Oriented Programming."""

from __future__ import annotations


__author__ = "730662932"


class Point:
    """Creating a Point Class."""
    def __init__(self, x_init: float, y_init: float):
        """Defining a Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutating Method Point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method Point Scale Being Mutated."""
        scaled_x = self.x * factor
        scaled_y = self.y * factor
        return Point(scaled_x, scaled_y)