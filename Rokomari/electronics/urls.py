from django.urls import path
from . import views

app_name = "electronics"
urlpatterns = [
    path('electronics-category/', views.electronics_category, name='electronics_category'),
    path('electronics-category/<int:ctg_id>/', views.electronics_category_details, name='electronics_category_details'),
    path('electronics/<str:electronics_id>/', views.electronics_details, name='electronics_details'),
    path('brand/', views.electronics_brand, name='electronics_brand'),
    path('brand/<int:brand_id>', views.electronics_brand_details, name='electronics_brand_details')
]