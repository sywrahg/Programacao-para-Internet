from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.contrib.auth.models import User
from perfis.models import Perfil
from usuarios.forms import RegistrarUsuarioForm

# Create your views here.

class RegistrarUsuarioView(View):
	template_name = 'registrar.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		form = RegistrarUsuarioForm(request.POST)
		if form.is_valid():
			dados_form = form.cleanned_data
			usuario= User.objects.create(username, dados_form['nome'], email = dados_form['email'], password = dados_form['senha'])

			perfil = Perfil(nome = dados_form['nome'], telefone = dados_form['telefone'], nome_empresa= dados_form['nome_empresa'], usuario = usuario)

			perfil.save()
			return redirect('index')

		return render(request, self.template_name, {'form': form})