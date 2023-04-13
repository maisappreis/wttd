from django.conf import settings
from django.http import Http404, HttpResponseRedirect
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

    # Save in the databse
    subscription = Subscription.objects.create(**form.cleaned_data)

    # Send email
    _send_email('subscriptions/subscription_email.txt',
                {'subscription': subscription},
                'Confirmação de inscrição',
                settings.DEFAULT_FROM_EMAIL,
                subscription.email
                )
    
    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.pk))


def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


def _send_email(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    mail.send_mail(subject,  # assunto
                   body,  # message body
                   from_,  # sender (quem envia)
                   [from_, to])  # receiver (pessoas que receberão)
    

# Esse _ no início indica que o programador que ler isso não deve acessar essa função diretamente em outros locais.
