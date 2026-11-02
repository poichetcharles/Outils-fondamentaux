# ============================================================
# EXERCICE 1
# ============================================================

def evaluer_naif(P, x):
    """Évalue le polynôme P au point x, terme par terme."""
    total = 0
    for i in range(len(P)):
        total = total + P[i] * (x ** i)
    return total

print("Test naïf en x=2 :", evaluer_naif([2, 3, 0, 5], 2))
print("Test naïf en x=25 :", evaluer_naif([2, 5, 7], 25))

# correction
def evaluer_naif(P, x):
    """Évalue le polynôme P au point x, terme par terme."""
    total = 0
    for i in range(len(P)):
        total = total + P[i] * x ** i
    return total

print(evaluer_naif([2, 3, 0, 5], 2))
print(evaluer_naif([2, 3, 0, 5], 0))


# ============================================================
# EXERCICE 2
# ============================================================

# 2.1
def evaluer(P, x):
    """Évalue le polynôme P au point x par le schéma de Horner."""
    total = 0
    for coefficient in reversed(P):
        total = total * x + coefficient
    return total

P = [2, 3, 0, 5]
for x in (-2, 0, 1, 2, 10):
    print("x =", x, "| Naïf :", evaluer_naif(P, x), "| Horner :", evaluer(P, x))

# correction
def evaluer(P, x):
    """Évalue le polynôme P au point x par le schéma de Horner."""
    total = 0
    for coefficient in reversed(P):
        total = total * x + coefficient
    return total

P = [2, 3, 0, 5]
for x in (-2, 0, 1, 2, 10):
    print(x, evaluer_naif(P, x), evaluer(P, x))


# 2.2
import time

for degre in (1000, 5000, 20000):
    P = [1] * (degre + 1)
    
    debut = time.perf_counter()
    a = evaluer_naif(P, 1.0001)
    t_naif = time.perf_counter() - debut
    
    debut = time.perf_counter()
    b = evaluer(P, 1.0001)
    t_horner = time.perf_counter() - debut
    
    rapport = t_naif / t_horner
    ecart = abs(a - b)
    print("Degré", degre, "| Rapport Naïf/Horner :", round(rapport, 1), "| Écart :", ecart)

# correction
import time

for degre in (1000, 5000, 20000):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 1.0001)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer(P, 1.0001)
    t_horner = time.perf_counter() - debut

    print(f"degre {degre:>6} : naif {t_naif:.5f} s | horner {t_horner:.5f} s "
          f"| rapport {t_naif / t_horner:.1f} | ecart des valeurs {abs(a - b):.2e}")


# 2.3
for degre in (200, 400, 800):
    P = [1] * (degre + 1)
    
    debut = time.perf_counter()
    a = evaluer_naif(P, 3)
    t_naif = time.perf_counter() - debut
    
    debut = time.perf_counter()
    b = evaluer(P, 3)
    t_horner = time.perf_counter() - debut
    
    rapport = t_naif / t_horner
    print("Degré", degre, "| Rapport entiers :", round(rapport, 1), "| Égaux ?", a == b)

# correction
for degre in (200, 400, 800):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 3)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer(P, 3)
    t_horner = time.perf_counter() - debut

    print(f"degre {degre:>4} : rapport {t_naif / t_horner:.1f} | resultats egaux : {a == b}")


# ============================================================
# EXERCICE 3
# ============================================================

def deriver(P):
    """Coefficients du polynôme dérivé de P."""
    derivee = []
    for i in range(1, len(P)):
        derivee.append(i * P[i])
    return derivee

print("Dérivée de [2, 3, 0, 5] :", deriver([2, 3, 0, 5]))
print("Dérivée d'une constante [7] :", deriver([7]))

# correction
def deriver(P):
    """Coefficients du polynôme dérivé de P."""
    return [i * P[i] for i in range(1, len(P))]

print(deriver([2, 3, 0, 5]))
print(deriver([7]))


# ============================================================
# EXERCICE 4
# ============================================================

# 4.1

