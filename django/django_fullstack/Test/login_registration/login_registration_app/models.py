from django.db import models
import re
import bcrypt
from dateutil.relativedelta import relativedelta
from datetime import datetime
import dateutil.parser

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstname']) < 2:
            errors["firstname"] = "First name should be at least 2 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData["password"] != postData['conf_password']:
            errors['password'] = 'Passwords do not match'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):      
            errors['email'] = ("Invalid email address!")
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use"
        years_ago = datetime.now() - relativedelta(years=16)
        if dateutil.parser.parse(postData['birthdate']) >= years_ago:
            errors['birthdate'] = 'You must be more than 16 years old'
        return errors

    def login(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        if existing_user is None:
            errors['email'] = "User does not exist."
        if len(postData['email']) == 0:
            errors['email'] = "Email must be entered"
        if len(postData['password']) < 8:
            errors['password'] = "An eight character password must be entered"
        if bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['mismatch'] = "Email and password do not match"
        return errors


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    friends= models.ManyToManyField("self", related_name="friends")
    password = models.CharField(max_length=255)
    birthdate = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
