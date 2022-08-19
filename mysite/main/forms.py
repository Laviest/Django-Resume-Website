from django import forms
from django.forms import Textarea, ModelForm
from .models import Question


class CreateNewQuestion(forms.ModelForm):
    question = forms.CharField(label="", required=False, max_length=200, widget=Textarea(attrs={'rows': 1, 'cols': 55}))

    class Meta:
        model = Question
        fields = ('name',)
