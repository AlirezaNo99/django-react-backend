from django.db import models

class CustomOrderForm(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100,blank=True,null=True)
    projectName = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)
    serviceId = models.CharField(max_length=400)
    projectLocation = models.CharField(max_length=100)
    investAmount = models.CharField(max_length=10,blank=True,null=True)
    timeToCallId = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fullName