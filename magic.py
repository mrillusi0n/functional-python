from operator import gt, and_, mul, add
from functools import partial

def magic(nums):
    nums1 = []
    for num in nums:
        if num < 20:
            x = num ** 2
            nums1.append(x)

    nums2 = []
    for num in nums1:
        y = abs(num)
        if 1 & y:
            z = 2 * (1 + y)
            nums2.append(z)

    return nums2

def compose(f, *fs):
    if not fs:
        return f
    return lambda x: f(compose(*fs)(x))

def magik(nums):
    two = map(compose(partial(mul, 2), partial(add, 1)),
          filter(partial(and_, 1),
          map(abs, map(partial(pow, exp=2), filter(partial(gt, 20), nums)))))

    return list(two)


majik = compose(
    list,
    partial(map, compose(partial(mul, 2), partial(add, 1))),
    partial(filter, partial(and_, 1)),
    partial(map, abs),
    partial(map, partial(pow, exp=2)),
    partial(filter, partial(gt, 20)))
    

# magikk = partial(

inc = lambda x: x + 1

print(magic([1, 2, 3, 4]))
print(magik([1, 2, 3, 4]))
print(majik([1, 2, 3, 4]))
print(compose(inc)(2))
