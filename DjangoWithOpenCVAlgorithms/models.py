from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

import os
import datetime


def filePath(request, filename):
    oldFilename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s_%s" % (timeNow, oldFilename)
    return os.path.join('uploads/', filename) 

class openCVimages(models.Model):
    #image = models.FileField(upload_to="media/", max_length=250, null=True, default=None)
    name = models.CharField(max_length=200)  
    choice_field = models.CharField(max_length=200) 
    image = models.ImageField(upload_to=filePath, null=True, default=None)


def __str__(self):
     return self.title



