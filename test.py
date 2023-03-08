import networkx as nx
import random
import matplotlib.pyplot as plt
from pageRank import pageRank
import networkx as nx
import random
import matplotlib.pyplot as plt



def simulate_epidemic_pagerank_vaccinated(G, initial_infected, initial_vaccinated, infection_rate, recovery_rate,
                                          vaccination_rate, simulation_duration):
    """
    Simule la propagation d'une épidémie dans un graphe donné en utilisant l'algorithme PageRank pour déterminer les
    nœuds les plus importants dans la propagation de l'épidémie. Prend en compte trois états: infecté, guéri et vacciné

    Args:
    - G: le graphe à simuler
    - initial_infected: le nombre initial de personnes infectées
    - initial_vaccinated: le nombre initial de personnes vaccinées
    - infection_rate: le taux de transmission de l'infection
    - recovery_rate: le taux de guérison de l'infection
    - vaccination_rate: le taux de vaccination des personnes non-infectées
    - simulation_duration: la durée de la simulation en jours

    Returns:
    - infected_history: l'historique du nombre de personnes infectées à chaque jour
    - recovered_history: l'historique du nombre de personnes guéries à chaque jour
    - vaccinated_history: l'historique du nombre de personnes vaccinées à chaque jour
    """

    adj_mat = G.get_adj_matrix()
    transition_mat = G.get_transition_matrix(adj_mat)
    nodes = G.get_nodes(G.get_nodes_nb())

    # Calcul des scores PageRank des nœuds
    pagerank_scores = pageRank(transition_mat, 0.85, 0.000001)

    # Sélection des personnes infectées initiales et vaccinées
    sorted_nodes = sorted(pagerank_scores, key=pagerank_scores, reverse=True)
    infected_nodes = sorted_nodes[:initial_infected]
    vaccinated_nodes = set(random.sample(set(nodes) - set(infected_nodes), initial_vaccinated))

    # Initialisation des variables
    susceptible_nodes = set(G.get_nodes()) - set(infected_nodes) - vaccinated_nodes
    recovered_nodes = set()
    infected_history = [initial_infected]
    recovered_history = [0]
    vaccinated_history = [initial_vaccinated]

    # Simulation de la propagation de l'infection
    for day in range(simulation_duration):
        newly_infected_nodes = set()
        newly_recovered_nodes = set()
        newly_vaccinated_nodes = set()

        # Transmission de l'infection
        for infected_node in infected_nodes:
            for neighbor_node in G.neighbors(infected_node):
                if neighbor_node in susceptible_nodes and random.random() < infection_rate:
                    newly_infected_nodes.add(neighbor_node)

        # Guérison de l'infection
        for infected_node in infected_nodes:
            if random.random() < recovery_rate:
                newly_recovered_nodes.add(infected_node)

        # Vaccination
        for susceptible_node in susceptible_nodes:
            if random.random() < vaccination_rate:
                newly_vaccinated_nodes.add(susceptible_node)

        # Mise à jour des variables
        susceptible_nodes -= newly_infected_nodes
        susceptible_nodes -= newly_vaccinated_nodes
        infected_nodes |= newly_infected_nodes
        infected_nodes -= newly_recovered_nodes
        recovered_nodes |= newly_recovered_nodes
        vaccinated_nodes |= newly_vaccinated_nodes

        infected_history.append(len(infected_nodes))
        recovered_history.append(len(recovered_nodes))
        vaccinated_history.append(len(vaccinated_nodes))

    return infected_history, recovered_history
