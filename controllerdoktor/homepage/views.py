from django.core.mail import EmailMessage
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    return render(request, 'homepage/index.html')

def reperaturanfragen(request):
    if request.method == 'POST':
        # Formularwerte abrufen
        name = request.POST.get('name')
        email = request.POST.get('e-mail')  # E-Mail des Benutzers
        description = request.POST.get('discreption')

        # Betreff und Nachrichtentext definieren
        subject = f"Neue Reparaturanfrage von {name}"
        message = f"""
        Eine neue Reparaturanfrage wurde über das Formular gesendet:

        Name: {name}
        E-Mail: {email}
        Beschreibung:
        {description}
        """

        # E-Mail versenden
        try:
            email_message = EmailMessage(
                subject,
                message,
                'reparatur@controllerdoktor.de',  # Feste Absenderadresse
                ['reparatur@controllerdoktor.de'],  # Zieladresse (IONOS-Postfach)
               # reply_to=[email],  # Antwort-Adresse des Benutzers
            )
            email_message.send()
            messages.success(request, "Danke, Ihre Nachricht wurde erfolgreich gesendet.")
        except Exception as e:
            messages.error(request, f"Fehler beim Senden der Nachricht: {str(e)}")
    
    # Seite mit Formular rendern
    return render(request, 'homepage/reperatur-anfragen.html')



def blog(request):
    return render(request, 'homepage/blog.html')

def dienstleitungen(request):
    return render(request, 'homepage/dienstleitungen.html')

def kontakt(request):

    if request.method == 'POST':
        # Formularwerte abrufen
        name = request.POST.get('name')
        email = request.POST.get('e-mail')  # E-Mail des Benutzers
        description = request.POST.get('discreption')

        # Betreff und Nachrichtentext definieren
        subject = f"Neue Kontaktanfrage von {name}"
        message = f"""
        Eine neue Kontaktanfrage wurde über das Formular gesendet:

        Name: {name}
        E-Mail: {email}
        Beschreibung:
        {description}
        """

        # E-Mail versenden
        try:
            email_message = EmailMessage(
                subject,
                message,
                'reparatur@controllerdoktor.de',  # Feste Absenderadresse
                ['reparatur@controllerdoktor.de'],  # Zieladresse (IONOS-Postfach)
               # reply_to=[email],  # Antwort-Adresse des Benutzers
            )
            email_message.send()
            messages.success(request, "Danke, Ihre Nachricht wurde erfolgreich gesendet.")
        except Exception as e:
            messages.error(request, f"Fehler beim Senden der Nachricht: {str(e)}")
    
    return render(request, 'homepage/kontakt.html')