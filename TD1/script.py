## Exercice 1:

# ======== Variables (globales)

tirage = ["a","n","t","i","g","r","p","u"]
path = "frenchssaccent.dic"

# On peut utiliser un dictionnaire pour repésenter les points de chaque lettre
points_lettres ={'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
                 'd': 2, 'g': 2, 'm': 2,
                 'b': 3, 'c': 3, 'p': 3,
                 'f': 4, 'h': 4, 'v': 4,
                 'j': 8, 'q': 8,
                 'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}

points_lettres_avec_joker ={'?':0,
                 'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
                 'd': 2, 'g': 2, 'm': 2,
                 'b': 3, 'c': 3, 'p': 3,
                 'f': 4, 'h': 4, 'v': 4,
                 'j': 8, 'q': 8,
                 'k': 10, 'w': 10, 'x': 10, 'y': 10, 'z': 10}


# ======== Fonctions

# charger les données dans mots_possibles depuis frenchssacent.dic
def read_file(path):
    # charge les données de path dans une liste et retourne la liste
    output = list()
    file = open(path,'r')
    for line in file:
        mot = line[0:len(line)-1]
        if len(mot) <=8:
            output.append(mot) # éliminer les mots de taille >= 8
        # output.append(line[0:len(line)-1])
        # output.append(line.replace("\n",""))
    file.close()        
    return output


def isMotPossible(tirage,mot):
    copie_du_tirage = list(tirage)
    for lettre in mot:
        if lettre in copie_du_tirage:
            copie_du_tirage.remove(lettre)
        else:
            return False
    return True

def motlepluslong(liste_mots_possibles):
#je compare le premier mot aux autres et je garde en mémoire le dernier
    mot_choisi=liste_mots_possibles[0]   
    for mot in liste_mots_possibles[1:]: 
        if len(mot_choisi) < len(mot):
            mot_choisi= mot
    return mot_choisi

def score(mot):
#je parcours chaque lettre du mot et j'additionne les points qu'elles valent à l'aide du dictionnaire
    points=0
    for lettre in mot:
        points+=points_lettres[lettre]
    return points

def max_score(mots_possibles):
#je compare les scores et je garde le plus grand avec le mot gagnant
    max_points=score(mots_possibles[0])
    max_mot=mots_possibles[0]
    for mot in mots_possibles:
        if max_points<score(mot):
            max_points=score(mot)
            max_mot=mot
    return (max_mot,max_points)

def isMotPossible_avec_joker(tirage, mot):
    copie_du_tirage =list(tirage)
    #à supposer qu'on a un seul joker:
    copie_du_tirage.remove('?')
    for lettre in points_lettres:# je regarde maintenant si pour chaque tirage possible le mot peut être écrit
        nouveau_tirage=copie_du_tirage+[lettre] 
        if isMotPossible(nouveau_tirage,mot):
            return True
    return False


# ======== Script / Main

# charger les données dans mots_possibles depuis frenchssacent.dic
mots_possibles = read_file(path)

# parcourir les mots et garder ceux que l'on peut écrire
liste_mots_possibles = [mot for mot in mots_possibles if isMotPossible(tirage, mot)]

#parmi ceux là, trouver le mot le plus long
motfinal = motlepluslong(liste_mots_possibles)

#parmi les mots disponibles, on prend celui qui rapporte le plus de point
mot_final=max_score(liste_mots_possibles)[0]

# avec le joker:
liste_mots_possibles_avec_joker=[mot for mot in mots_possibles if isMotPossible_avec_joker(tirage, mot)]
mot_final_avec_joker=max_score(liste_mots_possibles_avec_joker)[0]
