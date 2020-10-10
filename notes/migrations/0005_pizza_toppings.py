# Generated by Django 3.0.5 on 2020-09-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20200907_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_topping', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_pizza', models.CharField(max_length=100)),
                ('toppings', models.ManyToManyField(help_text='Add your toppings', to='notes.Toppings')),
            ],
        ),
    ]