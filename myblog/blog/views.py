from django.shortcuts import render ,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from .models import Category,Comment,Contact,Post
# Create your views here.

# controller method 
def homePage(request):
    posts = Post.objects.filter(published=True)
    return render(request, template_name="index.html", context={"posts":posts})


def postDetail(request,post_id):
    post = Post.objects.get(id=post_id)
    # comments = post.comments.all()
    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        if name and comment:
            Comment.objects.create(name=name,comment=comment,post=post)
            messages.success(request, "Firk saqlandi !")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Xatolik !")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
    return render(request, template_name="post_detail.html", context={"post":post})

def postList(request):
    posts = Post.objects.filter(published=True)
    return render(request, template_name="post_list.html",context={"posts":posts})


def postCategories(request):
    categories = Category.objects.all()
    return render(request, template_name="category_list.html", context={"categories":categories})

def categoryPosts(request,category_name):
    category = Category.objects.get(name=category_name)
    posts = category.posts.all()
    return render(request, template_name="post_list.html", context={"posts":posts})
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if all([name,email,message]):
            Contact.objects.create(name=name,email=email,message=message)
            messages.success(request, "Xabar saqlandi !")
            return redirect("/contact/")
        else:
            messages.error(request, "Xabar yuborilmadi, iltimos formani to'g'ri to'ldiring !")
            return redirect("/contact/")
    return render(request, template_name="contact.html")

