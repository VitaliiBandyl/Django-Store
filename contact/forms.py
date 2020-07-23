from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Email subscription form"""

    class Meta:
        model = Contact
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "input", "placeholder": "Your Email..."})
        }
        labels = {
            "email": ''
        }