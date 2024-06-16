from django import forms
from .models import FeedbackForm

class FeedbackFormForm(forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = ['description']
