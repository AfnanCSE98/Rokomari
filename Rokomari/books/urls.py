from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    #path('', views.index, name='index'),
    #path('home/', views.home , name='home'),
    #path('signup/', views.signup, name='signup'),
    #path('cart/', views.cart, name='cart'),
    #path('order/', views.order, name='order'),
    #path('order/<int:order_id>/', views.specificOrder, name='specificOrder'),
    #path('allOrder/', views.allOrder, name='allOrder'),
    #path('cart/<str:book_id>/', views.delete_Cart_Item, name='delete_Cart_Item'),
    path('book-category/', views.book_category, name='book_category'),
    path('book-category/<int:ctg_id>/', views.book_category_details, name='book_category_details'),
    path('book/<str:book_id>/', views.book_details, name='book_details'),
    #path('add/<str:book_id>/', views.addToCart, name='addToCart'),
    path('author/', views.book_author, name='book_author'),
    path('author/<int:author_id>/', views.book_author_details, name='book_author_details'),
    path('publisher/', views.book_publisher, name='book_publisher'),
    path('publisher/<int:pub_id>', views.book_publisher_details, name='book_publisher_details'),
    #path('user-profile', views.user_profile, name='user_profile'),
    #path('giveRating/<str:book_id>', views.giveRating, name='giveRating'),
    #path('addComment/<str:book_id>', views.addComment, name='addComment')
]