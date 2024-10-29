# cart/models.py
from django.db import models
from django.conf import settings
from digitalProducts.models import DigitalProduct  # Import from digitalProducts

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.email}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(DigitalProduct, on_delete=models.CASCADE)  # Use DigitalProduct here
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart Item: {self.product.title}"
