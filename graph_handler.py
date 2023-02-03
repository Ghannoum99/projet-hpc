#!/usr/bin/python3
# Authors : Ulysse Feillet - Jihad GHANNOUM
import linecache


class GraphHandler:

    def __init__(self, filename):
        self.filename = filename

    # fonction permettant de récupérer le nombre de noeuds
    def get_nodes_nb(self):
        line = linecache.getline(self.filename, 3)
        line = line.split()
        nodes_nb = line[2]
        return nodes_nb

    # fonction permettant de récupérer le nombre de liens
    def get_edges_nb(self):
        line = linecache.getline(self.filename, 3)
        line = line.split()
        edges_nb = line[4]
        return edges_nb

    # fonction permettant de créer un graphe
    def generate_graph(self):
        lines_nb = sum(1 for line in open(self.filename))
        mat_adj = [[0 for i in range(lines_nb)] for j in range(lines_nb)]

        # initialiser la matrice d'adjacence à 0
        """for i in range(lines_nb):
            for j in range(lines_nb):
                mat_adj[i][j] = 0"""

        lines = []

        # Lire le fichier afin de générer un graphe
        with open(self.filename, 'r') as fp:
            for i, line in enumerate(fp):
                if i >= 4:
                    lines.append(line.strip().split('\t'))

        # remplir la matrice d'adjacence
        """for i in lines:
            mat_adj[int(i[0]) - 1][int(i[1]) - 1] = 1
            print(i[1])"""


if __name__ == '__main__':
    graphe = GraphHandler("Wiki-Vote.txt")
    graphe.generate_graph()