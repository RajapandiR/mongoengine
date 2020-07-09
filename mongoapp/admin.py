from django.contrib import admin
from django_mongoengine import  mongo_admin as mongo
# Register your models here.

from mongoapp import models

mongo.site.register(models.Profile)
