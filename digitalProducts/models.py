from django.db import models
from django.utils import timezone

class DigitalProduct(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    category = models.IntegerField()
    status = models.IntegerField()
    keyWords = models.CharField(max_length=330)
    summary = models.CharField(max_length=1000)
    productLink = models.CharField(max_length=1000,null=True)
    mainPicAlt = models.CharField(max_length=1000,null=True)
    mainPic = models.ImageField(upload_to='products/', null=True, blank=True)  # Changed field
    body_html = models.TextField()
    releaseType = models.IntegerField()
    author_userName = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title