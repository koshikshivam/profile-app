from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created: 
        created = Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=Profile)
def do_something_when_user_updated(sender, instance, created, **kwargs):
    if created:
        user1 = User.objects.get(username=instance.user)
        user_obj = instance
        send_mail(f"your profile is created", f'{user1.username},your user name is',
                  'testsmtpintelsafe@gmail.com', [user1.email], fail_silently=False)
    else:
        user1 = User.objects.get(username=instance.user)

        user_obj = instance
        send_mail(f"your profile is update", f'{user1.username}',
                  'testsmtpintelsafe@gmail.com', [user1.email], fail_silently=False)
