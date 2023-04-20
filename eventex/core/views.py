from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk
from django.views.generic import ListView, DetailView


# Toda View do Djando é um objeto chamado, seja uma função, uma classe ou uma instância.
# Sempre recebe como 1º parâmentro uma instância de http request.
# E retorna uma instância de http response.


# class HomeView(ListView): # Class Based View - Usada quando se tem muita repetição de código, consegue generializar.
#     template_name = 'index.html'
#     model = Speaker


# Aqui é usado as conversões do Django para as Views.
# A mesma coisa pode ser feita nas 2 views abaixo.
home = ListView.as_view(template_name = 'index.html', model = Speaker)
speaker_detail = DetailView.as_view(model = Speaker)
talk_list = ListView.as_view(model = Talk)



# As Views Padrões foram substituidas por Views já convencionadas pelo Django.

# def home(request): 
#     speakers = Speaker.objects.all()
#     return render(request, 'index.html', {'speakers': speakers}) # processa o request com um template.


# def speaker_detail(request, slug):
#     speaker = get_object_or_404(Speaker, slug=slug)
#     return render(request, 'core/speaker_detail.html', {'speaker': speaker})


# def talk_list(request):
#     context = {
#         'morning_talks': Talk.objects.at_morning(),
#         'afternoon_talks': Talk.objects.at_afternoon(),
#     }
#     return render(request, 'core/talk_list.html', context)