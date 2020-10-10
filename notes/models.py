from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Note(models.Model):
    title = models.CharField(max_length=50)
    note = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    pinned = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)


class Hello(models.Model):
    shirt_sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )
    name = models.CharField(max_length=100, help_text="this is the size of shirt", verbose_name='custom name')
    size = models.CharField(max_length=2, choices=shirt_sizes)

    def __str__(self):
        return self.name


class Toppings(models.Model):
    name_of_topping = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_topping


class Pizza(models.Model):
    name_of_pizza = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Toppings, help_text='Add your toppings')

    def __str__(self):
        return self.name_of_pizza


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True)
    is_legal = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.age < 18:
            self.is_legal = "Under Age"
            super().save(*args, **kwargs)
        else:
            self.is_legal = "18+"
            super().save(*args, **kwargs)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Personsssss'


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return self.person.name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, default=20)
    location = models.CharField(max_length=100, default='Mumbai')
    email = models.EmailField(default="someone@gmail.com")
    course = models.CharField(max_length=100, default='CS')
