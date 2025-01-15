"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import re_path,path, include
# from myOffice import views
from rest_framework import routers
from posts import urls as posts_urls
from categories import urls as categories_urls
from dPCategories import urls as dpCategories_urls
from businessInfo import urls as businessInfo_urls
from cart import urls as cart_urls
from core import urls as core_urls
from newsletter import urls as newsletter_urls
from digitalProducts import urls as digitalProducts_urls
from orders import urls as orders_urls

from users import urls as users_urls
from django.conf import settings
from django.conf.urls.static import static
from core.sitemaps import PostSitemap,ProductSitemap,StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
#from django.views.generic import TemplateView

##from templates.views import ReactAppView 
router = routers.DefaultRouter()


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('api/', include('categories.urls')),
    path('api/', include('dPCategories.urls')),
    path('api/', include('digitalProducts.urls')),
    path('api/', include('users.urls')),
    path('api/', include('businessInfo.urls')),
    path('api/', include('cart.urls')),
    path('api/', include('core.urls')), 
    path('api/', include('orders.urls')), 
    path('api/', include('newsletter.urls')), 

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)