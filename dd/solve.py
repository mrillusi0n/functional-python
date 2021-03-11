from problems import *

######## one ########
from operator import add

print(list(map(add, one, two)))

######## two ########
for _ in range(10):
    print(next(filter(lambda x: x[0] > x[1], b_iterable)))

######## three ########
print(list(map(next, iterables)))

######## four ########
from itertools import takewhile

print(list(takewhile(lambda x: x[0] > x[1], a_iterable)))
