import numpy as np
import itertools


def solution(number):

    binary = np.binary_repr(number)
    return max(len(list(v)) for g, v in itertools.groupby(binary))


for j in range(0, 100):
    print("Number", j, "Binary plateau: ", solution(j))


