from django import forms
from .models import Cat

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'breed', 'nicknames', 'emoji_preference', 'color', 'tail', 'age', 'magical_properties', 'image']
