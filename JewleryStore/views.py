from django.shortcuts import render
from jewlery.models import UnitModel, JewleryModel
from jewlery.utils import Scraping, UpdatePrice

def HomeView(request):
    try:
        Scraping()
        error=''
    except:
        error = 'مشکلی در به روز رسانی نرخ'

    unit = UnitModel.objects.latest('jdatetime')
    jewleries = JewleryModel.objects.all()
    return render(request,'home.html',{'unit':unit, 'jewleries':jewleries,'error':error})
