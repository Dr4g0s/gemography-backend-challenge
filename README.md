# backend-coding-challenge
- REST microservice that list the languages used by the 100 trending public and most starred repos created in the last 30 day descending order on GitHub.

## Functional specs
- Develop a REST microservice that list the languages used by the 100 trending public repos on GitHub.
- For every language, you need to calculate the attributes below:
    - Number of repos using this language.
    - The list of repos using the language.

## Technologies
- Python
- Django
- Django REST Framework

## Run project
1. run `pip install -r requirements.txt` to install project dependencies.
2. run `python manage.py runserver` to start project.

## API list
- `http://127.0.0.1:8000/api/repos-list/` display pure response from github in json format.
- `http://127.0.0.1:8000/api/language-list/` display languages formated list
