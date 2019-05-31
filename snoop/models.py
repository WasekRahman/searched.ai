from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

		

class ReportPost(models.Model):
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='images/')
	age = models.IntegerField()
	address = models.TextField()
	last_seen = models.CharField(max_length=100)
	contact = models.IntegerField()
	details = models.TextField(default='N/A')
	date_posted = models.DateTimeField(auto_now_add=True)
	posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)



	def __str__(self):
		return 'Case : ' + self.name

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})	



class SawPost(models.Model):
	name = models.CharField(max_length=100,default='N/A')
	photo = models.ImageField(upload_to='imagesunknown/')
	last_seen = models.CharField(max_length=100)
	contact = models.CharField(max_length=100)
	details = models.TextField(default='N/A')
	date_posted = models.DateTimeField(auto_now_add=True)
	posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)



	def __str__(self):
		return 'Case : ' + self.name

	def get_absolute_url(self):
		return reverse('sawpost-detail',kwargs={'pk':self.pk})			