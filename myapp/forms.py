from django import forms
from django.db import models
from django.forms import fields
from .models import signupMaster,uploadPost

class signupForm(forms.ModelForm):
    class Meta:
        model=signupMaster
        fields='__all__'

class postForm(forms.ModelForm):
    class Meta:
        model=uploadPost
        fields='__all__'