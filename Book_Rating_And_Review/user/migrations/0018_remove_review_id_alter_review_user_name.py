# Generated by Django 5.1.1 on 2024-10-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_review_review_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='id',
        ),
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
