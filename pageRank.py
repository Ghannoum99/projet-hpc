#!/usr/bin/python3
# Authors : Ulysse Feillet - Jihad GHANNOUM

import numpy as np
from numpy.linalg import norm
from graph_handler import GraphHandler


def pageRank(P, damping_factor, tolerance):
    jumping_rate = 1 - damping_factor

    size = len(P)
    G = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        print("\n")
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
        print("\n")
        for i in range(size):
            print("new_x[" + str(i) + "] : ", "%.9f" % new_x[i], end="\t")

        counter += 1
        diff = [new - old for old, new in zip(old_x, new_x)]
        # Normalisation
        N = norm(diff)

        if N < tolerance:
            break
    print("\n fini à l'itération : ", counter)
    return new_x




if __name__ == '__main__':
    damping_factor = 0.85
    tolerance = 0.000001
    graph = GraphHandler("test.txt")
    graph.generate_graph()
    size = graph.get_nodes_nb()
    adj_matrix = graph.get_adj_matrix()
    P = graph.get_transition_matrix(adj_matrix)

    pageRank(P, damping_factor, tolerance)