from django.db import models
from django.urls import reverse

# Create your models here.
class Color(models.Model):
	name = models.CharField(max_length =20)
	is_favorited = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering =['name']
