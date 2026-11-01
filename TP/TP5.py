# ============================================================
# EXERCICE 1
# ============================================================

# 1.1 Les deux conversions
def lettre_vers_nombre(c):
    return ord(c) - ord("A")

def nombre_vers_lettre(n):
    # Le modulo 26 permet de toujours retomber sur une lettre valide
    return chr((n % 26) + ord("A"))

print("La lettre C donne :", lettre_vers_nombre("C"))
print("Le nombre 2 donne :", nombre_vers_lettre(2))

# 1.2 Nettoyer un texte
import unicodedata

def nettoyer(texte):
    # Enlève les accents
    sans_accent = unicodedata.normalize("NFD", texte)
    texte_propre = ""
    
    # On parcourt chaque caractère
    for c in sans_accent:
        # Si ce n'est pas un accent (catégorie Mn)
        if unicodedata.category(c) != "Mn":
            c_majuscule = c.upper()
            # On ne garde que les lettres de A à Z
            if "A" <= c_majuscule <= "Z":
                texte_propre = texte_propre + c_majuscule
                
    return texte_propre

print("Texte nettoyé :", nettoyer("Été, à Paris !"))

# correction
def lettre_vers_nombre(c):
    """Numéro de 0 à 25 d'une lettre majuscule."""
    return ord(c) - ord("A")

def nombre_vers_lettre(n):
    """Lettre majuscule correspondant à un numéro de 0 à 25."""
    return chr(n % 26 + ord("A"))

print(lettre_vers_nombre("C"), nombre_vers_lettre(2))
print([nombre_vers_lettre(lettre_vers_nombre(c)) == c for c in "ABCXYZ"])

import unicodedata

def nettoyer(texte):
    """Majuscules sans accents, lettres A-Z uniquement."""
    sans_accent = unicodedata.normalize("NFD", texte)
    sans_accent = "".join(c for c in sans_accent if unicodedata.category(c) != "Mn")
    return "".join(c for c in sans_accent.upper() if "A" <= c <= "Z")

print(nettoyer("Été, à Paris !"))


# ============================================================
# EXERCICE 2
# ============================================================

# 2.1 La fonction de chiffrement
def chiffrer(texte, a, b):
    texte_propre = nettoyer(texte)
    resultat = ""
    
    for c in texte_propre:
        x = lettre_vers_nombre(c)
        nouveau_x = (a * x + b) % 26
        resultat = resultat + nombre_vers_lettre(nouveau_x)
        
    return resultat

message = "ATTAQUEALAUBE"
print("Chiffrement affine :", chiffrer(message, 5, 8))
print("Chiffrement César :", chiffrer(message, 1, 3))

# correction
def chiffrer(texte, a, b):
    """Chiffrement affine de texte avec la clé (a, b)."""
    resultat = []
    for c in nettoyer(texte):
        x = lettre_vers_nombre(c)
        resultat.append(nombre_vers_lettre((a * x + b) % 26))
    return "".join(resultat)

message = "ATTAQUEALAUBE"
print(chiffrer(message, 5, 8))
print(chiffrer(message, 1, 3))   # le chiffre de César


# ============================================================
# EXERCICE 3
# ============================================================

# 3.1 Les clés utilisables
def pgcd(a, b):
    while b != 0:
        reste = a % b
        a = b
        b = reste
    return a

valides = []
for a in range(1, 26):
    if pgcd(a, 26) == 1:
        valides.append(a)

print("Valeurs valides pour a :", valides)
print("Nombre de valeurs :", len(valides))

# 3.2 L'inverse modulaire
def inverse_modulaire(a, n):
    a = a % n
    for candidat in range(1, n):
        if (a * candidat) % n == 1:
            return candidat
            
    # Si on ne trouve rien, on affiche une erreur
    raise ValueError(str(a) + " n'est pas inversible modulo " + str(n))

print("Inverse de 5 modulo 26 :", inverse_modulaire(5, 26))

try:
    inverse_modulaire(4, 26)
except ValueError as erreur:
    print("Erreur attendue :", erreur)

# correction
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

valides = [a for a in range(1, 26) if pgcd(a, 26) == 1]
print(valides)
print(len(valides), "valeurs possibles pour a")

def inverse_modulaire(a, n):
    """Inverse de a modulo n, par recherche exhaustive."""
    a = a % n
    for candidat in range(1, n):
        if (a * candidat) % n == 1:
            return candidat
    raise ValueError(f"{a} n'est pas inversible modulo {n}")

