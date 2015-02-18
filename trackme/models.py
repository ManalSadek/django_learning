from django.db import models

from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS
from django.core.files.images import ImageFile
# Create your models here.


class User(models.Model):
	username = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	password = models.CharField(max_length=20)
	reports = models.IntegerField(default=0)
	profilePicture = models.ImageField(upload_to='profilePictures')
	def __str__(self):
		return self.username
	def clean(self):
		if len(self.password) < 8 :
			raise ValidationError('Use more complex password')
	def validate_unique(self, *args, **kwargs):
		if not self.id:
			if self.__class__.objects.filter(email=self.email).exists():
				raise ValidationError(
					{
					NON_FIELD_ERRORS:
					('Person with same email already exists.')
					}
				)
	