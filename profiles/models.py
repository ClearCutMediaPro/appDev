from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    """ From django user profile we are creating a OnetoOneField which in turn
    merges our user profile with the django one."""
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    def  __str__(self): # this command ensure that the title is displayed correctly in the backend
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
        
    """ Create a new Profile() object when Django User is created """
    
    if created:
        Profile.objects.create(user=instance)