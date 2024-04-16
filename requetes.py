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
    pass

def est_proche(G,u,v,k=1):
    pass

def distance_naive(G,u,v):
    pass

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