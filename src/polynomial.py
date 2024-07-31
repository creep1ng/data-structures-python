from typing import List

class Polynomial:
    
    _coefficients: List[float]

    def __init__(self, coefficients: List[float]) -> None:
        self._coefficients = coefficients

    def add(self, y) -> None:
        raise NotImplemented

    def __repr__(self) -> str:
        raise NotImplemented