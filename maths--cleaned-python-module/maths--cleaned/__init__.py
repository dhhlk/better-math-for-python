"""
maths--cleaned-python-module
Pure Decimal-based math utilities.
No math module. Clean. Educational. Precise.
"""

from .core import (
    # Constants
    PI, E,

    # Basic number functions
    fact,
    fibonacci,
    digital_root,
    is_harshad,
    triangular,
    collatz_steps,

    # Roots & powers
    sqrt,
    cbrt,
    power,

    # Logarithms
    ln,
    log,

    # Trigonometry
    sin,
    cos,
    tan,

    # Geometry
    circumference,
    area_circle,
    area_square,
    area_rectangle,
    area_triangle,
    perimeter_square,
    perimeter_rectangle,
    distance_2d,
    cube_volume,
    cube_surface_area,
    pythagoras,

    # Finance
    percentage,
    simple_interest,
    compound_interest,

    # Statistics
    average,
    weighted_average,

    # Number theory
    is_prime,
    gcd,
    lcm,

    # Utility / Game math
    clamp,
    smoothstep,
    logistic,
)

__all__ = [
    "PI", "E",

    "fact", "fibonacci", "digital_root", "is_harshad",
    "triangular", "collatz_steps",

    "sqrt", "cbrt", "power",

    "ln", "log",

    "sin", "cos", "tan",

    "circumference", "area_circle", "area_square",
    "area_rectangle", "area_triangle",
    "perimeter_square", "perimeter_rectangle",
    "distance_2d", "cube_volume", "cube_surface_area",
    "pythagoras",

    "percentage", "simple_interest", "compound_interest",

    "average", "weighted_average",

    "is_prime", "gcd", "lcm",

    "clamp", "smoothstep", "logistic",
]
