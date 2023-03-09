#!/usr/bin/python3
# Authors : Ulysse Feillet - Jihad GHANNOUM

import math
from itertools import islice
import matplotlib.pyplot as plt
from graph_handler import GraphHandler
import cProfile
import timeit
import numpy as np
from numpy.linalg import norm


def pageRank(P, damping_factor, tolerance):

    jumping_rate = 1 - damping_factor
    size = len(P)

    x = [0 for i in range(size)]
    x[0] = 1

    G = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            G[i][j] = 1 / size

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

        counter += 1
        diff = [new - old for old, new in zip(old_x, new_x)]
        # Normalisation
        N = norm(diff)

        if N < tolerance:
            break

    return new_x


def simulate_epidemic_pagerank_vaccinated(G, nb_infected, nb_vaccinated, infection_rate, recovery_rate,
                                          vaccination_rate):
    counter = 0
    counter_list = list()
    infected_list = list()

    nodes_nb = G.get_nodes_nb()

    # Calculer l'importance des nœuds en utilisant l'algorithme PageRank
    adj_matrix = G.get_adj_matrix()
    P = G.get_transition_matrix(adj_matrix)
    pr = pageRank(P, damping_factor, tolerance)
    print("pageRank scores: ", pr)

    infected = np.zeros(nodes_nb)

    infected_position = np.random.choice(infected.size, nb_infected, replace=False)
    infected[infected_position] = 1

    # Initialiser les états de vaccination des nœuds en fonction de leur ordre d'importance
    vaccinated = np.zeros(nodes_nb)

    # Position des n individus les plus importants pour qu'ils soient vaccinés
    top_n = sorted(pr, reverse=True)[:nb_vaccinated]
    most_important_positions = list(islice([i for i, v in enumerate(pr) if v in top_n], nb_vaccinated))
    vaccinated[most_important_positions] = 1

    print("\nInfected: ", infected)
    print("vaccinated: ", vaccinated)
    print("----------------\n")

    #tant qu'il y a des individus infectés
    while (not np.all(infected == 0)):
        counter += 1
        counter_list.append((counter))
        for i in range(nodes_nb):
            # si individu infecté, étape de possible infection de ses voisins
            if infected[i] == 1:
                neighbors = G.get_neighbors(str(i))
                for j in neighbors:
                    if infected[j] == 0 and vaccinated[j] == 0 and np.random.rand() < pr[j] * infection_rate:
                        print("Infection !")
                        infected[j] = 1

                #étape de guérison
                if np.random.rand() < recovery_rate:
                    print("Guérison !")
                    infected[i] = 0

            # si individu non infecté, étape de possible infection venant de ses voisins
            elif infected[i] == 0 and vaccinated[i] == 0:
                neighbors = G.get_neighbors(str(i))
                for j in neighbors:
                    if infected[j] == 1 and np.random.rand() < pr[j]:
                        print("Infection !")
                        infected[i] = 1
                        break
            #pas d'infection si vaccination
            elif vaccinated[i] == 1:
                pass
        infected_list.append(analysis_result(infected))

    plt.plot(counter_list, infected_list)
    plt.xlabel("Nombre d'itérations")
    plt.ylabel("Ratio nombre d'individus infectés sur le nombre total d'individus")
    plt.show()
    print("----------------")
    print("Final Infected: ", infected)
    print("Final vaccinated: ", vaccinated)


def analysis_result(infected):
    infected_number = 0
    for node in infected:
        if node == 1 :
            infected_number += 1
    return infected_number/len(infected)


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