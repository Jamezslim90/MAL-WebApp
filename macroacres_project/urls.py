"""PGHomes_website URL Configuration

"""
from django.conf import settings # new
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    # path('products/', include('products.urls')),
    path('team/', include('team.urls')),
    path('', include('pages.urls'))


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)