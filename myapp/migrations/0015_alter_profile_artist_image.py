# Generated by Django 4.2.5 on 2023-09-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_profile_artist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='artist_image',
            field=models.ImageField(upload_to='myapp/static/img/artist'),
        ),
    ]