def dichotomie(f, a, b, tolerance=1e-12):
    """Racine de f dans [a, b], par bissection."""
    fa = f(a)
    fb = f(b)
    
    if fa == 0: 
        return a
    if fb == 0: 
        return b
    if fa * fb > 0:
        print("Erreur : f(a) et f(b) doivent être de signes opposés.")
        return None
        
    while (b - a) > tolerance:
        milieu = (a + b) / 2
        if f(a) * f(milieu) <= 0:
            b = milieu
        else:
            a = milieu
    return (a + b) / 2

def carre_moins_deux(x):
    return x * x - 2

racine = dichotomie(carre_moins_deux, 0, 2, 1e-9)
print("Racine de x^2 - 2 (Dichotomie) :", racine)

# correction
def dichotomie(f, a, b, tolerance=1e-12):
    """Racine de f dans [a, b], par bissection. Exige f(a) et f(b) de signes opposés."""
    fa, fb = f(a), f(b)
    if fa == 0:
        return a
    if fb == 0:
        return b
    if fa * fb > 0:
        raise ValueError("f(a) et f(b) doivent etre de signes opposes")
    while b - a > tolerance:
        milieu = (a + b) / 2
        if f(a) * f(milieu) <= 0:
            b = milieu
        else:
            a = milieu
    return (a + b) / 2

def carre_moins_deux(x):
    return x * x - 2

racine = dichotomie(carre_moins_deux, 0, 2)
print(racine)
print(abs(racine - 2 ** 0.5) < 1e-9)


# 4.2
def newton(P, depart, tolerance=1e-12, tours_max=100):
    derivee = deriver(P)
    x = float(depart)
    
    for tour in range(tours_max):
        valeur = evaluer(P, x)
        pente = evaluer(derivee, x)
        
        if pente == 0:
            print("Erreur : Tangente horizontale.")
            return None, tour
            
        suivant = x - (valeur / pente)
        ecart = abs(suivant - x)
        
        if ecart <= tolerance * max(1.0, abs(suivant)):
            return suivant, tour + 1
            
        x = suivant
        
    print("Erreur : Pas de convergence.")
    return None, tours_max

Q = [-5, -2, 0, 1]
racine_newton, tours = newton(Q, 2)
print("Racine (Newton, départ 2) :", racine_newton, "en", tours, "tours")

# correction
def newton(P, depart, tolerance=1e-12, tours_max=100):
    """Racine du polynôme P par la méthode de Newton, à partir de depart."""
    derivee = deriver(P)
    x = float(depart)
    for tour in range(tours_max):
        valeur = evaluer(P, x)
        pente = evaluer(derivee, x)
        if pente == 0:
            raise ZeroDivisionError("tangente horizontale, Newton ne peut pas continuer")
        suivant = x - valeur / pente
        if abs(suivant - x) <= tolerance * max(1.0, abs(suivant)):
            return suivant, tour + 1
        x = suivant
    raise RuntimeError("pas de convergence en {} tours".format(tours_max))

Q = [-5, -2, 0, 1]
racine, tours = newton(Q, 2)
print(racine, "en", tours, "tours")
print(abs(evaluer(Q, racine)) < 1e-10)


# 4.3
def newton_trace(P, depart, tours):
    derivee = deriver(P)
    x = float(depart)
    trajet = [x]
    
    for i in range(tours):
        pente = evaluer(derivee, x)
        if pente == 0: 
            break
        x = x - (evaluer(P, x) / pente)
        trajet.append(x)
        
    return trajet

R = [2, -2, 0, 1]
print("Trajet de x^3 - 2x + 2 :", newton_trace(R, 0, 8))

# correction
def newton_trace(P, depart, tours):
    """Renvoie la liste des premiers itérés de Newton, sans test d'arrêt."""
    derivee = deriver(P)
    x = float(depart)
    trajet = [x]
    for _ in range(tours):
        pente = evaluer(derivee, x)
        if pente == 0:
            break
        x = x - evaluer(P, x) / pente
        trajet.append(x)
    return trajet

