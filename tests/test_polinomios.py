from src.polynomial import Polynomial
from unittest import TestCase

class TestPolynomial(TestCase):

    def test_add_same_size(self) -> None:
        p = Polynomial([3, 4, 5])
        q = Polynomial([1, 1, 1])

        p.add(q)

        expected = Polynomial([4, 5, 6])

        self.assertEqual(p, expected)

    def test_add_different_size_bigger_first(self) -> None:
        p = Polynomial([1, 2, 3, 4, 5])
        q = Polynomial([1, 1, 1])

        p.add(q)

        expected = Polynomial([2, 3, 4, 4, 5])

        self.assertEqual(p, expected)
        
    def test_add_different_size_smaller_first(self) -> None:
        p = Polynomial([1, 2, 3, 4, 5])
        q = Polynomial([1, 1, 1])

        q.add(p)

        expected = Polynomial([2, 3, 4, 4, 5])

        self.assertEqual(q, expected)

    def test_equals_true_case(self) -> None:
        p = Polynomial([1, 1, 1])
        q = Polynomial([1, 1, 1])

        expected = True

        self.assertEqual(p == q, expected)

    def test_equals_false_case(self) -> None:
        p = Polynomial([1, 1, 1])
        q = Polynomial([1, 2, 1])

        expected = False

        self.assertEqual(p == q, expected)
 