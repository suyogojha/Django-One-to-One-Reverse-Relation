from .models import *
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Page)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()
    
    
    
    #now in apps.py