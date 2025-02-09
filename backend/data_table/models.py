from django.db import models
import math
# Create your models here.
class Alumni(models.Model):
    sl_no = models.IntegerField(default=0,primary_key=True)
    usn=models.CharField(max_length=10,null=True,blank=True)
    name=models.CharField(max_length=20)
    batch=models.IntegerField(default=0)
    company=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=50,null=True)
    PROEmail=models.CharField(max_length=20,null=True)
    OFFEmail=models.CharField(max_length=20,null=True)
    contact_no=models.CharField(max_length=12)
    designation=models.CharField(max_length=20,null=True)
    domain=models.CharField(max_length=15,null=True)
    willing_contribution=models.CharField(max_length=20,null=True)

    class Meta:
        app_label = 'data_table'
    def __str__(self):
        return f"{self.name}   ({self.usn}), Batch: {self.batch}, {self.designation} at {self.company} ({self.domain})"
                                                    