from django.urls import path
from . import views

app_name = "search_query"

urlpatterns = [
    path('search/', views.search, name='search'),

]