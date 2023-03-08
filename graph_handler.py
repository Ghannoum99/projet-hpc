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

    def get_nodes(self):
        nodes = list()
        for i in range(self.get_nodes_nb()):
            nodes.append(i)
        return nodes

    # fonction permettant de créer un graphe
    def generate_graph(self):
        graph = []

        # Lire le fichier afin de générer un graphe
        with open(self.filename, 'r') as fp:
            for i, line in enumerate(fp):
                if i >= 4:
                    graph.append(line.strip().split('\t'))
        return graph

    def get_adj_matrix(self):
        size = self.get_nodes_nb()
        adj_mat = [[0 for i in range(size)] for j in range(size)]

        lines = self.generate_graph()
        # initialiser la matrice d'adjacence à 0
        for i in range(size):
            for j in range(size):
                adj_mat[i][j] = 0
        # remplir la matrice d'adjacence
        for i in lines:
            adj_mat[int(i[0])][int(i[1])] = 1

        for i in range(size):
            print("\n")
            for j in range(size):
                print("Ajd[" + str(i) +"][" + str(j) +"] : ", adj_mat[i][j], end="\t")
        return adj_mat

    def get_transition_matrix(self, ajd_matrix):
        # transposé de la matrice d'adjacence
        trans_mat_adj = np.transpose(ajd_matrix)
        # matrice de transition
        P = trans_mat_adj / trans_mat_adj.sum(axis=0)
        for i in range(len(P)):
            print("\n")
            for j in range(len(P)):
                print("P[" + str(i) +"][" + str(j) +"] : ", P[i][j], end="\t")
        return P

    def get_neigh(self, x):
        neigh = []
        graphe = self.generate_graph()
        for node in graphe:
            if x in node[0]:
                neigh.append(int(node[1]))

        return neigh

    def get_matrix_G(self):
        size = self.get_nodes_nb()
        G = [[0 for i in range(size)] for j in range(size)]
        for i in range(size):
            print("\n")
            for j in range(size):
                G[i][j] = 1/size
                print("G[" + str(i) + "][" + str(j) + "] : ", "%.5f" % G[i][j], end="\t")
        return G









