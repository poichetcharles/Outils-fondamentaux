import time
import random
import matplotlib.pyplot as plt

# ============================================================
# TÉLÉMÉTRIE F1 & CRYPTOGRAPHIE RSA (SÉCURITÉ DES STANDS)
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
    """Calcule l'inverse de e modulo phi pour générer la clé privée de l'écurie."""
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

def generer_cles_ecurie(premier_p, premier_q):
    """Construit la clé publique de la monoplace (n, e) et la clé privée du stand (n, d)."""
    module_chiffrement_n = premier_p * premier_q
    indicatrice_phi = (premier_p - 1) * (premier_q - 1)
    
    # Recherche d'un exposant public e premier avec phi
    exposant_e = 3
    while euclide_etendu(exposant_e, indicatrice_phi)[0] != 1:
        exposant_e += 2
        
    exposant_d = inverse_modulaire(exposant_e, indicatrice_phi)
    
    return (module_chiffrement_n, exposant_e), (module_chiffrement_n, exposant_d)

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
# ATTAQUE PAR ESPIONNAGE INDUSTRIEL (FORCE BRUTE)
# ============================================================

def attaque_espionnage_telemetrie(module_chiffrement_n, duree_maximale):
    """
    Tente d'intercepter et de casser le module 'n' par force brute 
    pour décoder les données de la monoplace avant la fin du temps imparti.
    """
    temps_debut = time.time()
    nombre_tests = 0

    if module_chiffrement_n % 2 == 0:
        return 2, module_chiffrement_n // 2, time.time() - temps_debut, 1, False

    diviseur = 3
    limite_recherche = int(module_chiffrement_n ** 0.5) + 1

    while diviseur < limite_recherche:
        nombre_tests += 1
        
        # Vérification du timeout toutes les 1000 itérations pour éviter le crash du stand
        if nombre_tests % 1000 == 0:
            temps_ecoule = time.time() - temps_debut
            if temps_ecoule >= duree_maximale:
                return None, None, temps_ecoule, nombre_tests, True

        if module_chiffrement_n % diviseur == 0:
            temps_ecoule = time.time() - temps_debut
            return diviseur, module_chiffrement_n // diviseur, temps_ecoule, nombre_tests, False

        diviseur += 2

    temps_ecoule = time.time() - temps_debut
    
    return None, None, temps_ecoule, nombre_tests, False

# ============================================================
# EXPÉRIMENTATION ET VISUALISATION DES PERFORMANCES
# ============================================================

def afficher_graphique_securite(liste_resultats):
    """Trace la courbe de vulnérabilité de la télémétrie F1 en fonction de la taille de clé."""
    tailles_cles = []
    temps_moyens = []

    for resultat in liste_resultats:
        if resultat["temps_moyen"] is not None:
            tailles_cles.append(resultat["taille_cle"])
            temps_moyens.append(resultat["temps_moyen"])

    plt.figure(figsize=(9, 5))
    plt.plot(tailles_cles, temps_moyens, marker="s", color="darkred", linestyle="-", linewidth=2)
    plt.title("Vulnérabilité de la télémétrie F1 face à l'espionnage (Temps de cassage)")
    plt.xlabel("Taille de la clé publique de la monoplace (n) en bits")
    plt.ylabel("Temps moyen d'interception (secondes)")
    plt.yscale("log")  # Échelle logarithmique pour montrer l'explosion exponentielle
    plt.grid(True)
    plt.show()

def lancer_simulation_f1():
    """
    Simule l'interception de clés de chiffrement F1 de plus en plus robustes
    par une écurie concurrente.
    """
    tailles_premiers_bits = [8, 10, 12, 14, 16, 18, 20, 22, 24]
    nombre_essais_par_taille = 3
    duree_maximale_attaque = 3.0  # Limite de temps d'analyse par l'adversaire
    
    resultats_global = []
    print("\n--- SIMULATION PADDOCK F1 : SÉCURISATION DES DONNÉES DE LA MONOPLACE ---")

    for bits in tailles_premiers_bits:
        temps_reussites = []
        taille_cle = 0
        print("\n[ Clé générée avec des nombres premiers de " + str(bits) + " bits ]")

        for numero_essai in range(1, nombre_essais_par_taille + 1):
            nombre_p = generer_premier(bits)
            nombre_q = generer_premier(bits)
            while nombre_q == nombre_p:
                nombre_q = generer_premier(bits)

            module_chiffrement_n = nombre_p * nombre_q
            taille_cle = module_chiffrement_n.bit_length()

            # Lancement de l'attaque par l'écurie rivale
            facteur_p, facteur_q, temps_mesure, tests_effectues, limite_atteinte = attaque_espionnage_telemetrie(module_chiffrement_n, duree_maximale_attaque)

            if facteur_p is not None:
                temps_reussites.append(temps_mesure)
                print("  Essai " + str(numero_essai) + " : Interception RÉUSSIE en " + str(round(temps_mesure, 4)) + "s (" + str(tests_effectues) + " calculs)")
            else:
                if limite_atteinte:
                    print("  Essai " + str(numero_essai) + " : Échec de l'espionnage (Temps limite de " + str(round(temps_mesure, 2)) + "s dépassé, donnee sécurisée)")
                else:
                    print("  Essai " + str(numero_essai) + " : ÉCHEC total")

        # Calcul et affichage de la moyenne pour cette taille de clé
        if temps_reussites:
            temps_moyen = sum(temps_reussites) / len(temps_reussites)
            print("Temps MOYEN d'interception pour les clés de " + str(taille_cle) + " bits : " + str(round(temps_moyen, 4)) + " secondes")
        else:
            temps_moyen = None
            print("SÉCURITÉ TOTALE pour les clés de " + str(taille_cle) + " bits (インviolables dans le temps imparti)")
        
        resultats_global.append({
            "taille_cle": taille_cle,
            "temps_moyen": temps_moyen
        })

    afficher_graphique_securite(resultats_global)

# ============================================================
# DÉMARRAGE DU SCRIPT
# ============================================================

if __name__ == "__main__":
    # Test unitaire : Chiffrement d'une donnée de télémétrie (ex: température moteur en °C)
    p_test, q_test = 61, 53
    (module_chiffrement_n, exposant_e), (module_chiffrement_n, exposant_d) = generer_cles_ecurie(p_test, q_test)
    
    # Simulation d'une valeur de télémétrie à transmettre de la voiture au stand
    donnee_telemetrie_ claire = 95  # Ex: 95°C de température d'huile
    
    donnee_chiffree = exponentiation_rapide(donnee_telemetrie_ claire, exposant_e, module_chiffrement_n)
    donnee_dechiffree = exponentiation_rapide(donnee_chiffree, exposant_d, module_chiffrement_n)
    
    print("--- TEST UNITAIRE TÉLÉMÉTRIE F1 ---")
    print("Donnée brute (stand): " + str(donnee_telemetrie_ claire) + " -> Transmise chiffrée: " + str(donnee_chiffree) + " -> Déodée au stand: " + str(donnee_dechiffree))
    assert donnee_telemetrie_ claire == donnee_dechiffree, "Erreur de transmission radio !"
    
    # Lancement du benchmark global de sécurité
    lancer_simulation_f1()
