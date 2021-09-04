from django import forms
from masteruser.models import MasterUserModel
from django.core import validators


class MasterUserForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = MasterUserModel
        fields = ('logs',)
