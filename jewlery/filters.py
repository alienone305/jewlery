from jewlery.models import JewleryModel
import django_filters
from django import forms


class JewleryFilter(django_filters.FilterSet):

    CHOICES = (
            (True, "بله"),
            (False, "خیر"),
           )
    is_womanly =  django_filters.ChoiceFilter(choices=CHOICES,empty_label="زنانه",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', 'placeholder':'ss'}),field_name='is_womanly')
    is_used = django_filters.ChoiceFilter(choices=CHOICES,empty_label="طلای کهنه",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_used')
    is_domestic = django_filters.ChoiceFilter(choices=CHOICES,empty_label="تولید داخل",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_domestic')
    is_available = django_filters.ChoiceFilter(choices=CHOICES,empty_label="موجود",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_available')
#types
    is_goldset = django_filters.ChoiceFilter(choices=CHOICES,empty_label="سرویس کامل",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_goldset')
    is_pendant = django_filters.ChoiceFilter(choices=CHOICES,empty_label="مدال",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_pendant')
    is_bracelet = django_filters.ChoiceFilter(choices=CHOICES,empty_label="دستبند",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_bracelet')
    is_necklace = django_filters.ChoiceFilter(choices=CHOICES,empty_label="گردنبند",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_necklace')
    is_bangle = django_filters.ChoiceFilter(choices=CHOICES,empty_label="النگو",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_bangle')
    is_chain = django_filters.ChoiceFilter(choices=CHOICES,empty_label="زنجیر",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_chain')
    is_earings = django_filters.ChoiceFilter(choices=CHOICES,empty_label="گوشواره",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_earings')
    is_halfset = django_filters.ChoiceFilter(choices=CHOICES,empty_label="نیم ست",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_halfset')
    is_watch = django_filters.ChoiceFilter(choices=CHOICES,empty_label="ساعت",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_watch')
    is_anklet = django_filters.ChoiceFilter(choices=CHOICES,empty_label="پابند",widget=forms.NullBooleanSelect(attrs={'style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan', }),field_name='is_anklet')


    weight__gte = django_filters.NumberFilter(widget=forms.TextInput(attrs={'id': 'weight__gte','style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'وزن طلا بیشتر از (گرم)'}),field_name='weight', lookup_expr='gte')
    weight__lte = django_filters.NumberFilter(widget=forms.TextInput(attrs={'id': 'weight__lte','style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'وزن طلا کمتر از (گرم)'}),field_name='weight', lookup_expr='lte')

    wholesale_wage__gte = django_filters.NumberFilter(widget=forms.TextInput(attrs={'id': 'wholesale_wage__gte','style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'اجرت برای طلا فروشان بیشتر از'}),field_name='wholesale_wage', lookup_expr='gte')
    wholesale_wage__lte = django_filters.NumberFilter(widget=forms.TextInput(attrs={'id': 'wholesale_wage__lte','style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'اجرت برای طلا فروشان کمتر از'}),field_name='wholesale_wage', lookup_expr='lte')

    sale_wage__gte = django_filters.NumberFilter(widget=forms.TextInput(attrs={'id': 'sale_wage__gte','style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'اجرت فروش بیشتر از'}),field_name='sale_wage', lookup_expr='gte')
    sale_wage__lte = django_filters.NumberFilter(widget=forms.TextInput(attrs={'id': 'sale_wage__lte','style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'اجرت فروش کمتر از'}),field_name='sale_wage', lookup_expr='lte')

    instace_price__gte = django_filters.NumberFilter(widget=forms.TextInput(attrs={'id': 'instace_price__gte','style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'قیمت بیشتر از (تومان)'}),field_name='instance_price', lookup_expr='gte')
    instace_price__lte = django_filters.NumberFilter(widget=forms.TextInput(attrs={'id': 'instace_price__lte','style':'color:#d4af37;background-color:#212121;','class':'uk-input fHarmattan','placeholder':'قیمت کمتر از (تومان)'}),field_name='instance_price', lookup_expr='lte')

    class Meta:
        model = JewleryModel
        fields = ['is_womanly','is_unisex','is_used','is_domestic','is_available',
        'is_goldset','is_pendant','is_bracelet','is_necklace','is_bangle','is_chain','is_earings','is_halfset','is_watch','is_anklet',
        'weight__gte','weight__lte','wholesale_wage__gte','wholesale_wage__lte','sale_wage__gte','sale_wage__lte']
