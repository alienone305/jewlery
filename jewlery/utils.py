from urllib.request import urlopen
from jewlery.models import UnitModel, JewleryModel
import datetime
import jdatetime

def Scraping():
    unit = UnitModel.objects.latest('jdatetime')
    if unit.auto_update:
        try:
            last_update_str = unit.last_unit_update
            last_update = datetime.datetime.strptime(last_update_str,"%Y-%m-%d %H:%M:%S")
        except:
            last_update = datetime.datetime.now()
        now = datetime.datetime.now()
        if now >= last_update:
            url = "https://www.tgju.org/profile/geram18"
            page = urlopen(url)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            index = html.find("<span data-col=\"info.last_trade.PDrCotVal\">")
            start_index = index + len("<span data-col=\"info.last_trade.PDrCotVal\">")
            unit_str = html[start_index:start_index+10]
            if unit_str[2] == ',':
                price = unit_str[0:2]+unit_str[3:6]+unit_str[7:10]
                price = int(price)
            elif unit_str[1] == ',':
                price = unit_str[0:1]+unit_str[2:5]+unit_str[6:9]
                price = int(price)
            unit.unit_gram = price
            main_price = (int(price * 4.3318/1000) + 1 )* 1000
            print(main_price)
            unit.unit =  main_price
            unit.auto_update = True

            now = datetime.datetime.now() + datetime.timedelta(minutes=2)
            str_update = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
            unit.last_unit_update = str_update
            unit.save()



def UpdatePrice(request):
    unit = UnitModel.objects.latest('jdatetime')
    try:
        last_update_str = unit.last_jewlery_update
        last_update = datetime.datetime.strptime(last_update_str,"%Y-%m-%d %H:%M:%S")
    except:
        last_update = datetime.datetime.now()
    now = datetime.datetime.now()

    if now >= last_update:
        jewleries = JewleryModel.objects.all()
        unit = UnitModel.objects.latest('jdatetime')

        for jewlery in jewleries:
            sale_weight = (jewlery.weight + jewlery.weight * jewlery.sale_wage/100) * jewlery.karat / 750
            price = (unit.unit/4.3317) * sale_weight / 10000
            price = int(price) + 1
            price = price * 1000
            jewlery.instance_price = price
            jewlery.save()
        now = datetime.datetime.now() + datetime.timedelta(minutes=2)
        str_update = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        unit.last_jewlery_update = str_update
        unit.save()
