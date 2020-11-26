from django.urls import path, include
from . import views

app_name = "home"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('user-profile', views.user_profile, name='user_profile'),
    path('', include('books.urls')),
    path('', include('electronics.urls')),
    path('', include('CWO.urls')),
    path('', include('RC.urls'))
]