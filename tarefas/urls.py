# tarefas/urls.py

# Importa a função path — ela conecta URL a view
from django.urls import path

# Importa as views do nosso app
from . import views

# Lista de ramais deste departamento
urlpatterns = [
    # Quando acessar /tarefas/, chama a view index
    path('', views.index, name='index'),
]

