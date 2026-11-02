
import time
import random
import matplotlib.pyplot as plt


# ============================================================
# FONCTIONS RSA
# ============================================================

def est_premier(n):
    liste_diviseurs=[1]
    for i in range(2,n+1):
        if n%i==0: liste_diviseurs.append(i)
        if len(liste_diviseurs)>2: return False
    return True


def diviseurs_premiers(n):
    liste_diviseurs_premiers=[]
    for i in range(2,n+1):
        if n%i==0 and est_premier(i):
            liste_diviseurs_premiers.append(i)
    return liste_diviseurs_premiers


def recherche_pq(n):
    L=diviseurs_premiers(n)
    for nombre1 in L:
        for nombre2 in L:
            if nombre1*nombre2==n :
                return (nombre1,nombre2)
    return -1


def recherche_d(c,p,q):
    d=1
    while (c*d)%((p-1)*(q-1))!=1:
        d+=1
    return d


# ============================================================
# 2. FONCTIONS COMPLEMENTAIRES
# ============================================================

def pgcd(a, b):
    """Calcule le PGCD de deux nombres."""
    while b != 0:
        a, b = b, a % b
    return a


def exponentiation_rapide(base, exposant, modulo):
    """Calcule rapidement base puissance exposant modulo modulo."""
    resultat = 1
    base = base % modulo

    while exposant > 0:
        if exposant % 2 == 1:
            resultat = (resultat * base) % modulo

        exposant = exposant // 2
        base = (base * base) % modulo

    return resultat


def generer_premier(taille_bits):
    """Génère un nombre premier de la taille demandée."""
    minimum = 2 ** (taille_bits - 1)
    maximum = 2 ** taille_bits - 1

    while True:
        nombre = random.randint(minimum, maximum)

        if est_premier(nombre):
            return nombre


# ============================================================
# 3. GENERATION DES CLES RSA
# ============================================================

def generer_cles(taille_bits):

    p = generer_premier(taille_bits)
    q = generer_premier(taille_bits)

    while q == p:
        q = generer_premier(taille_bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Recherche d'un exposant public valide
    e = 3

    while pgcd(e, phi) != 1:
        e += 2

    # Calcul de la clé privée
    d = recherche_d(e, p, q)

    return p, q, n, e, d


# ============================================================
# CHIFFREMENT ET DECHIFFREMENT
# ============================================================

def chiffrer(message, e, n):
    return exponentiation_rapide(message, e, n)


def dechiffrer(chiffre, d, n):
    return exponentiation_rapide(chiffre, d, n)


# ============================================================
# 5. SIMULATION DE LA TELEMETRIE F1
# ============================================================

def simulation_f1():

    print("\n==========================================")
    print("      TELEMETRIE FORMULE 1 - RSA")
    print("==========================================")

    # Exemple de donnée envoyée par la voiture
    vitesse = 327

    # Création d'une petite clé RSA
    p, q, n, e, d = generer_cles(9)

    print("\n--- GENERATION DES CLES ---")
    print("Nombre premier p :", p)
    print("Nombre premier q :", q)
    print("Module n :", n)
    print("Cle publique :", (e, n))
    print("Cle privee :", (d, n))

    if vitesse >= n:
        print("Erreur : la valeur de télémétrie dépasse le module RSA.")
        return

    # Chiffrement de la vitesse
    message_chiffre = chiffrer(vitesse, e, n)

    # Déchiffrement à la réception
    message_dechiffre = dechiffrer(message_chiffre, d, n)

    print("\n--- TRANSMISSION DES DONNEES ---")
    print("Vitesse originale :", vitesse, "km/h")
    print("Donnee chiffree :", message_chiffre)
    print("Donnee dechiffree :", message_dechiffre, "km/h")

    if message_dechiffre == vitesse:
        print("Transmission securisee : dechiffrement reussi.")


# ============================================================
# RSA
# ============================================================

def attaque_rsa(n, e):

    debut = time.perf_counter()

    # Recherche des deux facteurs premiers
    resultats = recherche_pq(n)

    if resultats == -1:
        return None, None, time.perf_counter() - debut

    p_trouve, q_trouve = resultats

    # Reconstruction de la clé privée
    d_trouve = recherche_d(e, p_trouve, q_trouve)

    temps = time.perf_counter() - debut

    return p_trouve, q_trouve, temps


# ============================================================
# ETUDE DES TAILLES DE CLES
# ============================================================

def etude_securite():

    # Taille en bits de chacun des deux nombres premiers
    tailles = [8, 9, 10, 11]

    tailles_cles = []
    temps_attaques = []

    print("\n==========================================")
    print("       ETUDE DE LA SECURITE RSA")
    print("==========================================")

    for bits in tailles:

        # Génération des clés
        p, q, n, e, d = generer_cles(bits)

        taille_reelle = n.bit_length()

        # Mesure de l'attaque
        p_trouve, q_trouve, temps = attaque_rsa(n, e)

        tailles_cles.append(taille_reelle)
        temps_attaques.append(temps)

        # Vérification de la clé retrouvée
        succes = False

        if p_trouve is not None:
            d_trouve = recherche_d(e, p_trouve, q_trouve)

            message_test = 327 % n
            chiffre = chiffrer(message_test, e, n)
            resultat = dechiffrer(chiffre, d_trouve, n)

            succes = resultat == message_test

        print("\nTaille des nombres premiers :", bits, "bits")
        print("Taille de la clé publique :", taille_reelle, "bits")
        print("Temps de factorisation :", round(temps, 6), "secondes")
        print("Clé privée retrouvée :", "Oui" if succes else "Non")

    # ========================================================
    # GRAPHIQUE
    # ========================================================

    plt.figure(figsize=(10, 6))

    plt.plot(
        tailles_cles,
        temps_attaques,
        marker="o",
        linewidth=2,
        label="Temps de cassage par factorisation"
    )

    plt.title("Formule 1 : résistance du chiffrement RSA")
    plt.xlabel("Taille du module RSA (bits)")
    plt.ylabel("Temps de cassage (secondes)")

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    plt.savefig("resultats_rsa_f1.png", dpi=150)
    plt.show()


# ============================================================
# Appel de fonction
# ============================================================

if __name__ == "__main__":

    simulation_f1()

    etude_securite()


