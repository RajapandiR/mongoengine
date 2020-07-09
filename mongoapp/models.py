from django.db import models
from mongoengine import Document, fields
# Create your models here.

class Profile(Document):
	name = fields.StringField(max_length=200, null=True)
	age = fields.IntField(null=True)

	def __str__(self):
		return self.name