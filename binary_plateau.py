import numpy as np
import itertools


def solution(number):
    return max(len(list(v)) for g, v in itertools.groupby(np.binary_repr(number)))


for j in range(0, 648):
    print("Number", j, "has a binary plateau of", solution(j))


