from django.db import models
from datetime import datetime
import dateutil.parser
from login_registration_app.models import *
from django.core.exceptions import ValidationError
from django import forms
from django.utils import timezone

class TravelManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['destination']) < 1:
            errors["destination"] = "Destination field should be at least 2 characters"
    def clean(self):
        super().clean()
        if not (timezone.now() <= self.startdate <= self.end_date):
            raise ValidationError('Invalid start and end datetime')

class Travel(models.Model):
    destination = models.CharField(max_length=255)
    plan = models.CharField(max_length=255)
    startdate = models.DateTimeField()
    end_date = models.DateTimeField()
    user= models.ManyToManyField(User, related_name="travels")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()

