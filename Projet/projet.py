import time
import random
import matplotlib.pyplot as plt

# ============================================================
# ARITHMÉTIQUE AVANCÉE ET CHIFFREMENT RSA
# ============================================================

def euclide_etendu(coefficient_a, coefficient_b):
    """Calcule le PGCD de a et b, ainsi que les coefficients de Bezout (u, v)."""
    if coefficient_a == 0:
        return coefficient_b, 0, 1
        
    pgcd, coefficient_u1, coefficient_v1 = euclide_etendu(coefficient_b % coefficient_a, coefficient_a)
    coefficient_u = coefficient_v1 - (coefficient_b // coefficient_a) * coefficient_u1
    coefficient_v = coefficient_u1
    
    return pgcd, coefficient_u, coefficient_v

def inverse_modulaire(exposant_e, indicatrice_phi):
    """Calcule l'inverse de e modulo phi pour générer la clé privée."""
    pgcd, coefficient_u, coefficient_v = euclide_etendu(exposant_e, indicatrice_phi)
    
    if pgcd != 1:
        raise ValueError("L'inverse modulaire n'existe pas (e et phi non premiers entre eux).")
        
    return coefficient_u % indicatrice_phi

def exponentiation_rapide(base, exposant, modulo):
    """Calcule (base^exposant) % modulo très rapidement en O(log(exposant))."""
    resultat = 1
    base_courante = base % modulo
    exposant_restant = exposant
    
    while exposant_restant > 0:
        if exposant_restant % 2 == 1:
            resultat = (resultat * base_courante) % modulo
        exposant_restant = exposant_restant // 2
        base_courante = (base_courante * base_courante) % modulo
        
    return resultat

def generer_cles(nombre_premier_p, nombre_premier_q):
    """Construit la clé publique (n, e) et la clé privée (n, d)."""
    module_n = nombre_premier_p * nombre_premier_q
    indicatrice_phi = (nombre_premier_p - 1) * (nombre_premier_q - 1)
    
    # Recherche d'un exposant public e premier avec phi
    exposant_e = 3
    while euclide_etendu(exposant_e, indicatrice_phi)[0] != 1:
        exposant_e += 2
        
    exposant_d = inverse_modulaire(exposant_e, indicatrice_phi)
    
    return (module_n, exposant_e), (module_n, exposant_d)

# ============================================================
# GÉNÉRATION DE NOMBRES PREMIERS
# ============================================================

def est_premier(nombre):
    """Test de primalité basique (déterministe)."""
    if nombre < 2:
        return False
    if nombre == 2:
        return True
    if nombre % 2 == 0:
        return False
        
    diviseur = 3
    while diviseur * diviseur <= nombre:
        if nombre % diviseur == 0:
            return False
        diviseur += 2
        
    return True

def generer_premier(taille_en_bits):
    """Génère un nombre premier aléatoire de la taille demandée en bits."""
    borne_minimale = 2 ** (taille_en_bits - 1)
    borne_maximale = (2 ** taille_en_bits) - 1
    
    while True:
        candidat = random.randint(borne_minimale, borne_maximale)
        if est_premier(candidat):
            return candidat

# ============================================================
# ATTAQUE PAR FACTORISATION
# ============================================================

def attaque_factorisation(module_n, duree_maximale):
    """
    Tente de retrouver les facteurs de n par force brute.
    S'arrête si le temps 'duree_maximale' est dépassé pour éviter de bloquer la machine.
    """
    temps_debut = time.time()
    nombre_tests = 0

    if module_n % 2 == 0:
        return 2, module_n // 2, time.time() - temps_debut, 1, False

    diviseur = 3
    limite_recherche = int(module_n ** 0.5) + 1

    while diviseur < limite_recherche:
        nombre_tests += 1
        
        # Vérification du timeout toutes les 1000 itérations pour ne pas ralentir la boucle
        if nombre_tests % 1000 == 0:
            temps_ecoule = time.time() - temps_debut
            if temps_ecoule >= duree_maximale:
                return None, None, temps_ecoule, nombre_tests, True

        if module_n % diviseur == 0:
            temps_ecoule = time.time() - temps_debut
            return diviseur, module_n // diviseur, temps_ecoule, nombre_tests, False

        diviseur += 2

    temps_ecoule = time.time() - temps_debut
    
    return None, None, temps_ecoule, nombre_tests, False

# ============================================================
# EXPÉRIMENTATION ET VISUALISATION
# ============================================================

def afficher_graphique(liste_resultats):
    """Trace la courbe exponentielle des temps de cassage avec matplotlib."""
    tailles_cles = []
    temps_moyens = []

    for resultat in liste_resultats:
        if resultat["temps_moyen"] is not None:
            tailles_cles.append(resultat["taille_cle"])
            temps_moyens.append(resultat["temps_moyen"])

    plt.figure(figsize=(9, 5))
    plt.plot(tailles_cles, temps_moyens, marker="o", color="red", linestyle="-")
    plt.title("Temps moyen de factorisation d'une clé RSA")
    plt.xlabel("Taille de la clé publique (n) en bits")
    plt.ylabel("Temps moyen (secondes)")
    plt.yscale("log")  # Indispensable pour bien voir l'évolution exponentielle
    plt.grid(True)
    plt.show()

def lancer_experiences():
    """
    Génère des clés de différentes tailles, lance l'attaque et compile les résultats.
    """
    tailles_premiers_bits = [8, 10, 12, 14, 16, 18, 20, 22, 24]
    nombre_essais_par_taille = 3
    duree_maximale_attaque = 3.0  # Limité à 3 secondes d'effort par attaque
    
    resultats_global = []
    print("\n--- DÉBUT DES TESTS (Essais par taille: " + str(nombre_essais_par_taille) + " | Timeout: " + str(duree_maximale_attaque) + "s) ---")

    for bits in tailles_premiers_bits:
        temps_reussites = []
        taille_cle = 0
        print("\n[ n généré à partir de nombres premiers de " + str(bits) + " bits ]")

        for numero_essai in range(1, nombre_essais_par_taille + 1):
            nombre_p = generer_premier(bits)
            nombre_q = generer_premier(bits)
            while nombre_q == nombre_p:
                nombre_q = generer_premier(bits)

            module_n = nombre_p * nombre_q
            taille_cle = module_n.bit_length()

            # Lancement du casseur
            facteur_p, facteur_q, temps_mesure, tests_effectues, limite_atteinte = attaque_factorisation(module_n, duree_maximale_attaque)

            if facteur_p is not None:
                temps_reussites.append(temps_mesure)
                print("  Essai " + str(numero_essai) + " : RÉUSSI en " + str(round(temps_mesure, 4)) + "s (" + str(tests_effectues) + " itérations)")
            else:
                if limite_atteinte:
                    print("  Essai " + str(numero_essai) + " : ABANDON (Temps de " + str(round(temps_mesure, 2)) + "s dépassé)")
                else:
                    print("  Essai " + str(numero_essai) + " : ÉCHEC (Facteurs introuvables)")

        # Calcul et affichage de la moyenne pour cette taille de clé
        if temps_reussites:
            temps_moyen = sum(temps_reussites) / len(temps_reussites)
            print("Temps MOYEN pour les clés de " + str(taille_cle) + " bits : " + str(round(temps_moyen, 4)) + " secondes")
        else:
            temps_moyen = None
            print("ÉCHEC total pour les clés de " + str(taille_cle) + " bits (aucune moyenne calculable)")
        
        resultats_global.append({
            "taille_cle": taille_cle,
            "temps_moyen": temps_moyen
        })

    afficher_graphique(resultats_global)

# ============================================================
# DÉMARRAGE DU SCRIPT
# ============================================================

if __name__ == "__main__":
    # Test unitaire pour valider l'aller-retour du chiffrement RSA
    p_test, q_test = 61, 53
    (module_n, exposant_e), (module_n, exposant_d) = generer_cles(p_test, q_test)
    
    # Génération d'un message clair aléatoire entre 2 et n-1
    message_clair = random.randint(2, module_n - 1)
    
    message_chiffre = exponentiation_rapide(message_clair, exposant_e, module_n)
    message_dechiffre = exponentiation_rapide(message_chiffre, exposant_d, module_n)
    
    print("--- TEST UNITAIRE CHIFFREMENT ---")
    print("Clair: " + str(message_clair) + " -> Chiffré: " + str(message_chiffre) + " -> Déchiffré: " + str(message_dechiffre))
    assert message_clair == message_dechiffre, "Erreur dans les fonctions arithmétiques !"
    
    # Lancement du benchmark global
    lancer_experiences()