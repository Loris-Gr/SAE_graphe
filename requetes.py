# Q1
def json_vers_nx(chemin):
    pass

# Q2
def collaborateurs_communs(G,u,v):
    pass

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