print(inverse_modulaire(5, 26))
print((5 * 21) % 26)

try:
    inverse_modulaire(4, 26)
except ValueError as erreur:
    print("erreur attendue :", erreur)


# ============================================================
# EXERCICE 4
# ============================================================

# 4.1 La fonction de déchiffrement
def dechiffrer(texte, a, b):
    a_inverse = inverse_modulaire(a, 26)
    resultat = ""
    
    for c in nettoyer(texte):
        y = lettre_vers_nombre(c)
        ancien_x = (a_inverse * (y - b)) % 26
        resultat = resultat + nombre_vers_lettre(ancien_x)
        
    return resultat

message = nettoyer("Attaque a l aube")
secret = chiffrer(message, 5, 8)
print("Message secret :", secret)
print("Déchiffré :", dechiffrer(secret, 5, 8))
print("Identique à l'original ?", dechiffrer(secret, 5, 8) == message)

try:
    dechiffrer(secret, 4, 7)
except ValueError as erreur:
    print("Clé refusée :", erreur)

# correction
def dechiffrer(texte, a, b):
    """Déchiffrement affine. Lève une erreur si la clé n'est pas inversible."""
    a_inverse = inverse_modulaire(a, 26)
    resultat = []
    for c in nettoyer(texte):
        y = lettre_vers_nombre(c)
        resultat.append(nombre_vers_lettre(a_inverse * (y - b) % 26))
    return "".join(resultat)

message = nettoyer("Attaque a l aube")
secret = chiffrer(message, 5, 8)
print(secret)
print(dechiffrer(secret, 5, 8))
print(dechiffrer(secret, 5, 8) == message)

try:
    dechiffrer(secret, 4, 7)
except ValueError as erreur:
    print("cle refusee :", erreur)


# ============================================================
# EXERCICE 5
# ============================================================

# 5.1 Casser par force brute
def toutes_les_clefs(secret):
    resultats = []
    for a in valides:
        for b in range(26):
            texte_clair = dechiffrer(secret, a, b)
            resultats.append((a, b, texte_clair))
    return resultats

essais = toutes_les_clefs(secret)
print("Nombre de clés essayées :", len(essais))

# Recherche du bon message parmi les essais
for a, b, texte in essais:
    if texte == message:
        print("La bonne clé est : a =", a, ", b =", b)

# correction
def toutes_les_clefs(secret):
    """Tous les déchiffrements possibles, sous forme de triplets (a, b, texte)."""
    resultats = []
    for a in valides:
        for b in range(26):
            resultats.append((a, b, dechiffrer(secret, a, b)))
    return resultats

essais = toutes_les_clefs(secret)
print(len(essais), "clefs essayees")
bons = [e for e in essais if e[2] == message]
print("la bonne clef :", bons[0][0], bons[0][1])


# ============================================================
# EXERCICE 6
# ============================================================

# 6.1 Casser par analyse de fréquences
texte_long = nettoyer(
    "Le chiffrement affine est un chiffrement par substitution monoalphabetique. "
    "Chaque lettre du message est remplacee par une autre lettre, toujours la meme, "
    "ce qui laisse intactes les frequences relatives des lettres et permet de casser "
    "le code sans essayer toutes les clefs possibles."
)
secret_long = chiffrer(texte_long, 7, 12)

# Comptage manuel (niveau NSI)
frequences = {}
for lettre in secret_long:
    if lettre in frequences:
        frequences[lettre] = frequences[lettre] + 1
    else:
        frequences[lettre] = 1

# Recherche de la lettre qui apparaît le plus
lettre_frequente = ""
max_occurences = 0
for lettre in frequences:
    if frequences[lettre] > max_occurences:
        max_occurences = frequences[lettre]
        lettre_frequente = lettre

print("Lettre la plus fréquente du chiffre :", lettre_frequente)

cible = lettre_vers_nombre(lettre_frequente)
candidats = []

for a in valides:
    # Si E (valeur 4) donne 'cible', alors : cible = 4 * a + b
    # Donc b = cible - 4 * a
    b = (cible - 4 * a) % 26
    candidats.append((a, b, dechiffrer(secret_long, a, b)))

print("Nombre de candidats :", len(candidats))
for a, b, texte in candidats:
    # On regarde si ça commence par LECHIFFREMENT
    if texte[0:13] == "LECHIFFREMENT":
        print("Trouvé ! Clé : a =", a, ", b =", b)
        print("Début du texte :", texte[0:60])

