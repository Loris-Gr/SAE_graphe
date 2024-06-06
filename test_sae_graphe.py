import sources.py as src

graphe = json_vers_nx("./data_100.txt")

def test_collaborateurs_communs():
    assert src.collaborateurs_communs(graphe,"Al Pacino","Jack Kehoe") == ['Robert De Niro', 'Robert Redford', 'John Travolta', 'Andy García', 'Richard Bright (actor)|Richard Bright', 'John Randolph (actor)|John Randolph', 'Biff McGuire', 'Barbara Eda-Young', 'Cornelia Sharpe', 'Edward Grover', 'Tony Roberts (actor)|Tony Roberts', 'Allan Rich', 'Albert Henderson (actor)|Albert Henderson', 'Joseph Bova', 'Woodie King Jr.', 'James Tolkan', 'Bernard Barrow', 'Nathan George', 'M. Emmet Walsh', 'Ted Beniades', 'F. Murray Abraham', 'Judd Hirsch', 'James Caan', 'Charles Grodin', 'Jerry Orbach', 'Philip Baker Hall', 'Michael V. Gazzo', 'Paul Sorvino', 'Joe Santos', 'Sully Boyar', 'Pepe Serna', 'William Forsythe (actor)|William Forsythe', 'Charles Durning', 'Philip Sterling', 'Gene Hackman', 'Eileen Brennan', 'Warren Beatty', 'Madonna', 'Glenne Headly', 'Charlie Korsmo', 'James Keane', 'Seymour Cassel', 'Michael J. Pollard', 'Dick Van Dyke', 'Frank Campanella', 'Kathy Bates', 'Dustin Hoffman', "Ed O'Ross", 'Mandy Patinkin', 'R. G. Armstrong', 'Henry Silva', 'Chuck Hicks', 'Neil Summers', 'Stig Eldred', 'Lawrence Steven Meyers', "Catherine O'Hara", 'Robert Beecher', 'Rita Bland, Lada Boder, Dee Hengstler, Liz Imperio, Michelle Johnston, Karyne Ortega', 'Lew Horn', 'Mike Hagerty', 'Arthur Malet', 'Bert Remsen', "Michael Donovan O'Donnell", 'Tom Signorelli', 'Jim Wilkey', 'Mary Woronov']
    assert src.collaborateurs_communs(graphe,"Mary Woronov","Jack Kehoe") == ['Warren Beatty', 'Al Pacino', 'Madonna', 'Glenne Headly', 'Charlie Korsmo', 'James Keane', 'Seymour Cassel', 'Michael J. Pollard', 'Charles Durning', 'Dick Van Dyke', 'Frank Campanella', 'Kathy Bates', 'Dustin Hoffman', 'William Forsythe (actor)|William Forsythe', "Ed O'Ross", 'James Tolkan', 'Mandy Patinkin', 'R. G. Armstrong', 'Henry Silva', 'Paul Sorvino', 'Chuck Hicks', 'Neil Summers', 'Stig Eldred', 'Lawrence Steven Meyers', 'James Caan', "Catherine O'Hara", 'Robert Beecher', 'Rita Bland, Lada Boder, Dee Hengstler, Liz Imperio, Michelle Johnston, Karyne Ortega', 'Lew Horn', 'Mike Hagerty', 'Arthur Malet', 'Bert Remsen', "Michael Donovan O'Donnell", 'Tom Signorelli', 'Jim Wilkey']
    assert src.collaborateurs_proches(graphe,"Al Pacino", "L'inconnu du graphe") is None
    assert src.collaborateurs_proches(graphe,"L'inconnu du graphe","Al Pacino") is None

def test_collaborateurs_proches():
    assert src.collaborateurs_proches(graphe,"Marion Dougherty",1) == {'Diane Lane', 'Jeff Bridges', 'Martin Scorsese', 'Lynn Stalmaster', 'Richard Dreyfuss', 'Danny Glover', 'Jon Voight', 'Robert Duvall', 'Woody Allen', 'Glenn Close', 'Marion Dougherty', 'Robert De Niro', 'Robert Redford', 'John Travolta', 'Bette Midler', 'Al Pacino', 'Clint Eastwood'}
    assert src.collaborateurs_proches(graphe,"Marion Dougherty",0) == {'Marion Dougherty'}
    assert src.collaborateurs_proches(graphe,"Marion Dougherty",-1) == {'Marion Dougherty'}
    assert src.collaborateurs_proches(graphe,"L'inconnu du graphe",10) is None

def test_est_proche():
    assert src.est_proche(graphe,"Al Pacino","Jack Kehoe",1)
    assert src.est_proche(graphe,"Marion Dougherty","Lynn Stalmaster",1)
    assert not src.est_proche(graphe,"Syndey Armus","Peter Douglas",1)
    assert not src.est_proche(graphe,"James Tolkan","Carl Reiner",1)

def test_distance_naive():
    assert src.distance_naive(graphe, "Al Pacino","Jack Kehoe") == 1
    assert src.distance_naive(graphe, "Marion Dougherty","Lynn Stalmaster") == 1
    assert src.distance_naive(graphe, "John Goodman", "James Ransone") == 2
    assert src.distance_naive(graphe, "L'inconnu du graphe","Al Pacino") is None

def test_distance():
    assert src.distance(graphe, "Al Pacino","Jack Kehoe") == 1
    assert src.distance(graphe, "Marion Dougherty","Lynn Stalmaster") == 1
    assert src.distance(graphe, "John Goodman", "James Ransone") == 2
    assert src.distance(graphe, "L'inconnu du graphe","Al Pacino") is None