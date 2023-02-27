from fractions import Fraction

# Returns how often p is a factor of n.
def count_factors(n, p):
  count = 0
  while n % p == 0:
    count += 1
    n /= p

  return count

# Returns the p-adic distance of an integer value.
def padic_dist_int(n, p):
  return count_factors(n, p)

# Returns the p-adic distance of a rational number that.
def padic_dist(x, p):
  # p must be a positive integer
  if not isinstance(p, int):
    # Would be nicer with specific exceptions but .. meh
    raise Exception(f"p must be of type integer but {p} is of type {type(p)}")

  if p < 1:
    raise Exception(f"p must be positive but is {p}")

  # 0 is a special case (i.e. n**p will never be 0).
  # The distance of 0 is defined as 0.
  if x == 0:
    return 0
  
  # Branch out some 
  if isinstance(x, int):
    return padic_dist_int(x, p)
  
  if isinstance(x, float):
    frac = Fraction(x).limit_denominator()

    # Fraction.limit_denominator already reduces the shared factors so
    # the p-adic distance is just the larger one.
    num_dist = padic_dist_int(abs(frac.numerator), p)
    denom_dist = padic_dist_int(abs(frac.denominator), p)
    return max(num_dist, denom_dist)
  
  raise Exception(f"unsupported type {type(x)} for input x: {x}")
