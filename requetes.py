import json
import networkx as nx
import matplotlib as plt

# Q1
def json_vers_nx(chemin):
    G = nx.Graph()
    with open(chemin, mode="r", encoding="utf-8") as jsonfile:
        for ligne in jsonfile:
            acteurs = json.loads(ligne)["cast"]
            acteurs2 = []
            for charac in acteurs:
                acteurs2.append(charac.strip("[]"))
            for acteur1 in acteurs2:
                for acteur2 in acteurs2:
                    if acteur1 != acteur2:
                        G.add_edge(acteur1, acteur2)
    return G

# Q2
def collaborateurs_communs(G,u,v):
    """fonction consiste à renvoyer pour deux acteurs/actrices donné.e.s, l’ensemble des acteurs/actrices
qui ont collaboré.e.s avec ces deux personnes

    Args:
        G (nx.Graph): un graphe d'acteurs
        u (String): l'acteur/actrice 1
        v (String): l'acteur/actrive 2

    Returns:
        List: la liste des acteurs communs
    """    
    """fonction consiste à renvoyer pour deux acteurs/actrices donné.e.s, l’ensemble des acteurs/actrices
qui ont collaboré.e.s avec ces deux personnes

    Args:
        G (nx.Graph): un graphe d'acteurs
        u (String): l'acteur/actrice 1
        v (String): l'acteur/actrive 2

    Returns:
        List: la liste des acteurs communs
    """    
    liste_collabo = []
    for voisins1 in G.adj[u]:
        for voisins2 in G.adj[v]:
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
        print(u," est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

def est_proche(G,u,v,k=1):
    return v in collaborateurs_proches(G,u,k)

def distance_naive(G,u,v):
    k = 1
    while v not in collaborateurs_proches(G,u,k):
        k += 1
    return k

def distance(G,u,v):
    if u not in G.nodes:
        print(u," est un illustre inconnu")
        return None
    if v not in G.nodes:
        print(v," est un illustre inconnu")
        return None
    distance_trouvee = False
    distance = 0
    collaborateurs = set()
    collaborateurs.add(u)
    while not distance_trouvee :
        distance+=1
        for i in range(distance):
            collaborateurs_directs = set()
            for c in collaborateurs:
                for voisin in G.adj[c]:
                    if voisin not in collaborateurs:
                        collaborateurs_directs.add(voisin)
            collaborateurs = collaborateurs.union(collaborateurs_directs)
            if v in collaborateurs :
                return distance
            
# Q4
def centralite(G,u):
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = {u: 0} 
    acteurs_en_cours = [u]
    distance = 0
    while len(acteurs_en_cours) > 0 :
        acteur = acteurs_en_cours.pop(0)
        for l_acteur_en_cours in G[acteur]:
            if l_acteur_en_cours not in collaborateurs:
                acteurs_en_cours.append(l_acteur_en_cours)
                collaborateurs[l_acteur_en_cours] = collaborateurs[acteur] + 1
                distance = max(distance, collaborateurs[l_acteur_en_cours])
    return distance

def centre_hollywood(G):
    """Fonction qui renvoie la personne la plus au centre d'Hollywood,
      c'est à dire l'acteur qui a la plus faible centralité

    Args:
        G (nx.Graph): un graphe d'acteurs

    Returns:
        String : l'acteur central
    """    
    acteur_central = None
    distance_acteur_centrale = None
    for acteur in G.nodes :
        distance = centralite(G, acteur)
        if distance_acteur_centrale is None or distance < distance_acteur_centrale :
            distance_acteur_centrale = distance
            acteur_central = acteur
    return acteur_central

# Q5
def eloignement_max(G:nx.Graph):
    """fonction qui calcule l'éloignement maximal de tout les acteurs du graphe G

    Args:
        G (nx.Graph): un graphe d'acteurs

    Returns:
        int : l'éloignement maximal
    """    
    centralite_max = None
    for acteur in G.nodes :
        distance = centralite(G, acteur)
        if centralite_max is None or distance > centralite_max :
            centralite_max = None
    return centralite_max

# Bonus
def centralite_groupe(G,S):
    pass

#pour tests :

graphe = json_vers_nx("./data_100.txt")

#print(collaborateurs_communs(graphe,"Al Pacino", "James Woods"))

#print(collaborateurs_proches(graphe, "Al Pacino", 3))

#print(est_proche(graphe, "Paul Newman", "Alicia Witt"))

#print(distance_naive(graphe, "John Travolta", "Ellen Barkin"))

#print(distance(graphe, "John Travolta", "Ellen Barkin"))

print(centralite2(graphe, "Al Pacino"))

#print(eloignement_max(graphe))