from django import forms
from .models import Personne

class PersonneForm(forms.ModelForm):

    class Meta :
        model = Personne
        fields= '__all__'