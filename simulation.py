#!/usr/bin/python3
# Authors : Ulysse Feillet - Jihad GHANNOUM

import numpy as np
from itertools import islice
from ctypes import *
from pageRank import pageRank

damping_factor = 0.85
tolerance = 0.000001


def simulate_epidemic_pagerank_vaccinated(G, nb_infected, nb_vaccinated, infection_rate, recovery_rate,
                                          vaccination_rate):

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

    print("----------------")
    print("Final Infected: ", infected)
    print("Final vaccinated: ", vaccinated)


