from django.forms import ModelForm
from django import forms
from .models import Pet, UserProfile, PetApplication
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'animal_type', 'breed_type', 'age', 'city', 'description', 'image']
        

class myUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class PetApplicationForm(forms.ModelForm):
    class Meta:
        model = PetApplication
        fields = ["message"]

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name","occupation", "age", "phone_number"]