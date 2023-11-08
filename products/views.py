from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Product



class ProductListView (ListView):
    model: Product
    context_object_name = 'product_list' 

    template_name= 'products/product_listings.html'

    def get_queryset(self):
          return Product.objects.order_by('pk')




class ProductDetailView (DetailView):
    model: Product
    context_object_name = 'product' 
    template_name = 'products/product_detail.html'

    def get_queryset(self):
          return Product.objects.order_by('pk')
        