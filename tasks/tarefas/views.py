from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Essa função é a view — o "atendente" do departamento
# Ela recebe um pedido (request) e devolve uma resposta
def index(request):
    return HttpResponse("Henrike está aprendendo Django! 🚀")