#!/usr/bin/python3
# Authors : Ulysse Feillet - Jihad GHANNOUM
import linecache

class GraphHandler:
    def __init__(self, filename):
        self.filename = filename

    def get_nodes_nb(self):
        line = linecache.getline(self.filename, 3)
        line = line.split()
        nodes_nb = line[2]
        return nodes_nb

    def get_edges_nb(self):
        line = linecache.getline(self.filename, 3)
        line = line.split()
        edges_nb = line[4]
        return edges_nb



    """def generate_graph(self, filename):
        line_numbers = [3, 4]
        lines = []
        for i in line_numbers:
            x = linecache.getline(filename, i).strip()
            lines.append(x)
        print(lines)"""


if __name__ == '__main__':
    graphe = GraphHandler("Wiki-Vote.txt")
    graphe.get_nodes_nb()