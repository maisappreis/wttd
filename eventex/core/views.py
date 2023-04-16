from django.shortcuts import render

# Toda View do Djando é um objeto chamado, seja uma função, uma classe ou uma instância.
# Sempre recebe como 1º parâmentro uma instância de http request.
# E retorna uma instância de http response.

def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},
        {'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'}
    ]
    return render(request, 'index.html', {'speakers': speakers}) # processa o request com um template.