from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.mixins import EmailCreateView
from django.views.generic import DetailView


new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição')

detail = DetailView.as_view(model=Subscription)


# def new(request):
#     if request.method == 'POST':
#         return create(request)
#     else:  # no caso GET
#         return empty_form(request)


# def create(request):
#     form = SubscriptionForm(request.POST)

#     if not form.is_valid():
#         return render(request, 'subscriptions/subscription_form.html', {'form': form})

#     # Save in the databse
#     subscription = Subscription.objects.create(**form.cleaned_data)

#     # Send email
#     _send_email('subscriptions/subscription_email.txt',
#                 {'subscription': subscription},
#                 'Confirmação de inscrição',
#                 settings.DEFAULT_FROM_EMAIL,
#                 subscription.email
#                 )
    
#     return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


# def empty_form(request):
#     return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


# def detail(request, pk):
#     try:
#         subscription = Subscription.objects.get(pk=pk)
#     except Subscription.DoesNotExist:
#         raise Http404
#     return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


# def _send_email(template_name, context, subject, from_, to):
#     body = render_to_string(template_name, context)
#     mail.send_mail(subject,  # assunto
#                    body,  # message body
#                    from_,  # sender (quem envia)
#                    [from_, to])  # receiver (pessoas que receberão)
    

# Esse _ no início indica que o programador que ler isso não deve acessar essa função diretamente em outros locais.
