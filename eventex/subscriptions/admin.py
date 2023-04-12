from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribed_today') # colunas da tabela no painel admin.
    date_hierarchy = 'created_at' # ordenação pela data
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at') # cria um campo de pesquisa.
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at == now().date()
    
    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True

admin.site.register(Subscription, SubscriptionModelAdmin)