# Generated by Django 5.1.1 on 2024-10-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_pics/profile.png', null=True, upload_to='profile_pics/'),
        ),
    ]
