from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Team, Text, Designation



@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['paragraph',]

class TextInline(admin.StackedInline): # new
   model = Text


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
  
  list_display = ['name', 'title','designation',]
  inlines = [
            TextInline,
]

@admin.register(Designation)
class FeaturesAdmin(admin.ModelAdmin):
     list_display = ['name',]