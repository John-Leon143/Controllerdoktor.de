"""
URL configuration for controllerdoktor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# In /var/www/controllerdoktor/controllerdoktor/urls.py
from django.contrib import admin
from django.urls import path, include  
from django.contrib.sitemaps.views import sitemap
from homepage.sitemaps import StaticViewSitemap
from homepage.sitemaps import BlogPostSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogPostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('homepage.urls')),
    path('blog/', include('blog.urls')),
    path("minecraft/", include("minecraft_console.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap')  
]

