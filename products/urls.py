from django.urls import path
from .views import  ProductListView, ProductDetailView

urlpatterns = [
path('product/', ProductListView.as_view() , name='product_listing'),
# path('product/<int:pk>/', ProductDetailView.as_view() , name='product_detail'),

]