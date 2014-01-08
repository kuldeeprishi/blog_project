from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	"""user profile model"""
        user=models.OneToOneField(User)
        
        def __unicode__(self):
                return self.First_name

