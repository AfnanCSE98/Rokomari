from django.urls import path, include
from . import views

app_name = "home"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('user-profile', views.user_profile, name='user_profile'),
    path('admin', views.admin, name='admin'),
    path('add-electronics', views.add_electronics, name='add_electronics'),
    path('update-electronics', views.update_electronics, name='update_electronics'),
    path('add-brand', views.add_brand, name='add_brand'),
    path('add-electronics-category', views.add_electronics_category, name='add_electronics_category'),
    path('', include('books.urls')),
    path('', include('electronics.urls')),
    path('', include('CWO.urls')),
    path('', include('RC.urls')),
    path('', include('search_query.urls'))
]