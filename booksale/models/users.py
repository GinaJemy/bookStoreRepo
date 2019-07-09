from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_CHOICES = [('Buyer','Buyer'),('Seller','Seller')]
    userType = models.CharField(max_length=100, blank=True, choices=USER_CHOICES, default='Buyer')

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

