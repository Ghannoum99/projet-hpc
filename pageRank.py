#!/usr/bin/python3
# Authors : Ulysse Feillet - Jihad GHANNOUM

import numpy as np
from numpy.linalg import norm


def pageRank(P, damping_factor, tolerance):
    jumping_rate = 1 - damping_factor

    size = len(P)
    G = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            G[i][j] = 1 / size

    x = [0 for i in range(size)]
    x[0] = 1

    old_x = []
    new_x = []
    counter = 0

    new_x = x

    while True:
        old_x = new_x
        # P * x
        new_x = np.array(P).dot(old_x)
        # P * alpha * x
        new_x = new_x * damping_factor
        # (P * alpha * X) + ((1 - alpha) * G * X)
        new_x = new_x + ((jumping_rate) * np.array(G).dot(old_x))
        """print("\n")
        for i in range(size):
            print("new_x[" + str(i) + "] : ", "%.9f" % new_x[i], end="\t")"""

        counter += 1
        diff = [new - old for old, new in zip(old_x, new_x)]
        # Normalisation
        N = norm(diff)

        if N < tolerance:
            break

    return new_x


