from unittest.mock import Mock
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        # Criando uma inscrição no banco
        Subscription.objects.create(name='Maisa', cpf='78945612398',
                                    email='maisa@maisa.com', phone='21-996658541')
        
        # Instânciando o SubscriptionModelAdmin
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)


    def test_has_action(self):
        """Action mark_as_paid should be installed."""
        self.assertIn('mark_as_paid', self.model_admin.actions)


    def test_mark_all(self):
        """It should mark all selected subscriptions as paid."""
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count()) # Verificando o resultado


    def test_message(self):
        """It should send a message to the user."""
        mock = self.call_action()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')


    # Esse é um método auxiliar criado para evitar que o mesmo código fique se repetindo em vários métodos.
    def call_action(self):
        # Montando uma Query
        queryset = Subscription.objects.all()

        # Configura um novo valor para o "message_user"
        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        # Chamando a action passando a query
        self.model_admin.mark_as_paid(None, queryset)

        # Retorna o valor anterior que tinha o "message_user"
        SubscriptionModelAdmin.message_user = old_message_user

        return mock