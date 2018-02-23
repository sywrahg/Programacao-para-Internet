from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):
	
	def is_valid(self):
		valid = True
		if not super(RegistrarUsuarioForm, self).is_valid():
			self.adiciona_erro('Por favor, verifique os dados informados')
			valid = False

		user_exists = User.objects.filter(username=self.cleaned_data['nome']).exists()
		if user_exists:
			self.adiciona_erro('Usuario ja existe')
			valid = False

		return valid
