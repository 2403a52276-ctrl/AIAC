from math import pi
from typing import Callable, Dict, Optional

# /c:/Users/welcome/Documents/Assignment 13.3 AI/task1.py
"""
Refactored area calculations with separate functions and dictionary dispatch.
"""



def rectangle_area(width: float, height: float) -> float:
    """Return area of a rectangle."""
    return width * height


def square_area(side: float, *_args) -> float:
    """Return area of a square. Extra args ignored for dispatch convenience."""
    return side * side


def circle_area(radius: float, *_args) -> float:
    """Return area of a circle."""
    return pi * radius * radius


# Dispatch table mapping shape name -> function
_AREA_FUNCTIONS: Dict[str, Callable[..., float]] = {
    "rectangle": rectangle_area,
    "square": square_area,
    "circle": circle_area,
}


def calculate_area(shape: str, x: float, y: Optional[float] = None) -> float:
    """
    Calculate area for the given shape using a dispatch table.

    - rectangle requires x (width) and y (height)
    - square uses x as side
    - circle uses x as radius

    Raises ValueError for unknown shapes or missing parameters.
    """
    shape_key = shape.lower()
    if shape_key not in _AREA_FUNCTIONS:
        raise ValueError(f"Unknown shape: {shape!r}")

    func = _AREA_FUNCTIONS[shape_key]

    if shape_key == "rectangle":
        if y is None:
            raise ValueError("Rectangle requires two dimensions: x (width) and y (height).")
        return func(x, y)

    # square and circle only need the first argument
    return func(x)


if __name__ == "__main__":
    # Simple demonstration
    examples = [
        ("rectangle", 3, 4),
        ("square", 5, None),
        ("circle", 2, None),
    ]

    for shape, x, y in examples:
        area = calculate_area(shape, x, y)
        print(f"{shape.capitalize()} area -> {area}")