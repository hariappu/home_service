from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm

from home_web.models import Userprofile,Job






class Userprofileform(forms.ModelForm):
    class Meta:

        model=Userprofile
        fields=["profile_pic","skill","address","location","phone_number"]