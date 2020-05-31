from django.db import models
from django.utils import timezone
import pytz,random,string

class User(models.Model):
    uid = models.CharField(max_length=30,unique=True,primary_key=True,editable=False)
    real_name = models.CharField(max_length=20)
    tz = models.CharField(max_length = 9)

    def __str__(self):
        return self.real_name

    def save(self,*args,**kwargs):
        self.uid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
        super().save(*args,**kwargs)

class ActivityPeriod(models.Model):
    related_to = models.ForeignKey(User,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

    