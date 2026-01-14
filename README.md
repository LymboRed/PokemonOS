# PokemonOS 🔋🔥💧

PokemonOS est un simulateur de combat Pokémon en ligne de commande, écrit en Python. Ce projet a été conçu pour explorer les principes de la **Programmation Orientée Objet (POO)** tout en s'amusant.

## ✨ Fonctionnalités

- **Système de Combat au Tour par Tour** : Choisissez vos attaques et affrontez l'adversaire.
- **Graphismes ASCII** : Visualisez Pikachu et Carapuce directement dans votre terminal.
- **Barres de Vie Dynamiques** : Les barres de HP changent de couleur (Vert → Orange → Rouge) selon les dégâts.
- **Mécaniques de Jeu** :
  - Table des types (Efficacité des attaques).
  - Coups critiques (10% de chance).
  - Ordre d'attaque basé sur la vitesse des Pokémon.
- **Interface Colorée** : Utilisation des codes ANSI pour une expérience immersive en CLI.

## 🚀 Installation et Lancement

### Prérequis
- [Python 3.x](https://www.python.org/downloads/) installé sur votre machine.

### Lancement
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/LymboRed/PokemonOS.git
   cd PokemonOS
   ```
2. Lancez le jeu :
   ```bash
   python3 main.py
   ```

## 🏗️ Structure du Projet

- `main.py` : Point d'entrée de l'application.
- `src/models/` : Contient les classes `Pokemon` et `Move`.
- `src/engine/` : Contient la logique de combat (`Battle`).

## 🛠️ Concepts de POO Appliqués
- **Encapsulation** : Les données des Pokémon et les mécaniques de combat sont isolées dans des classes.
- **Composition** : La classe `Pokemon` contient une liste d'objets `Move`.
- **Gestion d'État** : Suivi des points de vie et du déroulement du combat via les instances de classe.

---
Développé avec ❤️ pour apprendre la POO.
