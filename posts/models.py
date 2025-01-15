from django.db import models
from categories.models import Category  # Ensure to import Category model
from core.utility import create_thumbnail
from categories.models import Category  

class Post(models.Model):  # Renamed to follow convention
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')  
    status = models.IntegerField(default=2)
    keyWords = models.CharField(max_length=330)
    summary = models.CharField(max_length=1000)
    mainPic = models.ImageField(upload_to='posts/', null=True, blank=True) 
    thumbnail = models.ImageField(upload_to='posts/thumbnails/', null=True, blank=True)
    body_html = models.TextField()
    releaseType = models.IntegerField()
    author_userName = models.CharField(max_length=100)
    mainPicAlt = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Add field for creation timestamp
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Determine if this is a new instance or an update
        is_new = self.pk is None
        old_main_pic = None

    # Retrieve the existing mainPic if updating
        if not is_new:
            old_main_pic = Post.objects.get(pk=self.pk).mainPic

        super().save(*args, **kwargs)  # Save the instance first

    # Generate a new thumbnail if the instance is new or mainPic has changed
        if is_new or old_main_pic != self.mainPic:
            thumbnail_path = create_thumbnail(self.mainPic)
            self.thumbnail = thumbnail_path
            super().save(update_fields=['thumbnail']) 

    def __str__(self):
        return self.title
