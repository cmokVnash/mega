from django.db import models
from django.conf import settings

class BaseModelUser(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER,blank=True,null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER,blank=True,null=True)

    delete = models.BooleanField(default=False,blank=True,null=True)
    deleted_at = models.DateTimeField(blank=True,null=True)
    
    abstract =True
    


