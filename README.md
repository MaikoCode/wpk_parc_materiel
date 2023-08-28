# Gestion de Parc Matériel en Django

Ce projet est une application web développée en Django pour gérer un parc matériel. Il permet aux administrateurs et aux employés de suivre et de gérer divers équipements.

## Prérequis

- Python 3.x
- pip
- Virtualenv
- PostgreSQL

## Installation

Suivez ces étapes pour installer et configurer ce projet sur votre machine locale.

### Étape 1 : Cloner le dépôt

```bash
git@git-wpk.pilotsystems.net:wpk/parc-materiel.git
```

### Étape 2 : Naviguer dans le dossier du projet

```bash
cd parc-materiel
```

### Étape 3 : Créer et activer un environnement virtuel

```bash
python -m venv env
env/Scripts/activate  # Sur Windows, utilisez `env\Scripts\activate`
```

### Étape 4 : Installer les dépendances

```bash
pip install -r requirements.txt
```

## Configuration

### Configurer la base de données

1. Créez un fichier nommé `local_settings.py` dans le même dossier que votre `settings.py`.
2. Ajoutez-y les configurations de la base de données comme suit:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<Votre nom de la base de données>',
        'USER': '<Votre nom d'utilisateur>',
        'PASSWORD': '<Votre mot de passe>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
3. Executez ensuite:
```bash
python manage.py migrate
```


### Créer le superutilisateur

Pour créer le premier utilisateur administrateur de l'application, exécutez la commande suivante:

```bash
python manage.py createsuperuser
```

Suivez les instructions pour créer le superutilisateur.


## Utilisation

### Lancement de l'application

```bash
python manage.py runserver
```

### Se connecter à l'interface d'administration pour créer de nouveaux comptes ADMIN

Naviguez vers `http://localhost:8000/admin` pour accéder à l'interface d'administration.

Dans l'interface admin créez un nouveau employé à la suite un nouveau utilisateur est automatiquement crée et vous pourrez par la suite changer le role de l'utilisateur en ADMIN ou en USER(par defaut il est en USER)

[Interface admin](./admin1.jpeg)

### Se connecter à l'application

Ensuite vous pouvez vous rendre sur `http://localhost:8000/` pour utiliser l'application

#### Identifiants
- **Nom d'utilisateur** : Correspond à l'adresse email.
- **Mot de passe** : Initialement, il correspond au nom de l'employé. Il est recommandé de le changer lors de la première connexion.



