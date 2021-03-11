# MAP WARMPUP
# Given the two lists of numbers below, produce a new iterable of their element-wise sums
# In this example, that'd be (21, 33, 3, 60...)
# Hint: look for a `from operator import ...`

one = [1,  2,  3, 40,  5, 66]
two = [20, 31, 0, 20, 55, 10]

# FILTER WARMPUP
# Take the following iterable, and filter out / remove any `(x, y)` elements where `x` is greater than `y`
# It's fine to use a lambda on this one
from itertools import count
b_iterable = enumerate(count(30, 4), start=500)

# Given the below iterable, produce a generator containing ONLY the next element of each iterator in the iterable
# For this example, that'd be (900, 4, 10, 0)
# Hint: the most important word in the above sentences was "next"

iterables = [
    (x**2 for x in range(30, 40)),
    (x**x for x in range(2, 10)),
    (x-4 for x in [14, 3, 11]),
    iter(range(20))
]

# Take the following iterable, and filter out / remove ALL `(x, y)` elements where `x` is LESS than `y`. Convert the result to a list.
# Hint: you'll want `from itertools import takewhile`, instead of just `filter`
from itertools import count
a_iterable = enumerate(count(30, 4), start=500)
