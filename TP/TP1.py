# ============================================================
# EXERCICE 1
# ============================================================

# 1.1
n = 2026
d = 7
quotient = n // d
reste = n % d

print("Quotient :", quotient)
print("Reste :", reste)
print("Vérification :", quotient * d + reste == n)

# correction
n = 2026
d = 7
quotient = n // d
reste = n % d
print(quotient, reste)
print(quotient * d + reste == n)

# 1.2
nombre = 123456789
unites = nombre % 10
decale = nombre // 10

print("Dernier chiffre :", unites)
print("Nombre décalé :", decale)

# correction
n = 123456789
print(n % 10)
print(n // 10)

# ============================================================
# EXERCICE 2
# ============================================================

# 2.1 L'erreur de la machine
total = 0.0
for i in range(1000):
    total = total + 0.1

print("Résultat :", total)
print("Erreur :", total - 100)

# correction
total = 0.0
for _ in range(1000):
    total = total + 0.1
print(total)
print(total - 100)

# 2.2 Comparer deux flottants
def presque_egaux(a, b, tolerance=1e-9):
    ecart = abs(a - b)
    if ecart <= tolerance:
        return True
    else:
        return False
    
# correction
def presque_egaux(a, b, tolerance=1e-9):
    """Dit si a et b sont égaux à la tolérance près."""
    return abs(a - b) <= tolerance

print(presque_egaux(0.1 + 0.2, 0.3))
print(presque_egaux(1.0, 1.5))

# ============================================================
# EXERCICE 3
# ============================================================
n = 17

if n % 2 == 0:
    print("pair")
else:
    print("impair")

for i in range(1, 6):
    print(i, i * i)
    
n = 1
while n * n < 1000:
    n = n + 1
print(n)

# 3.1
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

# correction
for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)
    
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# 3.2 
n = 100
total_boucle = 0
for i in range(1, n + 1):
    total_boucle = total_boucle + i

print("Somme avec la boucle :", total_boucle)

# correction

n = 100
total = 0
for i in range(1, n + 1):
    total = total + i
print(total)
print(n * (n + 1) // 2)

# ============================================================
# EXERCICE 4
# ============================================================

def celsius_vers_fahrenheit(c):
    """Convertit une température de degrés Celsius en degrés Fahrenheit."""
    return c * 9 / 5 + 32

print(celsius_vers_fahrenheit(100))
print(celsius_vers_fahrenheit(-40))

def nombre_de_chiffres(n):
    compte = 1
    while n >= 10:
        n = n // 10
        compte = compte + 1
    return compte

print("Chiffres de 2026 :", nombre_de_chiffres(2026))

# correction

def nombre_de_chiffres(n):
    """Renvoie le nombre de chiffres de l'entier positif n."""
    compte = 1
    while n >= 10:
        n = n // 10
        compte = compte + 1
    return compte

print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))
print(nombre_de_chiffres(10 ** 60))

# ============================================================
# EXERCICE 5
# ============================================================

def heron(a):
    if a < 0:
        print("Erreur : nombre négatif")
        return -1
    if a == 0:
        return 0.0
        
    x = float(a)
    tolerance = 1e-12
    
    while True:
        suivant = 0.5 * (x + a / x)
        ecart = abs(suivant - x)
        
        if ecart <= tolerance * abs(suivant):
            return suivant
            
        x = suivant

print("Racine de 2 avec Héron :", heron(2))

# correction

import math

def heron(a, tolerance=1e-12):
    """Racine carrée de a par la méthode de Héron."""
    if a < 0:
        raise ValueError("pas de racine carrée réelle pour un nombre négatif")
    if a == 0:
        return 0.0
    x = float(a)
    tours = 0
    while True:
        suivant = 0.5 * (x + a / x)
        tours = tours + 1
        if abs(suivant - x) <= tolerance * abs(suivant):
            return suivant
        x = suivant

print(heron(2))
print(math.sqrt(2))
print(abs(heron(2) - math.sqrt(2)) < 1e-12)

# ============================================================
# EXERCICE 6
# ============================================================

print(bin(37))
print(int("100101", 2))

from fractions import Fraction

print(Fraction(0.1))

# 6.1
def vers_binaire(n):
    if n == 0:
        return "0"
        
    chiffres = ""
    while n > 0:
        reste = n % 2
        chiffres = str(reste) + chiffres
        n = n // 2
        
    return chiffres

# correction
def vers_binaire(n):
    """Écriture binaire de l'entier positif n, sans le préfixe 0b."""
    if n == 0:
        return "0"
    chiffres = ""
    while n > 0:
        chiffres = str(n % 2) + chiffres
        n = n // 2
    return chiffres

print(vers_binaire(37), vers_binaire(0), vers_binaire(1024))
print(all(vers_binaire(n) == bin(n)[2:] for n in range(2000)))

# 6.2
eps = 1.0
while 1.0 + eps / 2 != 1.0:
    eps = eps / 2
    
print("Le plus petit nombre (epsilon) :", eps)

# correction
import sys

eps = 1.0
while 1.0 + eps / 2 != 1.0:
    eps = eps / 2

print(eps)
print(sys.float_info.epsilon)
print(eps == 2 ** -52)

# ============================================================
# EXERCICE 7
# ============================================================

import math
from fractions import Fraction

def racines_naif(a, b, c):
    """Racines réelles de ax² + bx + c par la formule classique."""
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("pas de racine réelle")
    r = math.sqrt(delta)
    return (-b - r) / (2 * a), (-b + r) / (2 * a)

# 7.2 La formule stable détaillée
def racines_stables(a, b, c):
    delta = b * b - 4 * a * c
    r = math.sqrt(delta)
    
    # On choisit le bon calcul pour éviter de soustraire deux nombres très proches
    if b >= 0:
        sure = (-b - r) / (2 * a)
    else:
        sure = (-b + r) / (2 * a)
        
    autre = c / (a * sure)
    
    # On renvoie la plus petite puis la plus grande
    if sure < autre:
        return sure, autre
    else:
        return autre, sure

# 7.3 Addition exacte avec les Fractions
total_exact = Fraction(0, 1)
for i in range(1000):
    total_exact = total_exact + Fraction(1, 10)
    
print("Le résultat exact est :", total_exact)


# correction

import math

def racines_naif(a, b, c):
    """Racines réelles de ax² + bx + c par la formule classique."""
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("pas de racine réelle")
    r = math.sqrt(delta)
    return (-b - r) / (2 * a), (-b + r) / (2 * a)

petite, grande = racines_naif(1.0, -1e8, 1.0)
print(petite, grande)
print("produit :", petite * grande, "attendu : 1")

def racines(a, b, c):
    """Racines réelles de ax² + bx + c, sans élimination catastrophique."""
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("pas de racine réelle")
    r = math.sqrt(delta)
    # on choisit le signe qui additionne au lieu de soustraire
    if b >= 0:
        sure = (-b - r) / (2 * a)
    else:
        sure = (-b + r) / (2 * a)
    autre = c / (a * sure)
    return min(sure, autre), max(sure, autre)

petite, grande = racines(1.0, -1e8, 1.0)
print(petite, grande)
print("produit :", petite * grande)
for x in (petite, grande):
    residu = x * x - 1e8 * x + 1
    print(f"residu : {residu:.1e}, soit {residu / max(x * x, 1.0):.1e} en relatif")

total = Fraction(0)
for _ in range(1000):
    total = total + Fraction(1, 10)
print(total, total == 100)
print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))
