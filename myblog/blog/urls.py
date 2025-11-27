from django.urls import path 
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.homePage, name="home"),
    # path("home", views.HomePageView.as_view(), name="home2"),
]
