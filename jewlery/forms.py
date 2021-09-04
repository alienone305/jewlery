from django import forms
from django.forms import ValidationError
from django.core import validators
from jewlery.models import JewleryModel, JewleryPictureModel, UnitModel


class JewleryForm(forms.ModelForm):

    class Meta:
        model = JewleryModel
        fields = ('name','made_in','company_name','karat','weight','buy_wage','sale_wage','wholesale_wage','is_womanly','is_unisex',
        'is_used','is_domestic','is_available','is_confirmed','is_favorite',
        'is_goldset','is_pendant','is_bracelet','is_necklace','is_bangle','is_chain','is_earings','is_halfset','is_watch','is_anklet')
        widgets = {
            'name': forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'نام  محصول'},),
            'made_in': forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'ساخت کشور'},),
            'company_name': forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'شرکت سازنده'},),
            'karat': forms.NumberInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'عیار'},),
            'weight': forms.NumberInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'وزن'},),
            'buy_wage': forms.NumberInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'اجرت خرید'},),
            'sale_wage': forms.NumberInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'اجرت فروش'},),
            'wholesale_wage': forms.NumberInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'اجرت فروش عمده'},),

            'is_womanly': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_unisex': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_used': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_domestic': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_available': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_confirmed': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_favorite': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),

            'is_goldset': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_pendant': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_bracelet': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_necklace': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_bangle': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_chain': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_earings': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_halfset': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_watch': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
            'is_anklet': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),

        }


class JewleryPictureForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = JewleryPictureModel
        fields = ('picture',)



class JewleryPictureUpdateForm(forms.ModelForm):
    Hfield = forms.CharField(required=False,widget =forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = JewleryPictureModel
        fields = ('picture',)
        widgets = {
            'picture': forms.FileInput(attrs={},),
        }


class UnitForm(forms.ModelForm):

    class Meta():
        model = UnitModel
        fields = ('unit','auto_update')
        widgets = {
        'unit': forms.TextInput(attrs={'style':'color:#c7a046;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'فی به ریال','onkeyup':'format(this)'},),
        'auto_update': forms.CheckboxInput(attrs={'style':'color:#c7a046;background-color:#212121;','class': 'uk-checkbox'}),
        }
