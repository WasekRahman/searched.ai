from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ReportPost,SawPost
from django.apps import apps
from django.contrib.auth.models import User
from django.shortcuts import redirect
import face_recognition
from PIL import Image, ImageDraw
from .imagematch import image_search
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

matched = []
models = {
    model.__name__: model for model in apps.get_models()
}
print(models['ReportPost'])
for reportposts in ReportPost.objects.all():
    for sawposts in SawPost.objects.all():
        sawposts.name = 'Hello'
        print(sawposts.details)

import glob

for filepath in glob.iglob('my_dir/*.asm'):
    print(filepath)
        

def matched(request):
	report = ReportPost.objects.all()
	saw = SawPost.objects.all()
	context = {
	'saw': saw,
	'report':report,
	}
	return render(request, 'snoop/matched.html', context)


class PostListView(LoginRequiredMixin,ListView):
	model = ReportPost
	template_name = 'snoop/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin,DetailView):
	model = ReportPost

class PostCreateView(LoginRequiredMixin,CreateView):
	model = ReportPost
	fields = ["name","photo","age","address","last_seen","contact","details"]
	def form_valid(self,form):
        
		form.instance.posted_by = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ReportPost
    fields = ["name","photo","age","address","last_seen","contact","details"]

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ReportPost
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        return False        
class UserPostListView(ListView):
    model = ReportPost
    template_name = 'snoop/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class SawPostListView(LoginRequiredMixin,ListView):
    model = SawPost
    template_name = 'snoop/suspects.html'
    context_object_name = 'sawposts'
    ordering = ['-date_posted']

class SawPostDetailView(LoginRequiredMixin,DetailView):
    model = SawPost

class SawPostCreateView(LoginRequiredMixin,CreateView):
    model = SawPost
    fields = ["name","photo","last_seen","contact","details"]
    def form_valid(self,form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class SawPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SawPost
    fields = ["name","photo","last_seen","contact","details"]

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        return False

class SawPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SawPost
    success_url = '/snoop/suspects.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        return False


def about(request):
	if request.user.is_authenticated:
		return render(request,'snoop/about.html')
	else:
		return redirect('/accounts/login/')

def announcements(request):
	if request.user.is_authenticated:
		return render(request,'snoop/announcements.html')
	else:
		return redirect('/accounts/login/')			

def suspects(request):
	if request.user.is_authenticated:
 		return render(request,'snoop/suspects.html')
	else:
		return redirect('/accounts/login/')
      