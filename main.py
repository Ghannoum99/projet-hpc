#!/usr/bin/python3
# Authors : Ulysse Feillet - Jihad GHANNOUM
import math

import numpy as np
from math import *
from numpy.linalg import norm
from graph_handler import GraphHandler
from pageRank import pageRank
from simulation import simulate_epidemic_pagerank_vaccinated
from test import simulate_epidemic_pagerank_vaccinated
from simulation import *


if __name__ == '__main__':
    damping_factor = 0.85
    tolerance = 0.000001
    infection_rate = 0.2
    vaccination_rate = 0.24
    recovery_rate = 0.24

    graph = GraphHandler("test.txt")
    nodes_nb = graph.get_nodes_nb()

    nb_infected = int(nodes_nb * 0.3)
    # Nombre n d'individus vaccinés au départ (10% de la population)
    nb_vaccinated = math.ceil(nodes_nb * 0.1)

    simulate_epidemic_pagerank_vaccinated(graph, nb_infected, nb_vaccinated, infection_rate, recovery_rate,
                                          vaccination_rate)
