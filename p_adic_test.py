import unittest

from p_adic import count_factors, padic_dist

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
  def test_padic_dist(self):
    # p-adic distance of 0 is 0
    self.assertEqual(padic_dist(0, 2), 0)
    self.assertEqual(padic_dist(0, 5), 0)

    # distances of some integers
    self.assertEqual(padic_dist(2, 2), 1)
    self.assertEqual(padic_dist(2, 3), 0)
    self.assertEqual(padic_dist(6, 2), 1)
    self.assertEqual(padic_dist(6, 3), 1)
    self.assertEqual(padic_dist(18, 3), 2)

    # distances of some floats
    self.assertEqual(padic_dist(0.5, 2), 1)
    self.assertEqual(padic_dist(0.25, 2), 2)
    self.assertEqual(padic_dist(0.25, 3), 0)
    self.assertEqual(padic_dist(0.3, 3), 1)

    # float 0
    self.assertEqual(padic_dist(0.0, 3), 0)

  def test_padic_dist_errors(self):
    # p cannot be a float
    with self.assertRaises(Exception):
      padic_dist(4, 0)

    # p cannot be negative
    with self.assertRaises(Exception):
      padic_dist(3, -1)

    # n must be int or float
    with self.assertRaises(Exception):
      padic_dist("0.111")

if __name__ == '__main__':
    unittest.main()