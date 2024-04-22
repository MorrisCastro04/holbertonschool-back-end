#!/usr/bin/python3
"""Returns a function that multiplies a given number by the specified multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def mult(num: float) -> float:
        return num * multiplier

    return mult
