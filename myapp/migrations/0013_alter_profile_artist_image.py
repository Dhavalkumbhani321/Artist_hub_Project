# Generated by Django 4.2.5 on 2023-09-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_profile_artist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='artist_image',
            field=models.ImageField(upload_to='artis/'),
        ),
    ]
