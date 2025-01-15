from django.db import models
from django.utils import timezone
from core.utility import create_thumbnail
from dPCategories.models import DPCategory  

class DigitalProduct(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    category = models.ForeignKey(DPCategory, on_delete=models.CASCADE, related_name='products')  # Updated to use the Category model from dpCategories  
    status = models.IntegerField(default=2,null=True)
    keyWords = models.CharField(max_length=330)
    summary = models.CharField(max_length=1000)
    productLink = models.CharField(max_length=1000,null=True)
    mainPicAlt = models.CharField(max_length=1000,null=True)
    mainPic = models.ImageField(upload_to='products/', null=True, blank=True) 
    thumbnail = models.ImageField(upload_to='digital-products/thumbnails/', null=True, blank=True)
    body_html = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    releaseType = models.IntegerField()
    author_userName = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Determine if this is a new instance or an update
        is_new = self.pk is None
        old_main_pic = None

    # Retrieve the existing mainPic if updating
        if not is_new:
            old_main_pic = DigitalProduct.objects.get(pk=self.pk).mainPic

        super().save(*args, **kwargs)  # Save the instance first

        # Generate a new thumbnail if the instance is new or mainPic has changed
        if is_new or old_main_pic != self.mainPic:
            thumbnail_path = create_thumbnail(self.mainPic)
            self.thumbnail = thumbnail_path
            super().save(update_fields=['thumbnail'])  # Save only the updated field
    def __str__(self):
        return self.title
        