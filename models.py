'''
import sys
sys.path
import os
os.chdir("C:\\")
'''
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

'''
title
content
author
date of creation
date of published
age

'''
class Post(models.Model):
    
    title = models.CharField(max_length= 200 )
    #author = models.ForiegnKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date  = models.DateTimeField(blank=True,null=True)
    age=models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()





    def __str__(self):

         return self.title
    
    
    
    
