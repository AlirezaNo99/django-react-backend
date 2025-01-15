from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

# Example for static pages

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['AboutUs', 'ContactUs', 'Policies', 'AllPosts', 'AllProducts']

    def location(self, item):
        # Correctly return the full URL without 'example.com'
        urls = {
            'AboutUs': '/AboutUs',
            'ContactUs': '/ContactUs',
            'Policies': '/Policies',
            'AllPosts': '/AllPosts',
            'AllProducts': '/AllProducts',
        }
        return urls.get(item)
# Example for dynamic pages (e.g., products, posts)
from posts.models import  Post
from digitalProducts.models import  DigitalProduct


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return DigitalProduct.objects.all()

    def location(self, obj):
        # Update the URL to include the product ID as a query parameter
        return f"/ProductDetail?{obj.id}"

    def lastmod(self, obj):
        return obj.updated_at  # Ensure you have an `updated_at` field in your model


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        # Update the URL to include the post ID as a query parameter
        return f"/PostDetail?{obj.id}"

    def lastmod(self, obj):
        return obj.updated_at