from django import template
from django.shortcuts import get_object_or_404

from jewlery.models import UnitModel, JewleryModel
register = template.Library()


@register.filter(name='calculateprice')
def calculateprice(value):
    jewlery = get_object_or_404(JewleryModel, pk = value)
    unit = UnitModel.objects.latest('jdatetime')
    sale_weight = (jewlery.weight + jewlery.weight * jewlery.sale_wage/100) * jewlery.karat / 750
    price = (unit.unit/4.3317) * sale_weight / 10000
    price = int(price) + 1
    price = jewlery.instance_price


    str_price = str(price)
    length_price = len(str_price)
    final_str = str_price
    for i in range(int(length_price/3)):
        beg_str = final_str[:length_price-((i+1)*3)]
        end_str = final_str[length_price-((i+1)*3):]
        final_str = beg_str+','+end_str
    return final_str


@register.filter(name='pricedashes')
def pricedashes(value):

    str_price = str(value)
    length_price = len(str_price)
    final_str = str_price
    for i in range(int(length_price/3)):
        beg_str = final_str[:length_price-((i+1)*3)]
        end_str = final_str[length_price-((i+1)*3):]
        final_str = beg_str+','+end_str
    return final_str
