# Outils-fondamentaux

**Auteur :** Charles Poichet  
**Groupe :** S1 C1  
**Module :** Mathématiques – Calcul numérique et Arithmétique

---

## Structure du dépôt

Ce dépôt est organisé en deux parties distinctes, conformément aux consignes du module :

- `tp/` : Contient l'ensemble de mes solutions aux travaux pratiques, ainsi que mes essais et les exercices retravaillés après les séances.
- `projet/` : Contient mon projet personnel consacré au chiffrement RSA et à son utilisation pour sécuriser des données de télémétrie en Formule 1.

---

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
