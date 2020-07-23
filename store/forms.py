from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """Review form"""
    class Meta:
        model = Review
        fields = ("name", "email", "text")

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField(max_length=5000)
