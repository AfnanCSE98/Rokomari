from django.urls import path, include
from . import views

app_name = "RC"
urlpatterns = [
    path('giveRating/<str:product_id>', views.give_rating, name='give_rating'),
    path('addComment/<str:product_id>', views.add_comment, name='add_comment')
]