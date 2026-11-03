# Outils-fondamentaux

**Auteur :** Charles Poichet  
**Groupe :** S1 C1  

---

## Structure du dépôt

* **`tp/`** : Contient l'ensemble de mes solutions réalisées lors des séances de travaux pratiques.
* **`projet/`** : Contient le code source de mon projet personnel.
---

## Présentation du projet

Ce projet applique les concepts d'arithmétique modulaire à un cas d'usage concret avec la sécurisation des données de télémétrie en Formule 1. Il compare deux approches de chiffrement :
1. **Le chiffrement RSA (asymétrique)** : Implémenté avec génération de nombres premiers, calcul du PGCD, recherche de l'inverse modulaire et exponentiation rapide.
2. **Le masque jetable de Vernam (symétrique)** : Implémenté via des opérations binaires et la manipulation de fichiers texte.

L'objectif est d'étudier le compromis entre la sécurité mathématique face à une attaque par factorisation et la vitesse d'exécution requise pour des données envoyées en temps réel.

## Notions mathématiques mobilisées

* **Arithmétique et nombres premiers** : Génération de nombres premiers et recherche de diviseurs pour la création des clés publiques/privées.
* **Calcul modulaire** : Implémentation de l'exponentiation modulaire rapide pour chiffrer et déchiffrer efficacement, et calcul de l'inverse modulaire.
* **Complexité algorithmique** : Mesure du temps d'exécution (`time.perf_counter`) d'une attaque par force brute pour évaluer la résistance du RSA selon la taille de la clé.
* **Calcul numérique et visualisation** : Génération d'un graphique d'évolution du temps de cassage en fonction de la taille en bits à l'aide de Matplotlib.

## Comment lancer le projet et ce qu'il faut observer

**Prérequis :** Python 3 et la bibliothèque `matplotlib`.

**Observations attendues :**
   * La console affichera un comparatif entre le RSA et Vernam pour le chiffrement d'une donnée de télémétrie aléatoire, prouvant la supériorité de Vernam en termes de rapidité d'exécution.
   * Le script lancera ensuite une attaque par factorisation sur des clés RSA de tailles croissantes (8, 9, 10, 11 bits).
   * Un graphique sera généré, montrant l'explosion exponentielle du temps nécessaire pour casser une clé RSA à mesure que sa taille augmente.

## Originalité, résultats et limites reconnues

**Interprétation des résultats :**
Le code démontre expérimentalement que le chiffrement RSA est hautement vulnérable si le module $n$ est trop petit. Le graphique généré montre clairement la courbe exponentielle de la complexité de l'attaque par factorisation. Vernam, en revanche, offre une sécurité mathématique absolue (cassage infini) et une vitesse d'exécution supérieure.

**Limites identifiées :**
* *Recherche de l'inverse modulaire :* L'implémentation actuelle utilise une boucle naïve pour trouver la clé privée $d$. Pour des clés robustes (ex: 2048 bits), il est impératif de basculer sur l'algorithme d'Euclide étendu, sous peine d'un temps de génération infini.
* *Test de primalité :* La recherche des diviseurs premiers teste actuellement les nombres jusqu'à $n$. Une optimisation mathématique stricte exigerait de s'arrêter à $\sqrt{n}$.
* *Logistique F1 :* Si Vernam gagne sur le plan mathématique et temporel, son défaut logistique le rend impraticable en F1 : il nécessite l'échange préalable et sécurisé d'une clé aléatoire aussi longue que le flux continu de données généré par la monoplace.

## Usage de l'Intelligence Artificielle

L'assistant Gemini a été utilisé dans ce projet comme outil de relecture et de conseil. Il a permis de structurer la comparaison des temps d'exécution, d'affiner l'usage de Matplotlib pour un rendu visuel propre, et de mettre en évidence les limites de mon implémentation naïve (notamment l'absence de l'Euclide étendu et l'optimisation $\sqrt{n}$ pour les nombres premiers). Les choix thématiques et la logique restent entièrement personnels.
