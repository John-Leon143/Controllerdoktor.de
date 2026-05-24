# In minecraft_console/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("console/", views.console_view, name="console_view"),  # Zeigt die Konsole
    path("send_command/", views.send_command, name="send_command"),  # Sendet Befehle
]
