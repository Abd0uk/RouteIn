from .models import Goals
from django import forms


class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['title', 'desired_date', 'notes']
        widgets = {
            'desired_date': forms.DateInput(attrs={'type': 'date'})
        }