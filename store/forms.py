from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField(max_length=5000)

