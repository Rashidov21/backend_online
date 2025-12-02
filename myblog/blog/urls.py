from django.urls import path 
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.homePage, name="home"),
    path("post/<int:post_id>/", views.postDetail, name="post_detail"),
    path("posts/", views.postList, name="post_list"),
    path("categories/", views.postCategories, name="post_categories"),
    path("category/<str:category_name>/posts", views.categoryPosts, name="category_posts"),
    path("contact/", views.contact, name="contact"),
]
