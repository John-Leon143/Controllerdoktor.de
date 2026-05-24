# In minecraft_console/views.py

from django.shortcuts import render
from django.http import JsonResponse
from mcrcon import MCRcon
from django.views.decorators.csrf import csrf_exempt

# Minecraft-Server-Konfiguration
MC_SERVER_IP = "127.0.0.1"  # IP des Minecraft-Servers
MC_RCON_PORT = 25575        # RCON-Port des Servers
MC_RCON_PASSWORD = "Philipp1"

@csrf_exempt
def send_command(request):
    """
    Diese Funktion empfängt POST-Anfragen und sendet den Minecraft-Befehl
    über RCON an den Server, wobei die Rückmeldung zurückgegeben wird.
    """
    if request.method == "POST":
        command = request.POST.get("command")

        if command:
            try:
                with MCRcon(MC_SERVER_IP, MC_RCON_PASSWORD, port=MC_RCON_PORT) as mcr:
                    response = mcr.command(command)
                return JsonResponse({"status": "success", "output": response})
            except Exception as e:
                return JsonResponse({"status": "error", "error": str(e)})
        else:
            return JsonResponse({"status": "error", "error": "No command provided"})
    else:
        return JsonResponse({"status": "error", "error": "POST request required"})

def console_view(request):
    """
    Diese Funktion rendert das HTML-Template für die Minecraft-Server-Konsole.
    """
    return render(request, 'minecraft_console/console.html')

