from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from .models import Category,Comment,Post
# Create your views here.

# controller method 
def homePage(request):
    posts = Post.objects.filter(published=True)
    return render(request, template_name="index.html", context={"posts":posts})

# controller class 
# class HomePageView(TemplateView):
#     template_name = "index.html"