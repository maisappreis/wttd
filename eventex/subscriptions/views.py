from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from django.contrib import messages
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:  # no caso GET
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    # Send email
    _send_email('subscriptions/subscription_email.txt',
                form.cleaned_data,
                'Confirmação de inscrição',
                settings.DEFAULT_FROM_EMAIL,
                form.cleaned_data['email'])
    
    # Save in the databse
    Subscription.objects.create(**form.cleaned_data)

    # Success feedback
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def _send_email(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    mail.send_mail(subject,  # assunto
                   body,  # message body
                   from_,  # sender (quem envia)
                   [from_, to])  # receiver (pessoas que receberão)
    

# Esse _ no início indica que o programador que ler isso não deve acessar essa função diretamente em outros locais.
