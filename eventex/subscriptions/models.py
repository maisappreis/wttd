from django.db import models
from django.shortcuts import resolve_url as r


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    # protocolo do Python para dizer o que acontece com qualquer objeto Python quando eu instancio uma string a partir dele.
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return r('subscriptions:detail', self.pk)