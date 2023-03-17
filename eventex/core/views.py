from django.shortcuts import render

# Toda View do Djando é um objeto chamado, seja uma função, uma classe ou uma instância.
# Sempre recebe como 1º parâmentro uma instância de http request.
# E retorna uma instância de http response.

def home(request):
    return render(request, 'index.html') # processa o request com um template.