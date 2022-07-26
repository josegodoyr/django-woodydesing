from dataclasses import field
import imp
from operator import ipow
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')

        }