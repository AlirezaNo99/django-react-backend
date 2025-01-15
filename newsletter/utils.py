from django.core.mail import send_mass_mail
from .models import Subscriber
from django.conf import settings

def send_newsletter(subject, message):
    """
    Sends a newsletter email to all active subscribers.
    """
    subscribers = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    if not subscribers:
        return "No active subscribers found."

    emails = [(subject, message, settings.DEFAULT_FROM_EMAIL, [email]) for email in subscribers]
    send_mass_mail(emails)
    return f"Newsletter sent to {len(subscribers)} subscribers."
