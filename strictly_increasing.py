from operator import lt, and_
from doctest import testmod
from functools import reduce
from itertools import accumulate

def is_strictly_increasing(nums):
    """
    >>> is_strictly_increasing([1, 1, 2])
    False
    >>> is_strictly_increasing([1, 1, 1])
    False
    >>> is_strictly_increasing([2, 1, 3, 0])
    False
    >>> is_strictly_increasing([0, 2, 6, 17])
    True
    >>> is_strictly_increasing([1, 2, 2, 2, 2])
    False
    >>> is_strictly_increasing([-1, 0, 1, 0])
    False
    """
    # return all(list(accumulate(nums, lt))[1:])
    return all(map(lt, nums, nums[1:]))

testmod()
