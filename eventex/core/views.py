from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk, Course


# Toda View do Djando é um objeto chamado, seja uma função, uma classe ou uma instância.
# Sempre recebe como 1º parâmentro uma instância de http request.
# E retorna uma instância de http response.

def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers}) # processa o request com um template.

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})

def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }
    return render(request, 'core/talk_list.html', context)