from django.urls import path
from . import views

app_name = "CWO"
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('order/', views.order, name='order'),
    path('order/<int:order_id>/', views.specific_order, name='specific_order'),
    path('allOrder/', views.all_order, name='all_order'),
    path('cart/<str:product_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('wishlist/<str:product_id>/', views.delete_wishlist_item, name='delete_wishlist_item'),
    path('addc/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('addw/<str:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('update_cart/<str:product_id>/', views.update_cart, name='update_cart')
]
