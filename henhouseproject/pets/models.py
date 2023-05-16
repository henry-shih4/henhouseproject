from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    pass



ANIMAL_CHOICES = (
    ("Dog", "Dog"),
    ("Cat", "Cat")
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


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



class Foster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email
    


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(post_user_created_signal, sender=User)