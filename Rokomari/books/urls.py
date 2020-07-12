from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "books"
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]