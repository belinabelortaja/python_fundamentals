from django.db import models
import re
import bcrypt
from dateutil.relativedelta import relativedelta
from datetime import datetime
import dateutil.parser
from login_registration_app.models import *

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 0:
            errors["title"] = "Book must have a title"
        if len(postData['description']) <= 5:
            errors["description"] = "Book description should be at least 10 characters"
        return errors

class Book(models.Model):
    title= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="books", on_delete =models.CASCADE)
    favorite_book = models.ManyToManyField(User, related_name="fav_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= BookManager()
    


