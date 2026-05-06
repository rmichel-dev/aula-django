# passo 1

python -m venv venv

# passo 2
 .\venv\Scripts\activate

# passo 3
  pip install django

# passo 4
django-admin startproject setup .

# passo 5
python manage.py startapp ecommerce

# passo 6 (testar se esta ok)
python manage.py runserver
CTRL + C (para parar  o server)

# passo 7 (será executado toda vez que o model for alterado)
python manage.py makemigrations

# passo 8 (após o passo 7)
python manage.py migrate

# passo 9
python manage.py createsuperuser

# passo 10
## Rodar o server (passo 6) + abrir http://127.0.0.1:8000/admin/login



# passo 11
## configurar o settings
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecommerce',
]

# passo 12
criar a pasta 
'ecommerce\templates\ecommerce'


# passo 13
{% load static %}

# passo 14 
<img src="{% static 'ecommerce/img/logo.png' %}" alt="Logo">