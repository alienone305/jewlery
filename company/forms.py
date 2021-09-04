from django import forms
from company.models import ContactUsModel

class ContactUsForm(forms.ModelForm):
    class Meta():
        model = ContactUsModel
        fields = ('name','phone_number','request')
        widgets = {
            'name': forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan goldC-text','placeholder':'نام (اختیاری)'},),
            'phone_number': forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'شماره تماس (اختیاری)'},),
            'request': forms.Textarea(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-textarea fHarmattan','rows':'4','placeholder':'متن درخواست یا پیشنهاد یا انتقاد'},),


        }
