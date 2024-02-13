Code source - Projet Design Factory Air Pays de la Loire
==========

### Contient :

- Script main.py contenant la récupération des données d'Air Pays de la Loire, le choix la couleur à afficher et son envoi au programme contrôlant les LED ;
- Une version modifié du programme [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) (© 2014, jgarff)


### Compilation:

- Installer Scons `sudo apt-get install scons`;
- Dans le dossier rpi_ws281x, executer la commande `scons`.

### Lancement:

Lancer le script python en super-utilisateur avec la commande `sudo python main.py`. Son lancement peut être automatisé par une tâche système, pour permettre une actualisation régulière (dans le cas du prototype, toutes les 30 minutes).