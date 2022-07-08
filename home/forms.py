from django import forms
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy


class PyularForm(forms.Form):
 

    expression = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Python Regular Expression',
            'class': 'm-2 form-control'
        })
    )

    sample = forms.CharField(
        max_length=4000,
        widget=forms.Textarea(               
        attrs={
            'placeholder': 'Enter sample text',
            'class': 'm-2 form-control'
        })
    )
