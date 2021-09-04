from django import forms
from commonuser.models import CommonUserModel
from django.core import validators

class CommonUserForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = CommonUserModel
        fields = ('is_jewler_request','address')
        widgets = {
            'address': forms.Textarea(attrs={'class':'uk-textarea fHarmattan','rows':'3','placeholder':'آدرس','id':'text','style':'display:none;color:#c7a046;background-color:#212121;'}),
            'is_jewler_request': forms.CheckboxInput(attrs={'class': 'uk-checkbox','id':'is_jewler_request','id':'myCheck', 'onclick':'myFunction()'}),
        }


class ConfirmationForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'کد ارسالی به شماره تلفن','id': 'code',}))
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
