from django.urls import path, include # type: ignore
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='home'),  #link zur Homepage
    #path('index.html', views.index, name='home'),  #link zur Homepage
    path('reperatur-anfragen/', views.reperaturanfragen, name='reperatur-anfragen'), #fomular 
    path('dienstleitungen/', views.dienstleitungen, name='dienstleitungen'),
    path('kontakt/', views.kontakt, name='kontakt'),
    
    path('blog/', include('blog.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
