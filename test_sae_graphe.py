import sources.py as src

def test_collaborateurs_communs():
    assert src.collaborateurs_communs(G1,"","") == []
    assert src.collaborateurs_communs(G1,"","") == []
    assert src.collaborateurs_communs(G1,"","") == []
    assert src.collaborateurs_proches(G1,"L'inconnu du graphe","Al Pacino") is None

def test_collaborateurs_proches():
    assert src.collaborateurs_proches(G1,"",1) == []
    assert src.collaborateurs_proches(G1,"",2) == []
    assert src.collaborateurs_proches(G1,"",5) == []
    assert src.collaborateurs_proches(G1,"L'inconnu du graphe",10) is None

def test_est_proche():
    assert src.est_proche(G1,"Al Pacino","Jack Kehoe",1)
    assert src.est_proche(G1,"Marion Dougherty","Lynn Stalmaster",1)
    assert not src.est_proche(G1,"Syndey Armus","Peter Douglas",1)
    assert not src.est_proche(G1,"James Tolkan","Carl Reiner",1)

def test_distance_naive():
    assert src.distance_naive(G1, "Al Pacino","Jack Kehoe") == 1
    assert src.distance_naive(G1, "Marion Dougherty","Lynn Stalmaster") == 1
    assert src.distance_naive(G1, "","") == 1
    assert src.distance_naive(G1, "L'inconnu du graphe","Al Pacino") is None

def test_distance():
    assert src.distance(G1, "Al Pacino","Jack Kehoe") == 1
    assert src.distance(G1, "Marion Dougherty","Lynn Stalmaster") == 1
    assert src.distance(G1, "","") == 1
    assert src.distance(G1, "L'inconnu du graphe","Al Pacino") is None