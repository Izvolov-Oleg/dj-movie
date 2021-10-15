from django import forms

from .models import Reviews

class ReviewForm(forms.ModelForm):
    """Офрма отзыва"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
