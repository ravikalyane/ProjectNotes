# Generated by Django 3.0.5 on 2020-09-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, default=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.CharField(default='CS', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='someone@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Mumbai', max_length=100),
        ),
    ]
