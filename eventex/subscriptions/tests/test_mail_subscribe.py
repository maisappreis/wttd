from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r # Usa a estrutura de URLs nomeadas


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
                    email='henrique567@gmail.com', phone='21-99618-1234')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]
        
    def test_subscription_email_subject(self):
        excect = 'Confirmação de inscrição'
        self.assertEqual(excect, self.email.subject)

    def test_subscription_email_from(self):
        excect = 'contato@eventex.com.br'
        self.assertEqual(excect, self.email.from_email)

    def test_subscription_email_to(self):
        excect = ['contato@eventex.com.br', 'henrique567@gmail.com']
        self.assertEqual(excect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Henrique Bastos',
            '12345678901',
            'henrique567@gmail.com',
            '21-99618-1234'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

        # self.assertIn('Henrique Bastos', self.email.body)
        # self.assertIn('12345678901', self.email.body)
        # self.assertIn('henrique567@gmail.com', self.email.body)
        # self.assertIn('21-99618-1234', self.email.body)