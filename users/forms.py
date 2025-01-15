from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

class CustomPasswordResetForm(PasswordResetForm):
    def save(self, domain_override=None, subject_template_name=None,
             email_template_name=None, use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None, extra_email_context=None):
        UserModel = get_user_model()
        email = self.cleaned_data["email"]
        active_users = UserModel.objects.filter(email=email, is_active=True)
        for user in active_users:
            context = {
                "email": email,
                "domain": domain_override or request.get_host(),
                "site_name": "Your Site",
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": token_generator.make_token(user),
                "protocol": "https" if use_https else "http",
            }
            reset_url = f"{context['protocol']}://{context['domain']}/reset-password/{context['uid']}/{context['token']}/"
            send_mail(
                subject="Reset Your Password",
                message=f"Click the link to reset your password: {reset_url}",
                from_email=from_email,
                recipient_list=[email],
            )
