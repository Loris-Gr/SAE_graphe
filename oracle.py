import requetes
import time

def programme_principal():
    entree = "1"
    graphe = None
    print("Bonjour ! Bienvenue dans la consultation !\n")
    fichier = input("Quelle fichier voulez-vous utiliser ? \n data_100.txt ? Si oui tapez 1 ! \n data_1000.txt ? Si oui tapez 2 ! \n data_10000.txt ? Si oui tapez 3 ! \n")
    while graphe is None : 
        if fichier == "1" :
            graphe = requetes.json_vers_nx("./data_100.txt")
        elif fichier == "2" :
            graphe = requetes.json_vers_nx("./data_1000.txt")
        elif fichier == "3" :
            graphe = requetes.json_vers_nx("./data_10000.txt")
        else :
            fichier = input("Vous avez du faire une erreur, tapez : \n 1  : Pour utiliser le fichier avec 100 données. \n 2 : Pour utiliser avec 1000 données \n 3 : Pour utiliser avec 10000 données \n")
    entree = input("Maintenant passons à la consultation ! \n Si vous voulez connaître les collaborateurs communs de deux acteurs tapez 1 ! \n Si vous voulez avoir des informations sur les collaborateurs proches d'un acteur tapez 2 ! \n Si vous voulez avoir des connaître la distance entre deux acteurs tapez 3 ! \n Peut-être voulez-vous connaître la centralité d'un acteur ? Si oui tapez 4 ! \n Si vous souhaitez l'acteur central d'Hollywood tapez 5 ! \n Pour connaître l'éloignement maximal de tout les acteurs tapez 6 ! \n Si vous voulez quitter le menu d'interaction tapez 7 ! \n ")        
      
    while entree in "1234567" :
        if entree == "1" : 
            while entree == "1":
                acteur1 = None
                acteur2 = None
                while acteur1 not in graphe.nodes :
                    acteur1 = input("Pour commencer quel est votre 1er acteur ? Attention à bien mettre les majuscules ! \n")
                while acteur2 not in graphe.nodes :
                    acteur2 = input("Quel est votre 2ème acteur ? Attention à bien mettre les majuscules ! \n")
                print("Voici la liste des collaborateurs communs à " + acteur1 + " et " + acteur2 + " :\n")
                for acteur in requetes.collaborateurs_communs(graphe, acteur1, acteur2) :
                    print(acteur)
                time.sleep(3)
                entree = input("Nous avons fait le tour des informations pour les collaborateurs communs de " + acteur1 + " et " + acteur2 + " ! \n Pour consulter les collaborateurs communs de deux autres acteurs tapez 1 ! \n Si vous voulez avoir des informations sur les collaborateurs proches d'un acteur tapez 2 ! \n Si vous voulez avoir des connaître la distance entre deux acteurs tapez 3 ! \n Peut-être voulez-vous connaître la centralité d'un acteur ? Si oui tapez 4 ! \n Si vous souhaitez l'acteur central d'Hollywood tapez 5 ! \n Pour connaître l'éloignement maximal de tout les acteurs tapez 6 ! \n Si vous voulez quitter le menu d'interaction tapez 7 ! \n")
        if entree == "2" :
            while entree == "2":
                acteur = None
                while acteur not in graphe.nodes :
                    acteur = input("Pour commencer quel est votre acteur ? Attention à bien mettre les majuscules ! \n")
                k = int(input("Quel distance voulez-vous essayez ? \n"))
                print("Voici la liste des collaborateurs proches de " + acteur + " pour une distance de  " + str(k) + ":\n")
                for acteur in requetes.collaborateurs_proches(graphe, acteur, k) :
                    print(acteur)
                time.sleep(3)
                entree = input("Nous avons fait le tour des informations pour les collaborateurs proches de " + acteur + " pour une distance de  " + str(k) + " ! \n Pour consulter les collaborateurs communs de deux acteurs tapez 1 ! \n Si vous voulez avoir des informations sur les collaborateurs proches d'un autre acteur ou d'une autre distance tapez 2 ! \n Si vous voulez avoir des connaître la distance entre deux acteurs tapez 3 ! \n Peut-être voulez-vous connaître la centralité d'un acteur ? Si oui tapez 4 ! \n Si vous souhaitez l'acteur central d'Hollywood tapez 5 ! \n Pour connaître l'éloignement maximal de tout les acteurs tapez 6 ! \n Si vous voulez quitter le menu d'interaction tapez 7 ! \n")
        
        if entree == "3" : 
            while entree == "3":
                acteur1 = None
                acteur2 = None
                while acteur1 not in graphe.nodes :
                    acteur1 = input("Pour commencer quel est votre 1er acteur ? Attention à bien mettre les majuscules ! \n")
                while acteur2 not in graphe.nodes :
                    acteur2 = input("Quel est votre 2ème acteur ? Attention à bien mettre les majuscules ! \n")
                print(acteur1 + " et " + acteur2 + "ont une distance de : " + str(requetes.distance(graphe,acteur1,acteur2)) +" \n")
                time.sleep(3)
                entree = input("Nous avons fait le tour des informations pour la distance entre " + acteur1 + " et " + acteur2 + " ! \n Pour consulter les collaborateurs communs de deux acteurs tapez 1 ! \n Si vous voulez avoir des informations sur les collaborateurs proches d'un acteur tapez 2 ! \n Si vous voulez avoir des connaître la distance entre deux autres acteurs tapez 3 ! \n Peut-être voulez-vous connaître la centralité d'un acteur ? Si oui tapez 4 ! \n Si vous souhaitez l'acteur central d'Hollywood tapez 5 ! \n Pour connaître l'éloignement maximal de tout les acteurs tapez 6 ! \n Si vous voulez quitter le menu d'interaction tapez 7 ! \n")
        
        if entree == "4" :
            while entree == "4":
                acteur = None
                while acteur not in graphe.nodes :
                    acteur = input("Pour commencer quel est votre acteur ? Attention à bien mettre les majuscules ! \n")
                print(acteur + " a une centralité de " + str(requetes.centralite(graphe, acteur)) + ": \n")
                time.sleep(3)
                entree = input("Nous avons fait le tour des informations pour la centralité de " + acteur + " ! \n Pour consulter les collaborateurs communs de deux acteurs tapez 1 ! \n Si vous voulez avoir des informations sur les collaborateurs proches d'un acteur tapez 2 ! \n Si vous voulez avoir des connaître la distance entre deux acteurs tapez 3 ! \n Peut-être voulez-vous connaître la centralité d'un autre acteur ? Si oui tapez 4 ! \n Si vous souhaitez l'acteur central d'Hollywood tapez 5 ! \n Pour connaître l'éloignement maximal de tout les acteurs tapez 6 ! \n Si vous voulez quitter le menu d'interaction tapez 7 ! \n")
        
        if entree == "5" :
            while entree == "5":
                acteur = None
                print ("Calcul de l'acteur central d'Hollywood en cours, cela peut être long... \n")
                print("L'acteur central d'Hollywood est " + requetes.centre_hollywood(graphe) + " ! Quelle personne incroyable ! \n")
                time.sleep(3)
                entree = input("Nous avons fait le tour pour l'acteur central d'Hollywood ! \n Pour consulter les collaborateurs communs de deux acteurs tapez 1 ! \n Si vous voulez avoir des informations sur les collaborateurs proches d'un acteur tapez 2 ! \n Si vous voulez avoir des connaître la distance entre deux acteurs tapez 3 ! \n Peut-être voulez-vous connaître la centralité d'un acteur ? Si oui tapez 4 ! \n Si vous souhaitez revoir l'acteur central d'Hollywood tapez 5 ! \n Pour connaître l'éloignement maximal de tout les acteurs tapez 6 ! \n Si vous voulez quitter le menu d'interaction tapez 7 ! \n")
        
        if entree == "6" :
            while entree == "6":
                acteur = None
                print ("Calcul de l'éloignement maximal en cours, cela peut être long... \n")
                print("L'éloignement maximal est de " + str(requetes.eloignement_max(graphe)) + " ! \n")
                time.sleep(3)
                entree = input("Nous avons fait le tour pour l'éloignement maximal ! \n Pour consulter les collaborateurs communs de deux acteurs tapez 1 ! \n Si vous voulez avoir des informations sur les collaborateurs proches d'un acteur tapez 2 ! \n Si vous voulez avoir des connaître la distance entre deux acteurs tapez 3 ! \n Peut-être voulez-vous connaître la centralité d'un acteur ? Si oui tapez 4 ! \n Si vous souhaitez l'acteur central d'Hollywood tapez 5 ! \n Pour connaître l'éloignement maximal de tout les acteurs à nouveau tapez 6 ! \n Si vous voulez quitter le menu d'interaction tapez 7 ! \n")
        
        if entree == "7" :
            print("Au plaisir de vous revoir, bonne journée !")
            return None
        
        while entree not in "12345" : # cette fonction tourne en boucle tant que l'utilisateur ne répond pas à la demande
            print("Je n'ai pas compris votre message, nous allons revenir au menu de consultation \n")
            time.sleep(3)
            entree = input("Si vous voulez connaître les collaborateurs communs de deux acteurs tapez 1 ! \n Si vous voulez avoir des informations sur les collaborateurs proches d'un acteur tapez 2 ! \n Si vous voulez avoir des connaître la distance entre deux acteurs tapez 3 ! \n Peut-être voulez-vous connaître la centralité d'un acteur ? Si oui tapez 4 ! \n Si vous souhaitez l'acteur central d'Hollywood tapez 5 ! \n Pour connaître l'éloignement maximal de tout les acteurs tapez 6 ! \n Si vous voulez quitter le menu d'interaction tapez 7 ! \n ")        

programme_principal()
