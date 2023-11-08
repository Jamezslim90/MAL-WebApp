from django.contrib import admin
from .models import Project, ProjectFacility, ProjectPhoto, Category



@admin.register(ProjectPhoto)
class ProjectPhotoeAdmin(admin.ModelAdmin):
    list_display = ['project', 'image']

class ProjectPhotoInline(admin.StackedInline): # new
   model = ProjectPhoto



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
   
   list_display = ['name', 'category','location', 'status']
   inlines = [
            ProjectPhotoInline,
]

   
@admin.register(ProjectFacility)
class ProjectFacilityAdmin(admin.ModelAdmin):
     list_display = ['name',]


   
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
     list_display = ['name',]
    