from django.db import models
from django.conf import settings

class CommonUserModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                               related_name='commonusers', primary_key = True)
    address = models.TextField(null = True, blank = True)
    is_jewler_request = models.BooleanField('Jewler Request', default = False)
    is_jewler = models.BooleanField('Jewler Status', default = False)

    def __str__(self):
        return self.user.username
