def true_zip(*iters):
    heads = list(map(next, iters))

    if heads == []:
        return

    yield heads
    yield from true_zip(*iters)

def two_zip(g_one, g_two):
    try:
        first, *r_one = g_one
        second, *r_two = g_two
    except:
        return

    yield first, second
    yield from two_zip(r_one, r_two)


res = true_zip(iter([1, 3, 4]), iter([2, 3, 4]), iter([4, 18]))

for i in res:
    print(i)

# print(*next(res))
# print(*next(res))