# correction
from collections import Counter

comptes = Counter(secret_long)
lettre_frequente = comptes.most_common(1)[0][0]
print("lettre la plus frequente du chiffre :", lettre_frequente)

cible = lettre_vers_nombre(lettre_frequente)
candidats = []
for a in valides:
    b = (cible - 4 * a) % 26
    candidats.append((a, b, dechiffrer(secret_long, a, b)))

print(len(candidats), "candidats au lieu de 312")
for a, b, texte in candidats:
    if texte.startswith("LECHIFFREMENT"):
        print("trouve :", a, b)
        print(texte[:60])


# ============================================================
# EXERCICE 7
# ============================================================

# 7.1 L'indice de coïncidence
import random

def indice_coincidence(texte):
    N = len(texte)
    if N <= 1:
        return 0
        
    frequences = {}
    for c in texte:
        if c in frequences:
            frequences[c] = frequences[c] + 1
        else:
            frequences[c] = 1
            
    somme = 0
    for c in frequences:
        n = frequences[c]
        somme = somme + n * (n - 1)
        
    return somme / (N * (N - 1))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hasard = ""
for i in range(len(texte_long)):
    hasard = hasard + random.choice(alphabet)

print("IC du texte clair :", round(indice_coincidence(texte_long), 4))
print("IC du chiffre affine :", round(indice_coincidence(secret_long), 4))
print("IC du texte au hasard :", round(indice_coincidence(hasard), 4))

# correction
import random

def indice_coincidence(texte):
    """Probabilité que deux lettres tirées au hasard dans le texte coïncident."""
    N = len(texte)
    comptes = Counter(texte)
    return sum(n * (n - 1) for n in comptes.values()) / (N * (N - 1))

random.seed(1)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hasard = "".join(random.choice(alphabet) for _ in range(len(texte_long)))

print(f"clair    : {indice_coincidence(texte_long):.4f}")
print(f"affine   : {indice_coincidence(secret_long):.4f}")
print(f"hasard   : {indice_coincidence(hasard):.4f}")


# ============================================================
# EXERCICE 8
# ============================================================

# 8.1 Chiffrer par Vigenère
def vigenere(texte, cle):
    texte_propre = nettoyer(texte)
    cle_propre = nettoyer(cle)
    resultat = ""
    longueur_cle = len(cle_propre)
    
    for i in range(len(texte_propre)):
        c = texte_propre[i]
        # On répète la clé grâce au modulo
        lettre_cle = cle_propre[i % longueur_cle]
        
        decalage = lettre_vers_nombre(lettre_cle)
        valeur_c = lettre_vers_nombre(c)
        
        nouvelle_lettre = nombre_vers_lettre((valeur_c + decalage) % 26)
        resultat = resultat + nouvelle_lettre
        
    return resultat

secret_vigenere = vigenere(texte_long, "CLE")
print("Début du secret Vigenère :", secret_vigenere[0:40])
print("IC Vigenère :", round(indice_coincidence(secret_vigenere), 4))

# correction
def vigenere(texte, cle):
    """Chiffre de Vigenère : chaque lettre est décalée par la lettre de la clé en face."""
    resultat = []
    for i, c in enumerate(nettoyer(texte)):
        decalage = lettre_vers_nombre(cle[i % len(cle)])
        resultat.append(nombre_vers_lettre(lettre_vers_nombre(c) + decalage))
    return "".join(resultat)

secret_vigenere = vigenere(texte_long, "CLE")
print(secret_vigenere[:40])
print(f"IC vigenere : {indice_coincidence(secret_vigenere):.4f}")

# 8.2 Retrouver la longueur de la clé
for L in range(1, 8):
    somme_ic = 0
    # On découpe le texte en L colonnes
    for i in range(L):
        colonne = ""
        # On prend une lettre sur L
        for j in range(i, len(secret_vigenere), L):
            colonne = colonne + secret_vigenere[j]
        somme_ic = somme_ic + indice_coincidence(colonne)
        
    moyenne = somme_ic / L
    print("Longueur =", L, "-> indice moyen :", round(moyenne, 4))

# correction
for L in range(1, 8):
    colonnes = [secret_vigenere[i::L] for i in range(L)]
    moyenne = sum(indice_coincidence(col) for col in colonnes) / L
    print(f"L = {L} : indice moyen {moyenne:.4f}")