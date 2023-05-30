from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    is_foster = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email

ANIMAL_CHOICES = (
    ("Dog", "Dog"),
    ("Cat", "Cat")
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=24, blank=True)
    last_name = models.CharField(max_length=24, blank=True)
    occupation = models.CharField(max_length=40, blank=True)
    age = models.IntegerField(default = 0, blank = True)
    phone_number = PhoneNumberField(blank=True)
    
    def __str__(self):
        return self.user.username


class Pet(models.Model):
    name = models.CharField(max_length=30)
    animal_type = models.CharField(max_length=20, choices=ANIMAL_CHOICES, default='Dog')
    breed_type = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=30, default='Unknown')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, default="default.jpg")
    interested = models.ManyToManyField(User, related_name='interested_pets',blank = True)
    applicants = models.ManyToManyField(User, related_name='applicants_pets',blank = True)
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


class PetApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE,blank=True, null=True) 
    message = models.TextField(max_length=200,blank=True, null=True)

    def __str__(self):
        return f'User: {self.user.id}, pet: {self.pet.id}'