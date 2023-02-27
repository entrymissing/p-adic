def count_factors(n, p):
  count = 0
  while n % p == 0:
    count += 1
    n /= p

  return count

def padic_distance(n, p):
  return count_factors(n, p)

def padic_distance_rational(x, p):
    num_dist = padic_distance(abs(x.numerator), p)
    denom_dist = padic_distance(abs(x.denominator), p)
    return max(num_dist, denom_dist)