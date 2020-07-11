from rest_framework_mongoengine import serializers
from rest_framework import fields

from mongoapp import models

class ProfileSerializer(serializers.DocumentSerializer):
	name = fields.CharField(required=False)
	age = fields.IntegerField(required=False)
	class Meta:
		model = models.Profile
		fields = ['id', 'name', 'age']