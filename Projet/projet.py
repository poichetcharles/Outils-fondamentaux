import time
import random
import matplotlib.pyplot as plt

# ============================================================
# 1. FONCTIONS RSA (Mathématiques)
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

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def exponentiation_rapide(base, exposant, modulo):
    resultat = 1
    base = base % modulo
    while exposant > 0:
        if exposant % 2 == 1:
            resultat = (resultat * base) % modulo
        exposant = exposant // 2
        base = (base * base) % modulo
    return resultat

def generer_premier(taille_bits):
    minimum = 2 ** (taille_bits - 1)
    maximum = 2 ** taille_bits - 1
    while True:
        nombre = random.randint(minimum, maximum)
        if est_premier(nombre):
            return nombre

# ============================================================
# 2. GENERATION DES CLES RSA ET CHIFFREMENT
# ============================================================

def generer_cles(taille_bits):
    p = generer_premier(taille_bits)
    q = generer_premier(taille_bits)
    while q == p:
        q = generer_premier(taille_bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while pgcd(e, phi) != 1:
        e += 2
    d = recherche_d(e, p, q)
    return p, q, n, e, d

def chiffrer(message, e, n):
    return exponentiation_rapide(message, e, n)

def dechiffrer(chiffre, d, n):
    return exponentiation_rapide(chiffre, d, n)

# ============================================================
# 3. FONCTIONS VERNAM (Masque Jetable)
# ============================================================

def generateur_cle():
    cle=""
    # Génère 8000 bits (assez pour un message de 1000 caractères)
    for i in range(8000):
        cle += str( random.randint(0,1) )
    sauvegarde_dans_fichier("cle.txt", cle)

def sauvegarde_dans_fichier(nom_du_fichier, contenu):
    fichier_sauv = open(nom_du_fichier, "w")
    fichier_sauv.write(contenu)
    fichier_sauv.close()

def charger_le_contenu_du_fichier(nom_de_fichier):
    le_fichier = open(nom_de_fichier, 'r')
    contenu = le_fichier.read()
    le_fichier.close()
    return contenu

def transformer_en_binaire(texte):
    chaine_binaire=""
    for caractere in str(texte):
        chaine_binaire += format(ord(caractere), '08b')
    return chaine_binaire

def transformer_en_caracteres(binaire):
    chaine=""
    for i in range(0, len(binaire), 8):
        chaine += chr( int(binaire[i:i+8], 2) )
    return chaine

def chiffrement_vernam():
    msg = charger_le_contenu_du_fichier("texte.txt")
    msg_bin = transformer_en_binaire(msg)
    cle = charger_le_contenu_du_fichier("cle.txt")
    msg_chiffre=""
    for i in range(len(msg_bin)):
        msg_chiffre += str( int(msg_bin[i]) ^ int(cle[i]) )
    sauvegarde_dans_fichier("texte_chiffre.txt", msg_chiffre)

def dechiffrement_vernam():
    msg_bin = charger_le_contenu_du_fichier("texte_chiffre.txt")
    cle = charger_le_contenu_du_fichier("cle.txt")
    msg_bin_dechiffre=""
    for i in range(len(msg_bin)):
        msg_bin_dechiffre += str( int(msg_bin[i]) ^ int(cle[i]) )
    msg_dechiffre = transformer_en_caracteres(msg_bin_dechiffre)
    return msg_dechiffre

# ============================================================
# 4. SIMULATIONS ET COMPARAISONS F1
# ============================================================

def attaque_rsa(n, e):
    debut = time.perf_counter()
    resultats = recherche_pq(n)
    if resultats == -1:
        return None, None, time.perf_counter() - debut
    p_trouve, q_trouve = resultats
    temps = time.perf_counter() - debut
    return p_trouve, q_trouve, temps

def comparaison_rsa_vernam():
    print("\n==========================================")
    print("   COMPARAISON DE VITESSE : RSA vs VERNAM")
    print("==========================================")
    
    # Donnée de télémétrie aléatoire
    vitesse = random.randint(100, 350)
    print("Vitesse à transmettre :", vitesse, "km/h")
    
    # --- TEST RSA ---
    debut_rsa = time.perf_counter()
    p, q, n, e, d = generer_cles(9)
    if vitesse < n:
        msg_c = chiffrer(vitesse, e, n)
        msg_d = dechiffrer(msg_c, d, n)
    temps_rsa = time.perf_counter() - debut_rsa
    print("\n[RSA] Temps total :", round(temps_rsa, 6), "sec")
    
    # --- TEST VERNAM ---
    sauvegarde_dans_fichier("texte.txt", str(vitesse))
    
    debut_vernam = time.perf_counter()
    generateur_cle()
    chiffrement_vernam()
    vitesse_retrouvee = dechiffrement_vernam()
    temps_vernam = time.perf_counter() - debut_vernam
    
    print("[VERNAM] Temps total :", round(temps_vernam, 6), "sec")
    
    if temps_vernam < temps_rsa:
        print("\n=> Vernam est", round(temps_rsa / temps_vernam, 1), "fois plus rapide que RSA !")

def etude_securite():
    tailles = [8, 9, 10, 11]
    tailles_cles = []
    temps_attaques = []

    print("\n==========================================")
    print("        ETUDE DE LA SECURITE RSA")
    print("==========================================")

    for bits in tailles:
        p, q, n, e, d = generer_cles(bits)
        taille_reelle = n.bit_length()
        p_trouve, q_trouve, temps = attaque_rsa(n, e)

        tailles_cles.append(taille_reelle)
        temps_attaques.append(temps)
        
        print("Taille clé publique :", taille_reelle, "bits | Temps de cassage :", round(temps, 6), "sec")

    print("\n==========================================")
    print("       ETUDE DE LA SECURITE VERNAM")
    print("==========================================")
    print("Taille clé secrète : 8000 bits | Temps de cassage : INFINI")
    print("(Une attaque par force brute est mathématiquement impossible)")

    print("\n==========================================")
    print("               CONCLUSION")
    print("==========================================")
    print("L'algorithme le plus sécurisé est VERNAM (masque jetable).")
    print("Le RSA est vulnérable si la taille de la clé est trop petite, un pirate")
    print("peut la casser en factorisant le module (comme prouvé par les temps ci-dessus).")
    print("Vernam offre une sécurité absolue, mais son défaut en Formule 1 est")
    print("logistique il nécessite une clé aléatoire aussi longue que les données envoyées.")

    # GRAPHIQUE
    plt.figure(figsize=(10, 6))
    plt.plot(tailles_cles, temps_attaques, marker="o", linewidth=2, label="Temps de cassage par factorisation")
    plt.title("Formule 1 : résistance du chiffrement RSA")
    plt.xlabel("Taille du module RSA (bits)")
    plt.ylabel("Temps de cassage (secondes)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("resultats_rsa_f1.png", dpi=150)
    plt.show()

# ============================================================
# Appel principal
# ============================================================
if __name__ == "__main__":
    comparaison_rsa_vernam()
    etude_securite()
