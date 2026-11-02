# Outils-fondamentaux

**Auteur :** Charles Poichet  
**Groupe :** S1 C1
**Module :** Mathématiques - Calcul numérique et Arithmétique  

---

## Structure du dépôt

Ce dépôt est divisé en deux parties distinctes :
* `tp/` : Contient l'ensemble de mes solutions et essais réalisés lors des séances de Travaux Pratiques, retravaillés pour être propres et lisibles.
* `projet/` : Contient mon projet personnel centré sur la cryptographie RSA. Le script principal s'y trouve (ex: `rsa_benchmark.py`).

---

## Sujet du projet personnel

L'objectif de ce projet est de construire un système de chiffrement RSA "jouet" fonctionnel en partant de zéro, puis de le mettre à l'épreuve pour comprendre concrètement pourquoi la taille de la clé est le pilier de sa sécurité.

Le projet mobilise les notions suivantes vues en cours/TP :
* **Arithmétique modulaire :** Implémentation de l'algorithme d'Euclide étendu et de l'exponentiation modulaire rapide.
* **Calcul numérique :** Mesures de temps d'exécution et gestion des limites de calcul de la machine.
* **Représentation graphique :** Tracé d'une courbe exponentielle avec échelle logarithmique pour visualiser l'explosion de la complexité.

---

## Comment lancer le projet

**Prérequis :** 
Une installation de Python 3 avec la bibliothèque `matplotlib`.
Si vous ne l'avez pas, installez-la via le terminal :
```bash
pip install matplotlib
