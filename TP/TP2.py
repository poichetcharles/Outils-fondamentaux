# ============================================================
# EXERCICE 1
# ============================================================

# 1.1 
def diviseurs(n):
    resultat = []
    for d in range(1, n + 1):
        if n % d == 0:
            resultat.append(d)
    return resultat

print("Diviseurs de 28 :", diviseurs(28))
print("Diviseurs de 97 :", diviseurs(97))

# correction
def diviseurs(n):
    """Liste croissante des diviseurs positifs de n."""
    resultat = []
    for d in range(1, n + 1):
        if n % d == 0:
            resultat.append(d)
    return resultat

print(diviseurs(28))
print(diviseurs(97))


# ============================================================
# EXERCICE 2 
# ============================================================

# 2.1 
def pgcd_naif(a, b):
    meilleur = 1
    plus_petit = a
    if b < a:
        plus_petit = b
        
    for d in range(1, plus_petit + 1):
        if a % d == 0 and b % d == 0:
            meilleur = d
    return meilleur

def pgcd(a, b):
    while b != 0:
        reste = a % b
        a = b
        b = reste
    return a

print("PGCD naïf :", pgcd_naif(1071, 462))
print("PGCD Euclide :", pgcd(1071, 462))

# correction
def pgcd_naif(a, b):
    """PGCD par essai de tous les diviseurs possibles."""
    meilleur = 1
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            meilleur = d
    return meilleur

def pgcd(a, b):
    """PGCD par l'algorithme d'Euclide."""
    while b != 0:
        a, b = b, a % b
    return a

print(pgcd_naif(1071, 462), pgcd(1071, 462))


# ============================================================
# EXERCICE 3 
# ============================================================

# 3.1
import time

