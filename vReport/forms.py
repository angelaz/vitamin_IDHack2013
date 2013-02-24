from django import forms
from vReport.models import *

class IndividualReporterForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=50)

class UserProfileReporterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput())
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=50)
    target_small = forms.IntegerField(label="6-11 months target:")
    target_big = forms.IntegerField(label="12-59 months target:")
    target_dewormed = forms.IntegerField(label="12-59 months de-worming target:")