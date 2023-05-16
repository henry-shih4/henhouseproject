from django.forms import ModelForm
from .models import Pet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'animal_type', 'breed_type', 'age', 'city', 'description', 'image']
        

class myUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

