# Youtube Playlist Downloarder

- A simple GUI to download your own Youtube playlists 
- Une ptite interface graphique pour télécharger ses playlists Youtube


# Lancer depuis un terminal / Run from terminal : 

- Se placer depuis le terminal dans le dossier où l'on exécute le script / In terminal go in directory where you will execute the script :

- Avant toute chose on clone le répository git / Clone repository:

    git clone: https://github.com/LGD-P/YoutubePlaylistDownloarder.git

-Une fois le projet cloné on crée et on active l'environnement virtuel / creat virtual environement:

    python3 -m venv env

-Suivi de / activate it:

    source env/bin/activate

-Puis on lance l'installation des modules nécessaires au fonctionnement du script / install dependancies :

    pip install -r requirements.txt


-Il n'y a plus qu'à exécuter le script / execute the script:

    python3 main.py


# Lancer comme un exécutable Windows / Run as executable from .sh file :

Créer et écrire un fichier  .sh / creat and write.sh file: 

    touch Ydl.sh
    nano Ydl.sh

-1 : Ecrire le shebang / Write Shebang

-2 : pointer vers le fichier main.py / point to the right path

-3 : Ecrire la commande pour exécuter le script / Write command to execute script:


    #!/bin/bash
    
    cd your_path/to_folder/containing_main.py
    
    python3 main.py

*save .sh with ctrl + x*

-4 : Rendre le fichier .sh executable / make .sh file executable:

    sudo chmod +x Ytl.sh 