R = [2, -2, 0, 1]
print(newton_trace(R, 0, 8))

try:
    print(newton(R, 0))
except RuntimeError as erreur:
    print("echec :", erreur)


# 4.4
print("\nTest des départs pour x^3 - 2x - 5 :")
for depart in (2, 1, 0):
    rac, nb_tours = newton(Q, depart)
    print("Départ", depart, "-> Racine :", rac, "(en", nb_tours, "tours)")

# correction
Q = [-5, -2, 0, 1]
for depart in (2, 1, 0):
    racine, tours = newton(Q, depart)
    print(f"depart {depart:>2} : {tours:>2} tours, racine {racine:.9f}")


# ============================================================
# EXERCICE 5
# ============================================================

import matplotlib.pyplot as plt

Q = [-5, -2, 0, 1]
xs = [i / 100 for i in range(-300, 301)]
ys = [evaluer(Q, x) for x in xs]

plt.figure()
plt.plot(xs, ys, label="x^3 - 2x - 5")
plt.axhline(0, linewidth=0.8, color='black')
plt.axvline(0, linewidth=0.8, color='black')
plt.ylim(-20, 20)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.title("Un polynome et son unique racine reelle")
# plt.show()


# ============================================================
# EXERCICE 6
# ============================================================

# 6.1

def somme(P, Q):
    longueur = max(len(P), len(Q))
    P_complet = P + [0] * (longueur - len(P))
    Q_complet = Q + [0] * (longueur - len(Q))
    
    resultat = []
    for i in range(longueur):
        resultat.append(P_complet[i] + Q_complet[i])
    return resultat

def produit_poly(P, Q):
    if len(P) == 0 or len(Q) == 0:
        return []
        
    res = [0] * (len(P) + len(Q) - 1)
    for i in range(len(P)):
        for j in range(len(Q)):
            res[i + j] = res[i + j] + P[i] * Q[j]
    return res

print("\nSomme [1, 2] et [0, 0, 3] :", somme([1, 2], [0, 0, 3]))
print("Produit [1, 1] et [1, 1] :", produit_poly([1, 1], [1, 1]))
print("Produit [-1, 1] et [1, 1] :", produit_poly([-1, 1], [1, 1]))

# correction
def somme(P, Q):
    """Somme de deux polynômes donnés par leurs coefficients."""
    longueur = max(len(P), len(Q))
    P = P + [0] * (longueur - len(P))
    Q = Q + [0] * (longueur - len(Q))
    return [P[i] + Q[i] for i in range(longueur)]

def produit_poly(P, Q):
    """Produit de deux polynômes donnés par leurs coefficients."""
    if not P or not Q:
        return []
    R = [0] * (len(P) + len(Q) - 1)
    for i in range(len(P)):
        for j in range(len(Q)):
            R[i + j] = R[i + j] + P[i] * Q[j]
    return R

print(somme([1, 2], [0, 0, 3]))
print(produit_poly([1, 1], [1, 1]))
print(produit_poly([-1, 1], [1, 1]))


# 6.2 
l = [1]
for i in range(10):
    l = produit_poly(l, [1, 1])
print("Ligne 10 de Pascal :", l)
print("Somme de la liste :", sum(l), "| Attendu :", 2 ** 10)

# correction
binome = [1]
for _ in range(10):
    binome = produit_poly(binome, [1, 1])
print(binome)
print(sum(binome), 2 ** 10)


# ============================================================
# EXERCICE 7
# ============================================================

import math

def derivee_avant(f, x, h):
    return (f(x + h) - f(x)) / h

