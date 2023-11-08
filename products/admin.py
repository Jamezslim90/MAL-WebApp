from django.contrib import admin
from .models import Product, Feature, ProductPhoto



@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']

class ProductPhotoInline(admin.StackedInline): # new
   model = ProductPhoto


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  
  list_display = ['name', 'specification','project','location', 'available_units']
  inlines = [
            ProductPhotoInline,
]

@admin.register(Feature)
class FeaturesAdmin(admin.ModelAdmin):
     pass