from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from fragmantica import settings
from fragmantica.accounts.models import FragUser

UserModel=get_user_model()

@receiver(signal=post_save, sender=FragUser)
def send_greeting_email(sender, instance, created, **kwargs):
    if created:
        subject = "Registration greetings from Fragmantica"
        html_message = render_to_string('email-greeting.html', {'user': instance})
        plain_message = strip_tags(html_message)
        to = instance.email
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to], html_message=html_message
        )
