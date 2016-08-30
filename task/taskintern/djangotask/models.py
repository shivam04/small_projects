from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def upload_loaction(instance, filename):
	return str(instance.user.username)+"/"+filename

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	age = models.IntegerField(blank=True)
	picture = models.ImageField(upload_to=upload_loaction, 
		null=True,blank=True,
		height_field="height_field",width_field="width_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	gender = models.CharField(max_length=10,default="Male")
	
	def __unicode__(self):
	    return self.user.username
