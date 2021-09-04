from django.db import models
from django.conf import settings

class MasterUserModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                               related_name='masterusers', primary_key = True)
    logs = models.TextField(null = True, blank = True)


    def __str__(self):
        return self.user.username