def derivee_centree(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

exacte = math.cos(1.0)
print("\nErreur de dérivée pour sin(1.0) :")
for h in (1e-1, 1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12):
    e_avant = abs(derivee_avant(math.sin, 1.0, h) - exacte)
    e_centree = abs(derivee_centree(math.sin, 1.0, h) - exacte)
    print(f"h = {h:.0e} : avant {e_avant:.1e} | centrée {e_centree:.1e}")

# correction
import math

def derivee_avant(f, x, h):
    return (f(x + h) - f(x)) / h

def derivee_centree(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

exacte = math.cos(1.0)
for h in (1e-1, 1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12):
    e_avant = abs(derivee_avant(math.sin, 1.0, h) - exacte)
    e_centree = abs(derivee_centree(math.sin, 1.0, h) - exacte)
    print(f"h = {h:.0e} : avant {e_avant:.1e} | centree {e_centree:.1e}")


# ============================================================
# EXERCICE 8
# ============================================================

# 8.1

def rectangles(f, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(n):
        total = total + f(a + i * h)
    return h * total

def trapezes(f, a, b, n):
    h = (b - a) / n
    interieur = 0
    for i in range(1, n):
        interieur = interieur + f(a + i * h)
    return h * ((f(a) + f(b)) / 2 + interieur)

def simpson(f, a, b, n):
    if n % 2 == 1:
        n = n + 1
    h = (b - a) / n
    
    impairs = 0
    for i in range(1, n, 2):
        impairs = impairs + f(a + i * h)
        
    pairs = 0
    for i in range(2, n, 2):
        pairs = pairs + f(a + i * h)
        
    return (h / 3) * (f(a) + f(b) + 4 * impairs + 2 * pairs)

def carre(x):
    return x * x

print("\nErreur intégration x^2 entre 0 et 1 (Exact = 1/3) :")
for n in (10, 100, 1000):
    e_rect = abs(rectangles(carre, 0, 1, n) - (1 / 3))
    e_trap = abs(trapezes(carre, 0, 1, n) - (1 / 3))
    e_simp = abs(simpson(carre, 0, 1, n) - (1 / 3))
    print(f"n = {n:>4} : rectangles {e_rect:.1e} | trapezes {e_trap:.1e} | simpson {e_simp:.1e}")

# correction
def rectangles(f, a, b, n):
    """Intégrale de f sur [a, b] par n rectangles à gauche."""
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))

def trapezes(f, a, b, n):
    """Intégrale de f sur [a, b] par n trapèzes."""
    h = (b - a) / n
    interieur = sum(f(a + i * h) for i in range(1, n))
    return h * ((f(a) + f(b)) / 2 + interieur)

def simpson(f, a, b, n):
    """Intégrale de f sur [a, b] par la méthode de Simpson, n pair."""
    if n % 2 == 1:
        n = n + 1
    h = (b - a) / n
    impairs = sum(f(a + i * h) for i in range(1, n, 2))
    pairs = sum(f(a + i * h) for i in range(2, n, 2))
    return h / 3 * (f(a) + f(b) + 4 * impairs + 2 * pairs)

def carre(x):
    return x * x

for n in (10, 100, 1000):
    e_rect = abs(rectangles(carre, 0, 1, n) - 1 / 3)
    e_trap = abs(trapezes(carre, 0, 1, n) - 1 / 3)
    e_simp = abs(simpson(carre, 0, 1, n) - 1 / 3)
    print(f"n = {n:>4} : rectangles {e_rect:.1e} | trapezes {e_trap:.1e} | simpson {e_simp:.1e}")


# 8.2
def arctangente_derivee(x):
    return 4 / (1 + x * x)

approx_trap = trapezes(arctangente_derivee, 0, 1, 1000)
approx_simp = simpson(arctangente_derivee, 0, 1, 1000)

print("\nCalcul de Pi :")
print("Trapèzes :", approx_trap, "| Erreur :", abs(approx_trap - math.pi))
print("Simpson  :", approx_simp, "| Erreur :", abs(approx_simp - math.pi))

# correction
def arctangente_derivee(x):
    return 4 / (1 + x * x)

approx_trap = trapezes(arctangente_derivee, 0, 1, 1000)
approx_simp = simpson(arctangente_derivee, 0, 1, 1000)
print(approx_trap, abs(approx_trap - math.pi))
print(approx_simp, abs(approx_simp - math.pi))
