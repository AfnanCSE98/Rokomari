from django.urls import path, include
from . import views

app_name = "home"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('user-profile', views.user_profile, name='user_profile'),
    path('admin', views.admin_login, name='admin_login'),
    path('admindashboard/', views.admin, name='admin'),
    path('add-electronics', views.add_electronics, name='add_electronics'),
    path('update-electronics', views.update_electronics, name='update_electronics'),
    path('add-brand', views.add_brand, name='add_brand'),
    path('add-electronics-category', views.add_electronics_category, name='add_electronics_category'),
    path('add-book' , views.add_book , name='add_book'),
    path('add-book-category' , views.add_book_category , name = 'add_book_category'),
    path('all-books' , views.all_books , name='all_books'),
    path('all-electronics' , views.all_electronics , name = 'all_electronics'),
    path('all-orders' , views.all_orders , name = 'all_orders'),
    path('add-author' , views.add_author , name = 'add_author'),
    path('add-publisher' , views.add_publisher , name = 'add_publisher'),
    path('', include('books.urls')),
    path('', include('electronics.urls')),
    path('', include('CWO.urls')),
    path('', include('RC.urls')),
    path('', include('search_query.urls'))
]