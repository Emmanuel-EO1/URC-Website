from django import forms
from .models import Inquiry

class ContactForm(forms.ModelForm):
    message= forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Your detailed message...'}))

    class Meta:
        model= Inquiry
        fields=['property', 'name', 'email', 'phone', 'message']
        # widgets= {
        #     'property': forms.HiddenInput(),
        # }
