from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import  settings
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.
class Book(models.Model):
    owner = models.ForeignKey('auth.User',related_name = 'books',default =None, null =True)
    title= models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __unicode__(self):
        return  self.author
