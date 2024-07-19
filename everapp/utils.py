
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string

def notify_users(property, property_url):
    users = User.objects.all()  # Get all users (you may want to filter this)
    subject = 'New Property Added!'
    message = render_to_string('property_added_email.html', {
        'property': property,
        'property_url': property_url,
    })
    for user in users:
        send_mail(subject, message, 'wwwstephen95live@gmail.com', [user.email], html_message=message)