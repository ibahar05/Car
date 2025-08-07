from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, Location

@receiver(post_save, sender= User)
def create_user_prpfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance) 


@receiver(post_save, sender= Profile)
def create_profile_location(sender, instance, created, **kwargs):
    if created:
        Profile_location = Location.objects.create()
        instance.location = Profile_location
        instance.save()


 