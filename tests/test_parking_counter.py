from unittest import TestCase
from src.parking_counter import ParkingCounter

class TestParkingCounter(TestCase):

    def test_get(self) -> None:
        initial: int = 10
        test_parking = ParkingCounter(10)

        assert initial == test_parking.get_counter()