def est_premier_naif(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def est_premier(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

def duree(fonction, argument):
    debut = time.perf_counter()
    fonction(argument)
    fin = time.perf_counter()
    return fin - debut

nombres_a_tester = [10007, 100003, 1000003]
for n in nombres_a_tester:
    t_naif = duree(est_premier_naif, n)
    t_racine = duree(est_premier, n)
    print("Pour", n, "- Naïf :", round(t_naif, 5), "s | Racine :", round(t_racine, 6), "s")

# correction
import time

def est_premier_naif(n):
    """Teste la primalité en essayant tous les diviseurs jusqu'à n - 1."""
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def est_premier(n):
    """Teste la primalité en s'arrêtant à la racine carrée de n."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True

def duree(fonction, argument):
    """Renvoie le temps d'exécution de fonction(argument), en secondes."""
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter() - debut

for n in (10_007, 100_003, 1_000_003):
    t_naif = duree(est_premier_naif, n)
    t_rac = duree(est_premier, n)
    print(f"{n:>9} : naif {t_naif:.5f} s | racine {t_rac:.6f} s")


# ============================================================
# EXERCICE 4
# ============================================================

# 4.1 
def crible(limite):
    est_premier_tab = [True] * (limite + 1)
    est_premier_tab[0] = False
    if limite >= 1:
        est_premier_tab[1] = False
        
    d = 2
    while d * d <= limite:
        if est_premier_tab[d] == True:
            for multiple in range(d * d, limite + 1, d):
                est_premier_tab[multiple] = False
        d = d + 1
        
    premiers = []
    for n in range(limite + 1):
        if est_premier_tab[n] == True:
            premiers.append(n)
    return premiers

debut = time.perf_counter()
p = crible(100000)
t_crible = time.perf_counter() - debut

debut = time.perf_counter()
combien = 0
for n in range(100001):
    if est_premier(n):
        combien = combien + 1
t_un_par_un = time.perf_counter() - debut

print("Total crible :", len(p), "en", round(t_crible, 4), "s")
print("Total classique :", combien, "en", round(t_un_par_un, 4), "s")

# correction
def crible(limite):
    """Renvoie la liste des nombres premiers de 2 à limite inclus."""
    est_premier_tab = [True] * (limite + 1)
    est_premier_tab[0] = False
    if limite >= 1:
        est_premier_tab[1] = False
    d = 2
    while d * d <= limite:
        if est_premier_tab[d]:
            for multiple in range(d * d, limite + 1, d):
                est_premier_tab[multiple] = False
        d = d + 1
    return [n for n in range(limite + 1) if est_premier_tab[n]]

debut = time.perf_counter()
p = crible(100_000)
t_crible = time.perf_counter() - debut

debut = time.perf_counter()
combien = sum(1 for n in range(100_001) if est_premier(n))
t_un_par_un = time.perf_counter() - debut

print(len(p), combien)
print(f"crible {t_crible:.4f} s | un par un {t_un_par_un:.4f} s")


# ============================================================
# EXERCICE 5
# ============================================================

# 5.1 
def facteurs(n):
    resultat = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n = n // d
        d = d + 1
        
    if n > 1:
        resultat.append(n)
    return resultat

f = facteurs(360)
print("Facteurs de 360 :", f)

produit = 1
for x in f:
    produit = produit * x
print("Vérification produit :", produit)

# correction
def facteurs(n):
    """Facteurs premiers de n, avec multiplicité, dans l'ordre croissant."""
    resultat = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        resultat.append(n)
    return resultat

f = facteurs(360)
print(f)

produit = 1
for x in f:
    produit = produit * x
print(produit)


# ============================================================
# EXERCICE 6
# ============================================================

# 6.1 
def fibonacci_recursif(n):
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

appels = {}
def fibonacci_compte(n):
    if n in appels:
        appels[n] = appels[n] + 1
    else:
        appels[n] = 1
        
    if n < 2:
        return n
    return fibonacci_compte(n - 1) + fibonacci_compte(n - 2)

for n in (20, 25, 30):
    t_fibo = duree(fibonacci_recursif, n)
    print("Temps pour F(", n, ") :", round(t_fibo, 4), "s")

resultat = fibonacci_compte(30)
print("F(30) =", resultat)
print("Appels à F(1) :", appels[1])

# 6.2
def fibonacci(n):
    precedent = 0
    courant = 1
    for i in range(n):
        nouveau = precedent + courant
        precedent = courant
        courant = nouveau
    return precedent

print("Temps pour F(30) optimisé :", round(duree(fibonacci, 30), 6), "s")
grand = fibonacci(10000)
print("Chiffres de F(10000) :", len(str(grand)))

# correction
def fibonacci_recursif(n):
    """F(n) en suivant la définition, par récurrence."""
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

for n in (20, 25, 30):
    print(f"F({n}) : {duree(fibonacci_recursif, n):.4f} s")

appels = {}

def fibonacci_compte(n):
    appels[n] = appels.get(n, 0) + 1
    if n < 2:
        return n
    return fibonacci_compte(n - 1) + fibonacci_compte(n - 2)

resultat = fibonacci_compte(30)
print("F(30) =", resultat)
print("appels a F(1) :", appels[1])
print("appels en tout :", sum(appels.values()))

def fibonacci(n):
    """F(n) par une boucle : deux variables suffisent."""
    precedent, courant = 0, 1
    for _ in range(n):
        precedent, courant = courant, precedent + courant
    return precedent

print(all(fibonacci(n) == fibonacci_recursif(n) for n in range(26)))
print(f"F(30) en {duree(fibonacci, 30):.6f} s")
grand = fibonacci(10_000)
print(len(str(grand)), "chiffres")


# ============================================================
# EXERCICE 7
# ============================================================

# 7.1 
def euclide_etendu(a, b):
    if b == 0:
        return a, 1, 0
    
    g, u, v = euclide_etendu(b, a % b)
    nouvel_u = v
    nouveau_v = u - (a // b) * v
    return g, nouvel_u, nouveau_v

g, u, v = euclide_etendu(1071, 462)
print("PGCD :", g, "| u :", u, "| v :", v)
print("Vérification :", 1071 * u + 462 * v == g)

def puissance_mod_naive(a, e, n):
    resultat = 1
    for i in range(e):
        resultat = (resultat * a) % n
    return resultat

def puissance_mod(a, e, n):
    resultat = 1
    a = a % n
    while e > 0:
        if e % 2 == 1:
            resultat = (resultat * a) % n
        a = (a * a) % n
        e = e // 2
    return resultat

# correction
def euclide_etendu(a, b):
    """Renvoie (g, u, v) avec g = pgcd(a, b) et a u + b v = g."""
    if b == 0:
        return a, 1, 0
    g, u, v = euclide_etendu(b, a % b)
    return g, v, u - (a // b) * v

g, u, v = euclide_etendu(1071, 462)
print(g, u, v, 1071 * u + 462 * v == g)

def puissance_mod_naive(a, e, n):
    """a^e mod n, par e multiplications successives."""
    resultat = 1
    for _ in range(e):
        resultat = resultat * a % n
    return resultat

def puissance_mod(a, e, n):
    """a^e mod n, par élévations au carré successives."""
    resultat = 1
    a = a % n
    while e > 0:
        if e % 2 == 1:
            resultat = resultat * a % n
        a = a * a % n
        e = e // 2
    return resultat

a, e, n = 7, 10 ** 7, 1_000_003
print(puissance_mod(a, e, n), pow(a, e, n))

debut = time.perf_counter()
puissance_mod_naive(a, e, n)
t_naive = time.perf_counter() - debut

debut = time.perf_counter()
puissance_mod(a, e, n)
t_rapide = time.perf_counter() - debut

print(f"naive {t_naive:.3f} s | rapide {t_rapide:.6f} s")
