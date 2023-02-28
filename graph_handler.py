#!/usr/bin/python3
# Authors : Ulysse Feillet - Jihad GHANNOUM
import linecache
import numpy as np
from numpy.linalg import norm

class GraphHandler:

    def __init__(self, filename):
        self.filename = filename

    # fonction permettant de récupérer le nombre de noeuds
    def get_nodes_nb(self):
        line = linecache.getline(self.filename, 3)
        line = line.split()
        nodes_nb = line[2]
        return int(nodes_nb)

    # fonction permettant de récupérer le nombre de liens
    def get_edges_nb(self):
        line = linecache.getline(self.filename, 3)
        line = line.split()
        edges_nb = line[4]
        return int(edges_nb)

    # fonction permettant de créer un graphe
    def generate_graph(self):
        lines_nb = sum(1 for line in open(self.filename))
        mat_adj = [[0 for i in range(lines_nb)] for j in range(5)]

        # initialiser la matrice d'adjacence à 0
        for i in range(5):
            for j in range(5):
                mat_adj[i][j] = 0

        lines = []

        # Lire le fichier afin de générer un graphe
        with open(self.filename, 'r') as fp:
            for i, line in enumerate(fp):
                if i >= 4:
                    lines.append(line.strip().split('\t'))

        # remplir la matrice d'adjacence
        for i in lines:
            if i < lines_nb:
                mat_adj[int(i[0]) - 1][int(i[1]) - 1] = 1
                print(i[1])


if __name__ == '__main__':
    damping_factor = 0.85
    jumping_rate = 1 - damping_factor
    tolerance = 0.000001
    x = [1, 0, 0]
    P = [[5, 1, 3],
         [1, 1, 1],
         [1, 2, 1]]
    G = [[1/3, 1/3, 1/3],
         [1/3, 1/3, 1/3],
         [1/3, 1/3, 1/3]]

    old_x = []
    new_x = []
    counter = 0

    #graphe = GraphHandler("Wiki-Vote.txt")
    #graphe.generate_graph()
    #size = graphe.get_nodes_nb()
    size = 4

    new_x = x

    while True :
        old_x = new_x
        # P * x
        new_x = np.array(P).dot(old_x)
        new_x = new_x * damping_factor
        new_x = new_x + ((jumping_rate) * np.array(G).dot(old_x))

        counter += 1
        diff = [new - old for old, new in zip(old_x, new_x)]
        N = norm(diff)
        print(N)
        print(counter)
        if N < tolerance:
            break








