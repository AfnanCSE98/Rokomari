from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "books"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/' , views.home , name='home'),
    path('signup/', views.signup, name='signup'),
    path('book-category/' , views.book_category , name='book_category'),
    path('book-category/<int:ctg_id>/', views.book_category_details, name='book_category_details'),
    path('author/' , views.book_author , name = 'book_author'),
    path('author/<int:author_id>/' , views.book_author_details , name='book_author_details'),
    path('publisher/' , views.book_publisher , name = 'book_publisher'),
    path('publisher/<int:pub_id>' , views.book_publisher_details , name = 'book_publisher_details'),
    path('user-profile' , views.user_profile , name='user_profile')
]