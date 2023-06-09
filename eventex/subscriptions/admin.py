from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf',
                    'created_at', 'subscribed_today', 'paid') # Exibe as colunas da tabela no painel admin.
    date_hierarchy = 'created_at' # ordenação pela data
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at') # cria um campo de pesquisa.
    list_filter = ('paid', 'created_at')

    actions = ['mark_as_paid']

    def subscribed_today(self, obj):
        return obj.created_at == now().date()
    
    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid = True)

        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcadas como pagas.'
        
        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar como pago'

admin.site.register(Subscription, SubscriptionModelAdmin)