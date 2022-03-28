from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import DateTimeField
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    Work=models.CharField(max_length=50,default='')
    studiesrelated=models.BooleanField(default=False)
    def __str__(self):
         return self.Work
        
       

class WorkDetails(models.Model):
    Work=models.ForeignKey(Todo,on_delete=models.CASCADE,null=False,primary_key=True)
    date=models.DateField(default=timezone.now)
    time=models.TimeField(default=datetime.now)
    desc=models.TextField(max_length=100,default='')
    freq=models.IntegerField(default=0)
    

    def __str___(self):
        return self.desc


