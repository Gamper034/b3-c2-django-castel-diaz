# Nom du projet

Password Manager

## Prérequis

- Python 3+
- Django 5+

## Installation

1. Clonez ce dépôt :
    ```
    git clone https://github.com/Gamper034/b3-c2-django-castel-diaz
    ```
2. Accédez au répertoire du projet :
    ```
    cd project
    ```
3. Effectuez les migrations :
    ```
    python manage.py migrate
    ```

## Utilisation

Pour lancer le serveur de développement, exécutez :
    ```
    python3 manage.py runserver
    ```
Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/`.

## Utilisation avec Docker

Si vous avez Docker installé, vous pouvez construire et exécuter l'application en utilisant les commandes Docker suivantes :

1. Construisez l'image Docker :
    ```
    docker build -t password_manager .
    ```
2. Exécutez le conteneur Docker :
    ```
    docker run -d -p 8000:8000 password_manager
    ```

Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/`.

## Tests

Pour exécuter les tests, utilisez :
    ```
    python manage.py test
    ```