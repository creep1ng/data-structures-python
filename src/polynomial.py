from typing import List
from abc import abstractmethod

class Polynomial:
    
    _coefficients: List[float]

    def __init__(self, coefficients: List[float]) -> None:
        self._coefficients = coefficients

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, y) -> bool:
        raise NotImplementedError

    def __add__(self, y) -> Polynomial:
        max_grade: int = max(len(self._coefficients, y._coefficients))

        self._coefficients.extend([0] * (max_grade - len(self._coefficients)))
        y._coefficients.extend([0] * (max_grade - len(y._coefficients)))

        result: List[float] = [self_i + y_i for self_i, y_i in zip(self._coefficients, y._coefficients)]

        return Polynomial(result)

    def add(self, y) -> None:
        self = self.__add__(self, y)