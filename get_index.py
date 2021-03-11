from functools import reduce
# Create a function that takes two arguments `element`, `iterable`, and returns the index of the FIRST occurrence of `element` in iterable, if any, otherwise `None`
x, y = 2, [1, 2, 3]  # returns 1
x, y = 1, [1, 2, 3, 1, 2, 3] # returns 0
x, y = 4, [2, 4, 4, 4, 4, 4, 4] # returns 1
x, y = 12, range(2, 20, 2)
x, y = 5, [1, 2, 3] # returns None
x, y = 1, [] # returns None

def get_index(k, itr):
    return reduce(lambda state, val: state if state is not None else val[0] if val[1] == k else None,
                  enumerate(itr), None)

def get_index(k, itr):
    return reduce(lambda state, val: state if state is not None else val[0] if val[1] == k else None,
                  enumerate(itr), None)

def get_index(k, itr):
    return reduce(lambda state, val: state if state[1] else (state[0] + 1, k == val),
                  itr, (0, False))

def get_index(k, itr):
    return reduce(lambda state, val: (state[0] + 1 * state[1], k == val),
                  itr, (-1, True))

print(get_index(2, [1, 2, 3]))  # returns 1
print(get_index(1, [1, 2, 3, 1, 2, 3])) # returns 0
print(get_index(4, [2, 4, 4, 4, 4, 4, 4])) # returns 1
print(get_index(12, range(2, 20, 2)))
print(get_index(5, [1, 2, 3])) # returns None
print(get_index(1, [])) # returns None
