import math

# ============================================================
# EXERCICE 1
# ============================================================

# 1.1 La boîte à outils géométrique
def vecteur(A, B):
    return (B[0] - A[0], B[1] - A[1])

def produit_scalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]

def norme(u):
    return math.hypot(u[0], u[1])

def angle(u, v):
    # Calcul du cosinus avec précaution contre les arrondis
    cosinus = produit_scalaire(u, v) / (norme(u) * norme(v))
    if cosinus > 1.0:
        cosinus = 1.0
    elif cosinus < -1.0:
        cosinus = -1.0
    
    # Transformation du cosinus en angle (en degrés)
    return math.degrees(math.acos(cosinus))

print("Norme de (3,4) :", norme((3, 4)))
print("Produit scalaire :", produit_scalaire((1, 2), (3, 4)))
print("Angle 1 :", angle((1, 0), (1, 1)))
print("Angle 2 :", angle((1, 0), (0, 1)))
print("Angle 3 :", angle((2, 0), (2, 0)))

# correction
def vecteur(A, B):
    """Vecteur AB, de A vers B."""
    return (B[0] - A[0], B[1] - A[1])

def produit_scalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]

def norme(u):
    return math.hypot(u[0], u[1])

def angle(u, v):
    """Angle non orienté entre u et v, en degrés."""
    cosinus = produit_scalaire(u, v) / (norme(u) * norme(v))
    cosinus = max(-1.0, min(1.0, cosinus))
    return math.degrees(math.acos(cosinus))

print(norme((3, 4)), produit_scalaire((1, 2), (3, 4)))
print(angle((1, 0), (1, 1)), angle((1, 0), (0, 1)))
print(angle((2, 0), (2, 0)))

# 1.2 La distance d'un point à une droite
def determinant(u, v):
    return u[0] * v[1] - u[1] * v[0]

def distance_point_droite(P, A, B):
    AB = vecteur(A, B)
    AP = vecteur(A, P)
    aire = abs(determinant(AB, AP))
    base = norme(AB)
    return aire / base

distance_1 = distance_point_droite((0, 0), (0, 1), (1, 0))
valeur_attendue = math.sqrt(2) / 2
print("\nDistance 1 :", distance_1, "| Attendu :", valeur_attendue)

distance_2 = distance_point_droite((3, 4), (0, 0), (1, 0))
print("Distance 2 :", distance_2)

# correction
def determinant(u, v):
    """Déterminant de (u, v), aire orientée du parallélogramme qu'ils engendrent."""
    return u[0] * v[1] - u[1] * v[0]

def distance_point_droite(P, A, B):
    AB = vecteur(A, B)
    AP = vecteur(A, P)
    return abs(determinant(AB, AP)) / norme(AB)

print(distance_point_droite((0, 0), (0, 1), (1, 0)), math.sqrt(2) / 2)
print(distance_point_droite((3, 4), (0, 0), (1, 0)))


# ============================================================
# EXERCICE 2
# ============================================================

# 2.1 À gauche ou à droite ?
def orientation(A, B, C):
    AB = vecteur(A, B)
    AC = vecteur(A, C)
    det = determinant(AB, AC)
    
    if det > 0:
        return 1
    elif det < 0:
        return -1
    else:
        return 0

print("\nOrientation 1 :", orientation((0, 0), (1, 0), (1, 1)))
print("Orientation 2 :", orientation((0, 0), (1, 0), (1, -1)))
print("Orientation 3 :", orientation((0, 0), (1, 1), (2, 2)))

# correction
def orientation(A, B, C):
    """1 si A -> B -> C tourne à gauche, -1 à droite, 0 si alignés."""
    d = determinant(vecteur(A, B), vecteur(A, C))
    if d > 0:
        return 1
    if d < 0:
        return -1
    return 0

print(orientation((0, 0), (1, 0), (1, 1)))
print(orientation((0, 0), (1, 0), (1, -1)))
print(orientation((0, 0), (1, 1), (2, 2)))

# 2.2 L'aire d'un polygone
def aire(polygone):
    somme = 0
    n = len(polygone)
    for i in range(n):
        x1 = polygone[i][0]
        y1 = polygone[i][1]
        
        suivant = (i + 1) % n
        x2 = polygone[suivant][0]
        y2 = polygone[suivant][1]
        
        somme = somme + (x1 * y2 - x2 * y1)
        
    return abs(somme) / 2

carre = [(0, 0), (1, 0), (1, 1), (0, 1)]
triangle = [(0, 0), (4, 0), (0, 3)]
maison = [(0, 0), (2, 0), (2, 1.5), (1, 2.5), (0, 1.5)]

print("\nAire du carré :", aire(carre))
print("Aire du triangle :", aire(triangle))
print("Aire de la maison :", aire(maison))

