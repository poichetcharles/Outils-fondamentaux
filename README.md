# Outils-fondamentaux

**Auteur :** Charles Poichet  
**Groupe :** S1 C1  

---

## Structure du dépôt

* **`tp/`** : Contient l'ensemble de mes solutions réalisées lors des séances de travaux pratiques.
* **`projet/`** : Contient le code source de mon projet personnel.
---

## Présentation du projet

Ce projet applique les concepts d'arithmétique modulaire à un cas d'usage concret : la sécurisation des données de télémétrie en Formule 1. Il compare deux approches de chiffrement :
1. **Le chiffrement RSA (asymétrique)** : Implémenté "from scratch" avec génération de nombres premiers, calcul du PGCD, recherche de l'inverse modulaire et exponentiation rapide.
2. **Le masque jetable de Vernam (symétrique)** : Implémenté via des opérations binaires (XOR) et la manipulation de fichiers texte.

L'objectif est d'étudier le compromis entre la sécurité mathématique face à une attaque par factorisation et la vitesse d'exécution requise pour des données envoyées en temps réel à plus de 300 km/h.

## Notions mathématiques mobilisées

* **Arithmétique et nombres premiers** : Génération de nombres premiers et recherche de diviseurs pour la création des clés publiques/privées.
* **Calcul modulaire** : Implémentation de l'exponentiation modulaire rapide pour chiffrer et déchiffrer efficacement, et calcul de l'inverse modulaire.
* **Complexité algorithmique** : Mesure du temps d'exécution (`time.perf_counter`) d'une attaque par force brute (factorisation du module $n$) pour évaluer la résistance du RSA selon la taille de la clé.
* **Calcul numérique et visualisation** : Génération d'un graphique d'évolution du temps de cassage en fonction de la taille en bits à l'aide de Matplotlib.

## Comment lancer le projet et ce qu'il faut observer

**Prérequis :** Python 3 et la bibliothèque `matplotlib` (`pip install matplotlib`).

1. Placez-vous dans le répertoire `projet/`.
2. Exécutez le script principal : `python nom_du_script.py`
3. **Observations attendues :**
   * La console affichera une course de vitesse entre RSA et Vernam pour le chiffrement d'une donnée de télémétrie aléatoire, prouvant la supériorité de Vernam en termes de rapidité d'exécution.
   * Le script lancera ensuite une attaque par factorisation sur des clés RSA de tailles croissantes (8, 9, 10, 11 bits).
   * Un graphique (`resultats_rsa_f1.png`) sera généré, montrant l'explosion exponentielle du temps nécessaire pour casser une clé RSA à mesure que sa taille augmente.

## Originalité, résultats et limites reconnues

**Interprétation des résultats :**
Le code démontre expérimentalement que le chiffrement RSA est hautement vulnérable si le module $n$ est trop petit. Le graphique généré montre clairement la courbe exponentielle de la complexité de l'attaque par factorisation. Vernam, en revanche, offre une sécurité mathématique absolue (cassage infini) et une vitesse d'exécution supérieure.

**Limites identifiées :**
* *Recherche de l'inverse modulaire :* L'implémentation actuelle utilise une boucle naïve pour trouver la clé privée $d$. Pour des clés robustes (ex: 2048 bits), il est impératif de basculer sur l'algorithme d'Euclide étendu, sous peine d'un temps de génération infini.
* *Test de primalité :* La recherche des diviseurs premiers teste actuellement les nombres jusqu'à $n$. Une optimisation mathématique stricte exigerait de s'arrêter à $\sqrt{n}$.
* *Logistique F1 :* Si Vernam gagne sur le plan mathématique et temporel, son défaut logistique le rend impraticable en F1 : il nécessite l'échange préalable et sécurisé d'une clé aléatoire aussi longue que le flux continu de données généré par la monoplace.

## Usage de l'Intelligence Artificielle

L'assistant Gemini a été utilisé dans ce projet comme outil de relecture et de conseil. Il a permis de structurer la comparaison des temps d'exécution, d'affiner l'usage de Matplotlib pour un rendu visuel propre, et de mettre en évidence les limites de mon implémentation naïve (notamment l'absence de l'Euclide étendu et l'optimisation $\sqrt{n}$ pour les nombres premiers). Les choix thématiques, l'assemblage logique et l'analyse critique des résultats restent entièrement personnels.




















## Présentation du projet personnel

### Sécurisation des données de télémétrie en Formule 1 avec RSA

En Formule 1, les voitures transmettent de nombreuses informations aux ingénieurs pendant les essais et les courses. Ces données peuvent concerner la vitesse, le régime moteur, la température des pneus ou encore le système de freinage.

Ces informations peuvent être stratégiques pour une écurie. Il est donc intéressant d'étudier comment un système de chiffrement peut permettre de protéger leur transmission.

L'objectif de ce projet est de créer une simulation simplifiée du chiffrement RSA, puis d'étudier sa résistance face à une tentative de cassage de clé.

### Fonctionnement du programme

Le projet est organisé autour de plusieurs étapes :

1. **Génération des clés RSA :** création de deux nombres premiers, calcul du module RSA et détermination des clés publique et privée.
2. **Chiffrement des données :** simulation de l'envoi d'une donnée de télémétrie, par exemple la vitesse d'une Formule 1.
3. **Déchiffrement :** récupération de la donnée originale à l'aide de la clé privée.
4. **Attaque par factorisation :** simulation d'une tentative de récupération des deux nombres premiers à partir de la clé publique, afin de retrouver la clé privée.
5. **Étude expérimentale :** mesure du temps nécessaire pour factoriser différentes clés RSA et représentation des résultats sous forme de graphique.

### Notions mathématiques utilisées

Le projet mobilise plusieurs notions abordées pendant les travaux pratiques :

- **Arithmétique :** nombres premiers, divisibilité et calcul du PGCD.
- **Arithmétique modulaire :** calculs modulo n utilisés pour le chiffrement et le déchiffrement RSA.
- **Algorithmes :** recherche de nombres premiers, factorisation et exponentiation rapide.
- **Calcul numérique :** mesure et comparaison des temps d'exécution.
- **Représentation graphique :** visualisation de l'évolution du temps de factorisation en fonction de la taille des clés.

---

## Installation et lancement

### Prérequis

Le projet nécessite :
- Python 3.
- La bibliothèque `matplotlib`.

Pour installer la bibliothèque, exécuter la commande suivante dans un terminal :

```bash
pip install matplotlib
```

### Lancement du programme

Depuis le dossier du projet, exécuter :

```bash
python rsa_f1.py
```

Le programme lance automatiquement :
- Une simulation de chiffrement et de déchiffrement d'une donnée de télémétrie.
- Une tentative de cassage de plusieurs clés RSA.
- Une mesure des temps d'exécution.
- Un graphique présentant les résultats expérimentaux.

Le graphique est également enregistré sous le nom `resultats_rsa_f1.png`.

---

## Résultats et observations

L'expérience permet d'observer le fonctionnement du chiffrement RSA et de comprendre le rôle des nombres premiers dans la sécurité du système.

En augmentant la taille des nombres premiers utilisés pour générer les clés, le module RSA devient plus grand. La recherche de
