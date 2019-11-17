# Django Restful Framework 

Projeto básico com exemplos de uso do Django Rest Framework

# Autores:

* **Thiago Pires** - *Desenvolvedor*;

## Requisitos do sistema:

* Python3.7;
* Django 2.2.7;
* Django Rest Framewor 3.10.3;

### Comandos importantes:

Criar ambiente virtual
```
python3 -m venv venv
```
Instalar Django
```
pip install django
```
Instalar Django Framework
```
pip install djangorestframework
```
Criar projeto django
```
django-admin startproject [nome do projeto]
```
Criar um super-usuário
```
python manage.py createsuperuser
```
Criar as tabelas no banco de dados
```
python manage.py migrate
```
Fazer migrations 
```
python manage.py makemigrations
```
Rodar o projeto
```
python manage.py runserver
```
Criar uma app
```
python manage.py startapp [nome da app]
```

# Extras

Após criar uma app é necessário registrá-la em settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # nova app criada
]
```
