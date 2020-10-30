from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Customer, Order, Product
from django.contrib.auth.models import Group
from django.db import models
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
    	group 		=	Group.objects.get(name='sellers')
    	Customer.objects.create(User=instance)
    	instance.groups.add(group)
    	instance.customer.save()