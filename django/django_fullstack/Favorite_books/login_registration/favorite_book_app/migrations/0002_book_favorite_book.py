# Generated by Django 2.2 on 2021-05-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration_app', '__first__'),
        ('favorite_book_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorite_book',
            field=models.ManyToManyField(related_name='fav_books', to='login_registration_app.User'),
        ),
    ]
