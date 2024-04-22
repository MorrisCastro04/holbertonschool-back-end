#!/usr/bin/python3
"""
Takes a string `k` and a number `v` 
and returns a tuple with `k` as the first element and the 
square of `v` as the second element.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    return (k, v**2)
