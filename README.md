# Outils-fondamentaux

**Auteur :** Charles Poichet  
**Groupe :** C1

---

## Structure du dépôt

Le dépôt est organisé en deux parties :

- **`tp/`** : Regroupe mes solutions réalisées pendant les séances de TP.
- **`projet/`** : Contient les fichiers de mon projet personnel.

---

## Présentation du projet

Pour ce projet, j'ai choisi de travailler sur la sécurisation des données de télémétrie en Formule 1.

L'idée est de comparer deux méthodes de chiffrement :

1. **RSA (chiffrement asymétrique)** : Cette méthode utilise une clé publique pour chiffrer et une clé privée pour déchiffrer. J'ai notamment travaillé sur la génération des nombres premiers, le PGCD et l'exponentiation modulaire.
2. **Vernam (chiffrement symétrique)** : Cette méthode utilise une clé aléatoire et des opérations binaires pour chiffrer les données.

Le but est de comparer ces deux méthodes, notamment leur vitesse et leur résistance face aux tentatives de cassage. Le contexte de la Formule 1 permet aussi de voir l'importance de la rapidité lorsque les données doivent être envoyées en temps réel.

Grâce à la spécialité NSI que j'ai suivie en Terminale, j'avais déjà quelques bases en programmation et sur ces deux algorithmes. J'ai donc pu reprendre ce travail et l'améliorer pour réaliser ce projet.

## Notions mathématiques utilisées

Ce projet m'a permis de mettre en pratique plusieurs notions vues pendant le module :

- **Nombres premiers** : Génération et recherche de nombres premiers pour créer les clés RSA.
- **Arithmétique modulaire** : Utilisation de l'exponentiation rapide et recherche de l'inverse modulaire.
- **Complexité algorithmique** : Mesure du temps nécessaire pour retrouver les facteurs d'une clé RSA avec une attaque par force brute.
- **Calcul numérique et graphiques** : Utilisation de `time.perf_counter` pour mesurer les temps et de Matplotlib pour afficher les résultats sous forme de graphique.

## Lancer le projet et résultats attendus

**Prérequis :**
- Python 3
- La bibliothèque `matplotlib`

**Ce que fait le programme :**

- Il génère une donnée de télémétrie aléatoire et la chiffre avec RSA puis avec Vernam.
- Il affiche les temps d'exécution pour comparer les deux méthodes.
- Il lance ensuite une attaque par factorisation sur plusieurs petites clés RSA (8, 9, 10 et 11 bits).
- Il génère un graphique pour montrer l'évolution du temps nécessaire pour retrouver les facteurs selon la taille de la clé.

On peut ainsi observer que Vernam est plus rapide dans ce test. On remarque également que le cassage d'une clé RSA devient plus difficile lorsque sa taille augmente.

## Résultats et limites du projet

Les tests montrent que RSA est facilement cassable lorsque les clés utilisées sont trop petites. C'est notamment le cas des clés de quelques bits utilisées dans ce projet.

Vernam présente un avantage intéressant : lorsqu'il est utilisé avec une clé parfaitement aléatoire, aussi longue que le message et jamais réutilisée, il offre une sécurité théorique absolue.

Cependant, les deux méthodes ont aussi leurs limites.

**Quelques limites de mon code :**

- **Inverse modulaire :** J'utilise actuellement une boucle pour trouver l'inverse modulaire. Cette méthode fonctionne avec de petites valeurs, mais devient beaucoup trop lente avec de grandes clés. L'algorithme d'Euclide étendu serait plus adapté.
- **Recherche des nombres premiers :** Mon programme teste actuellement les diviseurs jusqu'au nombre lui-même. Il serait possible d'améliorer cette recherche en s'arrêtant à sa racine carrée.
- **Utilisation de Vernam en Formule 1 :** Même si cette méthode est rapide et très sûre, elle demande de partager une clé secrète aussi longue que les données à transmettre. Il faudrait donc pouvoir échanger et stocker ces clés de manière sécurisée, ce qui complique son utilisation en pratique.

## Utilisation de l'intelligence artificielle

J'ai utilisé Gemini comme aide pendant la réalisation du projet.

Il m'a notamment aidé à améliorer la présentation des résultats, à utiliser Matplotlib et à repérer certaines limites dans mon code.

Je me suis également servi de ses conseils pour réfléchir aux améliorations possibles, notamment pour le calcul de l'inverse modulaire et la recherche des nombres premiers.

Le choix du sujet, les différentes parties du projet et le travail de programmation restent les miens.
