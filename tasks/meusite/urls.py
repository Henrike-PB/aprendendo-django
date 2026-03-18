# meusite/urls.py

from django.contrib import admin
# Importa include — permite encaminhar pra URLs de outro app
from django.urls import path, include

urlpatterns = [
    # Ramal do admin (já vinha pronto)
    path('admin/', admin.site.urls),
    # Encaminha tudo que começa com tarefas/ pro urls.py do app
    path('tarefas/', include('tarefas.urls')),
]