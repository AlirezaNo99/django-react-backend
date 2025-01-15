from django.db import models
import os

class BusinessInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    logoDark = models.ImageField(upload_to='business/', null=True, blank=True)
    logoLight = models.ImageField(upload_to='business/', null=True, blank=True)
    aboutUs = models.TextField()
    aboutUsSummary = models.CharField(max_length=1000)
    aboutUsImage = models.ImageField(upload_to='business/', null=True, blank=True)
    tel = models.IntegerField()
    tel2 = models.IntegerField( null=True, blank=True)
    postalCode = models.IntegerField()
    address = models.CharField(max_length=2000, null=True, blank=True)
    address2 = models.CharField(max_length=2000, null=True, blank=True)
    email = models.CharField(max_length=500)
    contactUsImage = models.ImageField(upload_to='business/', null=True, blank=True)
    policies = models.TextField()
    policiesImage = models.ImageField(upload_to='business/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mainBanner = models.ImageField(upload_to='business/', null=True, blank=True)
    mainBannerText = models.CharField(max_length=200, null=True, blank=True)
    mainBannerLink = models.TextField(null=True, blank=True)
    Banner1 = models.ImageField(upload_to='business/', null=True, blank=True)
    Banner1Text = models.CharField(max_length=200, null=True, blank=True)
    Banner1Link = models.TextField(null=True, blank=True)
    Banner2 = models.ImageField(upload_to='business/', null=True, blank=True)
    Banner2Text = models.CharField(max_length=200, null=True, blank=True)
    Banner2Link = models.TextField(null=True, blank=True)
    Banner3 = models.ImageField(upload_to='business/', null=True, blank=True)
    Banner3Text = models.CharField(max_length=200, null=True, blank=True)
    Banner3Link = models.TextField(null=True, blank=True)
    Banner4 = models.ImageField(upload_to='business/', null=True, blank=True)
    Banner4Text = models.CharField(max_length=200, null=True, blank=True)
    Banner4Link = models.TextField(null=True, blank=True)
    Banner5 = models.ImageField(upload_to='business/', null=True, blank=True)
    Banner5Text = models.CharField(max_length=200, null=True, blank=True)
    Banner5Link = models.TextField(null=True, blank=True)
    Instagram = models.CharField(max_length=300, null=True, blank=True)
    Linkedin = models.CharField(max_length=300, null=True, blank=True)
    Telegram = models.CharField(max_length=300, null=True, blank=True)




    def __str__(self):
        return self.name

    def _delete_old_file(self, field_name):
        field = getattr(self, field_name)
        if field and hasattr(self, f'__original_{field_name}'):
            original_field = getattr(self, f'__original_{field_name}')
            if original_field and field != original_field:
                if os.path.isfile(original_field.path):
                    os.remove(original_field.path)

    def save(self, *args, **kwargs):
        # Handle each image field
        for field_name in ['logoDark', 'logoLight', 'aboutUsImage', 'contactUsImage', 'policiesImage',
                           'mainBanner', 'Banner1', 'Banner2', 'Banner3', 'Banner4', 'Banner5']:
            self._delete_old_file(field_name)
        
        # Save current values for future comparison
        for field_name in ['logoDark', 'logoLight', 'aboutUsImage', 'contactUsImage', 'policiesImage',
                           'mainBanner', 'Banner1', 'Banner2', 'Banner3', 'Banner4', 'Banner5']:
            setattr(self, f'__original_{field_name}', getattr(self, field_name))
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete all associated image files
        for field_name in ['logoDark', 'logoLight', 'aboutUsImage', 'contactUsImage', 'policiesImage',
                           'mainBanner', 'Banner1', 'Banner2', 'Banner3', 'Banner4', 'Banner5']:
            field = getattr(self, field_name)
            if field and os.path.isfile(field.path):
                os.remove(field.path)
        super().delete(*args, **kwargs)
