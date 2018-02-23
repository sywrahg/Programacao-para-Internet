from django.db import models

STATUS_REQUEST = (
		('APROVED', 'aprovado'),
		('REFUSED', 'recusado'),
		('WAITING', 'pendente'),
	)

REACT_KIND = (
		('LIKE', 'curtir'),
		('LOVE', 'amar'),
		('SAD', 'triste'),
		('IMPRESSED', 'impressionado'),
		('LAUGH', 'sorridente'),
	)


# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=20)
	user = models.ForeignKey('user.User',on_delete=models.CASCADE)	
	profile = models.ManyToManyField('Profile', through='FriendshipRequest')


class FriendshipRequest(models.Model):
	requester = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='meus_convites')
	requested = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='minhas_solicitacoes')
	status = models.CharField(max_length=20, choices=STATUS_REQUEST)


class Post(models.Model):
	text = models.CharField(max_length=400)
	date = models.DateField(auto_now=True)
	profile = models.ForeignKey('Profile', related_name='Timeline', on_delete=models.CASCADE) 
		

class Comment(models.Model):
	text = models.CharField(max_length=400)
	date = models.DateField(auto_now=True)
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)


class React(models.Model):
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
	date = models.DateField(auto_now=True)
	kind = models.CharField(max_length=20, choices=REACT_KIND)
	intensity = models.IntegerField()





		