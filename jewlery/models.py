from django.db import models
import jdatetime
from django_jalali.db import models as jmodels


class JewleryModel(models.Model):
    name = models.CharField(max_length = 264, null = False, blank = False)
    is_womanly = models.BooleanField(null = False, default = True)
    is_unisex = models.BooleanField(null = False, default = False)
    is_used = models.BooleanField(null = False , default = False)
    is_domestic = models.BooleanField(null = False, default = True)
    made_in = models.CharField(max_length = 264, null = True, blank = True)
    weight = models.FloatField(null = False, blank = False)
    company_name = models.CharField(max_length = 264, blank = True, null = True)
    karat = models.IntegerField(default = 750, blank = False, null = False)
    is_available = models.BooleanField(default = True, null = False)
    buy_wage = models.FloatField(null = False, blank = False)
    sale_wage = models.FloatField(null = False, blank = False)
    wholesale_wage = models.FloatField(null = False, blank = False)
    is_confirmed =  models.BooleanField(default = True, blank = False, null = False)
    instance_price = models.IntegerField(null = True, blank = True)
    is_favorite =  models.BooleanField(default = False, blank = False, null = False)

    #types
    is_goldset =  models.BooleanField(default = False, blank = False, null = False)
    is_pendant =  models.BooleanField(default = False, blank = False, null = False)
    is_bracelet = models.BooleanField(default = False, blank = False, null = False)
    is_necklace = models.BooleanField(default = False, blank = False, null = False)
    is_bangle =   models.BooleanField(default = False, blank = False, null = False)
    is_chain =    models.BooleanField(default = False, blank = False, null = False)
    is_earings =  models.BooleanField(default = False, blank = False, null = False)
    is_halfset =  models.BooleanField(default = False, blank = False, null = False)
    is_watch =    models.BooleanField(default = False, blank = False, null = False)
    is_anklet =   models.BooleanField(default = False, blank = False, null = False)

    def get_absolute_url(self):
        pk = str(self.pk)
        return '/jewlery/public-detail/{pk}/'.format(pk=pk)

class JewleryPictureModel(models.Model):
    jewlery = models.ForeignKey(JewleryModel, on_delete = models.CASCADE,
                               related_name = 'pictures')
    picture = models.ImageField(blank = True, null = True,
                                upload_to=r'jewlery/pictures')

    def save(self, *args, **kwargs):
        try:
            name = self.picture.name.lower()
            if name.endswith('.jpg') or name.endswith('.png') or name.endswith('.jpeg'):
                pass
            else:
                self.picture = None
        except:
            pass
        super(JewleryPictureModel, self).save(*args, **kwargs)


class UnitModel(models.Model):
    unit = models.IntegerField(null = False, blank = False)
    unit_gram = models.IntegerField(null = False, blank = False)
    auto_update =   models.BooleanField(default = True, blank = False, null = False)
    jdatetime = jmodels.jDateTimeField(null = False,default = jdatetime.datetime.now())
    last_jewlery_update = models.CharField(max_length = 264, null = True, blank = True)
    last_unit_update = models.CharField(max_length = 264, null = True, blank = True)