# correction
def aire(polygone):
    """Aire d'un polygone simple donné par ses sommets dans l'ordre (formule du lacet)."""
    somme = 0
    n = len(polygone)
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        somme = somme + (x1 * y2 - x2 * y1)
    return abs(somme) / 2

carre = [(0, 0), (1, 0), (1, 1), (0, 1)]
triangle = [(0, 0), (4, 0), (0, 3)]
maison = [(0, 0), (2, 0), (2, 1.5), (1, 2.5), (0, 1.5)]
print(aire(carre), aire(triangle), aire(maison))


# ============================================================
# EXERCICE 3
# ============================================================

# 3.1 Le test de croisement
def se_coupent(A, B, C, D):
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)
    
    if (o1 * o2 < 0) and (o3 * o4 < 0):
        return True
    else:
        return False

print("\nCroisement 1 :", se_coupent((0, 0), (1, 1), (0, 1), (1, 0)))
print("Croisement 2 :", se_coupent((0, 0), (1, 0), (0, 1), (1, 1)))
print("Croisement 3 :", se_coupent((0, 0), (1, 1), (2, 2), (3, 3)))

# correction
def se_coupent(A, B, C, D):
    """Vrai si les segments [AB] et [CD] se croisent franchement.

    Les cas dégénérés (trois points alignés) renvoient False.
    """
    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)
    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)
    return o1 * o2 < 0 and o3 * o4 < 0

print(se_coupent((0, 0), (1, 1), (0, 1), (1, 0)))
print(se_coupent((0, 0), (1, 0), (0, 1), (1, 1)))
print(se_coupent((0, 0), (1, 1), (2, 2), (3, 3)))

# 3.2 Le point d'intersection
def intersection(A, B, C, D):
    AB = vecteur(A, B)
    CD = vecteur(C, D)
    denom = determinant(AB, CD)
    
    if denom == 0:
        return None
        
    AC = vecteur(A, C)
    t = determinant(AC, CD) / denom
    u = determinant(AC, AB) / denom
    
    if (0 <= t <= 1) and (0 <= u <= 1):
        point_x = A[0] + t * AB[0]
        point_y = A[1] + t * AB[1]
        return (point_x, point_y)
        
    return None

print("\nIntersection 1 :", intersection((0, 0), (2, 2), (0, 2), (2, 0)))
print("Intersection 2 :", intersection((0, 0), (1, 0), (0, 1), (1, 1)))
print("Intersection 3 :", intersection((0, 0), (1, 1), (2, 2), (3, 3)))

# correction
def intersection(A, B, C, D):
    """Point d'intersection des segments [AB] et [CD], ou None."""
    AB = vecteur(A, B)
    CD = vecteur(C, D)
    denominateur = determinant(AB, CD)
    if denominateur == 0:
        return None            # parallèles ou alignés
    AC = vecteur(A, C)
    t = determinant(AC, CD) / denominateur
    u = determinant(AC, AB) / denominateur
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (A[0] + t * AB[0], A[1] + t * AB[1])
    return None

print(intersection((0, 0), (2, 2), (0, 2), (2, 0)))
print(intersection((0, 0), (1, 0), (0, 1), (1, 1)))
print(intersection((0, 0), (1, 1), (2, 2), (3, 3)))


# ============================================================
# EXERCICE 4
# ============================================================

# 4.1 Le lancer de rayon
def dedans(P, polygone):
    x = P[0]
    y = P[1]
    n = len(polygone)
    interieur = False
    
    for i in range(n):
        x1 = polygone[i][0]
        y1 = polygone[i][1]
        suivant = (i + 1) % n
        x2 = polygone[suivant][0]
        y2 = polygone[suivant][1]
        
        # Test si le rayon traverse le segment en y
        if (y1 > y) != (y2 > y):
            x_croise = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            # Test si l'intersection est à droite du point
            if x < x_croise:
                if interieur == True:
                    interieur = False
                else:
                    interieur = True
                    
    return interieur

print("\nTests du lancer de rayon :")
points_test = [(1, 1), (1, 2.4), (3, 1), (0.2, 2.2)]
for P in points_test:
    print("Point", P, "-> Dedans :", dedans(P, maison))

