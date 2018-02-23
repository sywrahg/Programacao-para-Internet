from django.shortcuts import render
from perfis.models import Perfil, Convite, Post
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
	'''import random
	n = random.randint(0,100)
	return render(request, 'index.html',
		          {'nome':'ely', 'n' : n})
	'''

	return render(request, 'index.html',{'perfis' : Perfil.objects.all(),
										 'perfil_logado' : get_perfil_logado(request)})

@login_required
def exibir_perfil(request, perfil_id):

	#perfil = get(perfil_id)
	perfil = Perfil.objects.get(id=perfil_id)
	timeline_my_posts = perfil.my_timeline.exibicao()

	return render(request, 'perfil.html',
		          {'perfil' : perfil, 
				   'perfil_logado' : get_perfil_logado(request),'timeline_my_posts': timeline_my_posts})

def get(perfil_id):
	if (perfil_id == 1):
		return Perfil('Ely', 'ely@ifpi.edu.br',
						'99999-9999', 'ifpi')				
	if (perfil_id == 2):
		return Perfil('Pedro', 'pedro@gmail.com',
						'99999-8888', 'Google')				
	if (perfil_id == 3):
		return Perfil('Maria', 'maria@hotmail.com',
						'88888-7777', 'MS')				

@login_required
def convidar(request,perfil_id):

	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	
	if(perfil_logado.pode_convidar(perfil_a_convidar)):
		perfil_logado.convidar(perfil_a_convidar)
	
	return  redirect('index')

@login_required
def get_perfil_logado(request):
	return request.user.perfil

@login_required
def aceitar(request, convite_id): 
	convite = Convite.objects.get(id = convite_id)
	convite.aceitar()
	return redirect('index')

@login_required
def recusar(request, convite_id): 
	convite = Convite.objects.get(id = convite_id)
	convite.recusar()
	return redirect('index')

@login_required
def desfazer(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil.desfazer(get_perfil_logado(request))
	return redirect('index')

@login_required
def excluir_post(request, post_id):
	post = Post.objects.get(id=post_id)
	if post.perfil.usuario == request.user:
		post.excluir()
	else:
		return render(request, 'error.html')

	return redirect('index')

