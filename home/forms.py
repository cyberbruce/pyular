from tkinter.tix import Form
from django import forms
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy


class PyularForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse_lazy('home')
        self.helper.form_show_labels=False
        self.helper.attrs = {
            'hx-post': reverse_lazy('home'),
            'hx-target': '#pyular-form',
            'hx-trigger': 'submit, input keyup delay:500m'
        }

    expression = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Python Regular Expression'
        })
    )

    sample = forms.CharField(widget=forms.Textarea(        
        attrs={
            'placeholder': 'Enter sample text'
        })
    )
