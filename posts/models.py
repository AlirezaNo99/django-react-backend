from django.db import models
from categories.models import Category  # Ensure to import Category model


class Post(models.Model):  # Renamed to follow convention
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField()
    keyWords = models.CharField(max_length=330)
    summary = models.CharField(max_length=1000)
    mainPic = models.ImageField(upload_to='posts/', null=True, blank=True)  # Changed field
    body_html = models.TextField()
    releaseType = models.IntegerField()
    author_userName = models.CharField(max_length=100)
    mainPicAlt = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Add field for creation timestamp
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
