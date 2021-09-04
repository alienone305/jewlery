from django.db import models
import jdatetime
from django_jalali.db import models as jmodels
from commonuser.models import CommonUserModel
from jewlery.models import JewleryModel


class OrderModel(models.Model):
    jewlery = models.ForeignKey(JewleryModel, on_delete = models.CASCADE,
                                  related_name = 'orders')
    commonuser = models.ForeignKey(CommonUserModel, on_delete = models.CASCADE,
                                  related_name = 'orders')
    description = models.TextField(null = True, blank = True)
    is_checked = models.BooleanField(null = False, default = False)
    is_delivered = models.BooleanField(null = False, default = False)
    numbers = models.IntegerField(null = True, blank = True)
    weight = models.FloatField(null = True, blank = True)
    sale_wage = models.FloatField(null = True, blank = True)
    jdatetime = jmodels.jDateTimeField(null = False,default = jdatetime.datetime.now())
    check_datetime = jmodels.jDateTimeField(null = True, blank = True)
    price = models.IntegerField(null = False, blank = False)
    unit = models.IntegerField(null = False, blank = False)
    name = models.CharField(max_length = 264, null = True, blank = True)
    phone_number = models.IntegerField(null = True, blank = True)
    address = models.TextField(null = True, blank = True)
