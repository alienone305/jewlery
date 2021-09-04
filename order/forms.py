from django import forms
from order.models import OrderModel

class OrderForm(forms.ModelForm):
    class Meta():
        model = OrderModel
        fields = ('description','weight','numbers','name','address','phone_number',)
        widgets = {
        'name': forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','id':'name'},),
        'description': forms.Textarea(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-textarea fHarmattan','rows':'3',},),
        'phone_number': forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan',},),
        'numbers': forms.NumberInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan',},),
        'weight': forms.NumberInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan',},),
        'address': forms.Textarea(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-textarea fHarmattan','rows':'3','required':'true'},),
}
