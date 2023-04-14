from django import forms
from django.core.exceptions import ValidationError


# Esse 'validator' retorna um 'validater error' caso não passe na validação.

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')
    
    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='E-mail', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    # Esse é um método especial, basta chamar o 'clean' mais o '_' e mais o nome do campo.
    # Quando implementar esse método, é necessário retornar o valor correto, porque ele vai substituir o 'cleaned_data['name']'
    def clean_name(self):
        name = self.cleaned_data['name']

        words = []
        for w in name.split():
            words.append(w.capitalize())

        # OU, agora usando List Comprehension
        # words = [w.capitalized() for w in name.split()]

        capitalized_name = ' '.join(words)
        return capitalized_name
    
    # Esse é o 'clean' do formulário como um todo, ele é chamado depois de todos os outros 'clean'.
    def clean(self):
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')
        
        return self.cleaned_data # precisa retornar os dados, mesmo que não haja nenhuma modificação.
