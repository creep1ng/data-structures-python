from abc import ABC, abstractmethod

class Parking:
    _free_spaces: int
    _initial_free_spaces: int

class ICounter(ABC):

    @abstractmethod
    def increment() -> None:
        ...

    @abstractmethod
    def decrement() -> None:
        ...

    @abstractmethod
    def get_counter() -> int:
        ...

class ParkingCounter(Parking, ICounter): 

    def __init__(self, initial_free_spaces) -> None:
        if initial_free_spaces <= 0:
            raise ValueError("`initial_free_spaces` must be a positive non-zero value.")

        self._free_spaces = initial_free_spaces
        self._initial_free_spaces = initial_free_spaces

    def increment(self) -> None:
        self._free_spaces += 1

    def decrement(self) -> None:
        if self._free_spaces == 0:
            raise ValueError("There are no more free spaces!")
        else:
            self._free_spaces -= 1

    def get_counter() -> int:
        return self._free_spaces