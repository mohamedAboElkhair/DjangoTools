from django import forms

from .models import Produ


class ProduForm(forms.ModelForm):
    class Meta:
        model = Produ
        fields = [
            'titel',
            'content',
            'price'
        ]