import unittest

from fractions import Fraction

from p_adic import count_factors, padic_distance_rational

class TestFactorization(unittest.TestCase):
  def test_count_factors(self):
    self.assertEqual(count_factors(2, 2), 1)
    self.assertEqual(count_factors(2, 3), 0)
    self.assertEqual(count_factors(81, 3), 4)
    self.assertEqual(count_factors(121, 11), 2)
    self.assertEqual(count_factors(122, 11), 0)
    self.assertEqual(count_factors(15, 3), 1)
    self.assertEqual(count_factors(15, 5), 1)
    # TODO: Add 0 and negative values

class TestPAdicDistance(unittest.TestCase):
  def test_padic_distance_rational(self):
    self.assertEqual(padic_distance_rational(Fraction(1, 2), 2), 1)
    self.assertEqual(padic_distance_rational(Fraction(2, 1), 2), 1)

    self.assertEqual(padic_distance_rational(Fraction(1, 3), 2), 0)
    self.assertEqual(padic_distance_rational(Fraction(3, 1), 2), 0)

    self.assertEqual(padic_distance_rational(Fraction(1, 4), 2), 2)
    self.assertEqual(padic_distance_rational(Fraction(4, 1), 2), 2)

    self.assertEqual(padic_distance_rational(Fraction(4, 2), 2), 1)
    self.assertEqual(padic_distance_rational(Fraction(4, 3), 2), 2)


if __name__ == '__main__':
    unittest.main()