from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel
from django.core import validators
from django.contrib.auth.forms import AuthenticationForm

class UserForm(UserCreationForm):
    '''form for creating a user'''


    terms = forms.BooleanField(
    error_messages={'required': 'لطفا شرایط و قوانین سایت را مطالعه کرده و تیک موافقت را بزنید'},
    widget=forms.CheckboxInput(attrs={'class': 'uk-checkbox'})
    )

    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan goldC-text','placeholder':'نام کاربری','id':'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan goldC-text','placeholder':'رمز عبور','id':'password1'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan redC-text','placeholder':'تکرار رمز عبور'
        }))

    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username','name','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan','placeholder':'نام کاربری','id':'username'},),
            'name': forms.TextInput(attrs={'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan','placeholder':'نام و نام خانوادگی','id':'name'},),
        }


class UserLoginForm(AuthenticationForm):


    username = forms.CharField(widget=forms.TextInput(
        attrs={'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan goldC-text','placeholder':'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'style':'background-color:#212121;color:#c7a046;',
'class':'uk-input fHarmattan goldC-text','placeholder':'رمز عبور'
        }
))
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = UserModel
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'id':'name'}),
        }


class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan','placeholder':'رمز فعلی','id':'current_password'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan','placeholder':'رمز جدید','id':'new_password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan','placeholder':'تکرار رمز جدید','id':'confirm_password'}))
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])


class ForgotPasswordForm(forms.Form):
    phone_number = forms.CharField(required = True, widget=forms.TextInput(attrs={'style':'background-color:#212121;color:#c7a046;','class':'uk-input fHarmattan','placeholder':'مثال 09141234567','id':'username'}))
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
