import json
import networkx as nx

# Q1
def json_vers_nx(chemin):
    G = nx.Graph()
    cast = [actor.strip("[]") for actor in json_data.get("cast", [])]
    directors = [director.strip("[]") for director in json_data.get("directors", [])]
    producers = [producer.strip("[]") for producer in json_data.get("producers", [])]
    companies = [company.strip("[]") for company in json_data.get("companies", [])]
    for actor1 in cast:
        for actor2 in cast:
            if actor1 != actor2:
                G.add_edge(actor1, actor2)
    return G


# Q2
def collaborateurs_communs(G,u,v):
    liste_collabo = []
    for voisins1 in G.adj(u):
        for voisins2 in G.adj(v):
            if voisins1 == voisins2:
                liste_collabo.append(voisins1)
    return liste_collabo

# Q3     
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

def est_proche(G,u,v,k=1):
    return v in collaborateurs_proches(G,u,1)

def distance_naive(G,u,v):
    k = 1
    while v not in collaborateurs_proches(G,u,k):
        k += 1
    return k

def distance(G,u,v):
    pass

# Q4
def centralite(G,u):
    pass

def centre_hollywood(G):
    pass

# Q5
def eloignement_max(G:nx.Graph):
    pass

# Bonus
def centralite_groupe(G,S):
    pass