# correction
def dedans(P, polygone):
    """Vrai si P est à l'intérieur du polygone, par lancer de rayon horizontal."""
    x, y = P
    n = len(polygone)
    interieur = False
    for i in range(n):
        x1, y1 = polygone[i]
        x2, y2 = polygone[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            x_croisement = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_croisement:
                interieur = not interieur
    return interieur

for P in ((1, 1), (1, 2.4), (3, 1), (0.2, 2.2)):
    print(P, dedans(P, maison))

# 4.2 L'aire par le hasard (Monte-Carlo)
import random
random.seed(0)

tirages = 200000
touches = 0

for i in range(tirages):
    rx = random.uniform(0, 2)
    ry = random.uniform(0, 2.5)
    P = (rx, ry)
    
    if dedans(P, maison) == True:
        touches = touches + 1

aire_rect = 2 * 2.5
aire_estimee = aire_rect * touches / tirages
print("\nAire estimée de la maison :", aire_estimee)

# correction
import random

random.seed(0)
tirages = 200_000
touches = 0
for _ in range(tirages):
    P = (random.uniform(0, 2), random.uniform(0, 2.5))
    if dedans(P, maison):
        touches = touches + 1

aire_rectangle = 2 * 2.5
print(aire_rectangle * touches / tirages)


# ============================================================
# EXERCICE 5
# ============================================================

import matplotlib.pyplot as plt

def tracer_polygone(polygone, points=[]):
    xs = []
    ys = []
    
    # On ajoute chaque point pour tracer le contour
    for s in polygone:
        xs.append(s[0])
        ys.append(s[1])
        
    # On referme le polygone en ajoutant le premier point à la fin
    xs.append(polygone[0][0])
    ys.append(polygone[0][1])
    
    plt.figure(figsize=(5, 5))
    plt.plot(xs, ys, color="black")
    
    for P in points:
        if dedans(P, polygone):
            couleur = "green"
        else:
            couleur = "red"
        plt.scatter([P[0]], [P[1]], color=couleur)
        
    plt.axis("equal")
    plt.title("Vert : dedans, rouge : dehors")
    plt.show()

# 5.1 Un polygone qui n'est pas convexe
etoile = []
for k in range(10):
    if k % 2 == 0:
        rayon = 2
    else:
        rayon = 0.8
        
    theta = math.pi / 2 + k * math.pi / 5
    px = rayon * math.cos(theta)
    py = rayon * math.sin(theta)
    etoile.append((px, py))

print("\nAire de l'étoile :", round(aire(etoile), 4))
print("Centre (0,0) dedans :", dedans((0, 0), etoile))
print("Pointe (0,1.5) dedans :", dedans((0, 1.5), etoile))
print("Creux (1.2,1.2) dedans :", dedans((1.2, 1.2), etoile))

# On décommente la ligne suivante pour voir le dessin
# tracer_polygone(etoile, [(0, 0), (0, 1.5), (1.2, 1.2), (0, 1.9)])

# correction
import matplotlib.pyplot as plt

def tracer_polygone(polygone, points=()):
    xs = [s[0] for s in polygone] + [polygone[0][0]]
    ys = [s[1] for s in polygone] + [polygone[0][1]]
    plt.figure(figsize=(5, 5))
    plt.plot(xs, ys, color="black")
    for P in points:
        couleur = "green" if dedans(P, polygone) else "red"
        plt.scatter([P[0]], [P[1]], color=couleur)
    plt.axis("equal")
    plt.title("Vert : dedans, rouge : dehors")
    plt.show()

random.seed(1)
nuage = [(random.uniform(-0.5, 2.5), random.uniform(-0.5, 3)) for _ in range(60)]
# tracer_polygone(maison, nuage)

etoile = []
for k in range(10):
    rayon = 2 if k % 2 == 0 else 0.8
    theta = math.pi / 2 + k * math.pi / 5
    etoile.append((rayon * math.cos(theta), rayon * math.sin(theta)))

print(round(aire(etoile), 4))
print(dedans((0, 0), etoile), dedans((0, 1.5), etoile), dedans((1.2, 1.2), etoile))
# tracer_polygone(etoile, [(0, 0), (0, 1.5), (1.2, 1.2), (0, 1.9)])


# ============================================================
# EXERCICE 6
# ============================================================

# 6.1 Le polygone le plus proche
def zone_de(P, zones):
    for indice in range(len(zones)):
        zone = zones[indice]
        if dedans(P, zone) == True:
            return indice
    return None

liste_zones = [maison, [(3, 0), (4, 0), (4, 1), (3, 1)]]
print("\nTest des zones :")
print("Point (1,1)     -> Zone :", zone_de((1, 1), liste_zones))
print("Point (3.5,0.5) -> Zone :", zone_de((3.5, 0.5), liste_zones))
print("Point (2.5,0.5) -> Zone :", zone_de((2.5, 0.5), liste_zones))

# correction
def zone_de(P, zones):
    """Indice de la première zone qui contient P, ou None."""
    for indice, zone in enumerate(zones):
        if dedans(P, zone):
            return indice
    return None

zones = [maison, [(3, 0), (4, 0), (4, 1), (3, 1)]]
for P in ((1, 1), (3.5, 0.5), (2.5, 0.5)):
    print(P, zone_de(P, zones))