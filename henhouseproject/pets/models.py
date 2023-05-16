from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ANIMAL_CHOICES = (
    ("Dog", "Dog"),
    ("Cat", "Cat")
)

class Pet(models.Model):
    name = models.CharField(max_length=30)
    animal_type = models.CharField(max_length=20, choices=ANIMAL_CHOICES, default='Dog')
    breed_type = models.CharField(max_length=20)
    age = models.IntegerField(default = 0)
    city = models.CharField(max_length=30, default='Unknown')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, default="default.jpg")
    interested = models.ManyToManyField(User, related_name='interested_pets')
    foster = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):
        return self.name

