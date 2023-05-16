from django import forms
from pets.models import Foster

class FosterModelForm(forms.ModelForm):
    class Meta:
        model = Foster
        fields = (
            'user',
        )