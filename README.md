# OC-P4
Chess software
1) Description de l'application
Ce projet consiste en une application python qui permet de :

gérer des tournois d'échecs
gérer des joueurs d'échecs
générer des rapports relatifs aux tournois et aux joueurs :
Liste de tous les acteurs
Liste de tous les joueurs d'un tournoi
Liste de tous les tournois

L'application se lance à partir du programme main.py situé à la racine du projet en lançant main.py

2) Installation du projet en local sur votre machine

  Créer un dossier dans lequel vous allez installer le projet. 
  Allez sur le depot github https://github.com/naegel23/OC-P4
  Télécharger le fichier en zip puis placer votre fichier zip dans le dossier précédemment créé.
  Ouvrir votre terminal et se déplacer dans la racine du projet dossier.
  
 3) Configuration de l'environnement virtuel

Pour Windows, on utilise python et pip.

Pour Mac OS, on utilise python3 et pip3.

3.1) Installer pip pour python3 si ce n'est pas déjà fait
Si la commande pip3 --version renvoie une erreur alors il convient d'installer pip

sudo apt-get update && sudo apt-get install python3-pip

Si l'installation a réussi, la commande vous renverra une ligne indiquant la version pip installé 

3.2) Créer un environnement virtuel et l'activer
Se placer à la racine du projet (dossier dans lequel se trouve le fichier main.py) et lancer la commande :

python3 -m venv env

Une fois l'environnement virtuel env créé, l'activer avec la commande :

source env/bin/activate

3.4) Installer les dépendances du projet
Toujours à la racine du projet, lancer l'une des 2 commandes suivantes :

pip3 install -r requirements.txt

python3 -m pip install -r requirements.txt

4) Execution du programme

Afin d'executer le programme il vous suffit de taper la commande python3 main.py

5) Rapport flake8-html
La commande pour générer les rapports flake8-html de vérification de conformité du code source est la suivante :

flake8 --format=html --htmldir=flake-report --exclude=env/;images/

Attention : se positionner à la racine du projet et exclure les répertoires env/ et images/ du périmètre de fichiers à analyser.

Le résultat se trouve dans le dossier flake-report
Il suffit alors d'ouvrir le fichier index.html dans votre navigateur Internet.
