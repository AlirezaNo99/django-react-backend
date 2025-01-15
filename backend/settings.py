from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b3$w@hhx2937i!z202%@c*1^xn0v%#+j7a%uodg(_w2+f7%up)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'api.busiknow.com',
    'www.api.busiknow.com',
    'busiknow.com',   # Add your actual domain here
    'www.busiknow.com',  # Add your DirectAdmin server address
    'localhost',
    'https://busiknow.com',
    'http://localhost:5000',
    "http://localhost:3000",
    "https://panel.busiknow.com"
]
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5000',
    'http://localhost:3000',  # Add your frontend URL here
    'https://busiknow.com',
    "https://panel.busiknow.com"   # Add your production frontend URL if applicable
]
CSRF_COOKIE_SECURE = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5000',  # Development frontend
    'http://localhost:3000',  # Development frontend
    'https://busiknow.com',
    "https://panel.busiknow.com"   # Production frontend
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = "*"
CORS_ORIGIN_WHITELIST = [
    'https://busiknow.com',
     'http://localhost:5000',
    "https://panel.busiknow.com"
     ]
# Media files (images, uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'posts',
    'categories',
    'digitalProducts',
    'dPCategories',
    "users",
    "businessInfo",
    'cart',
    'core',
    'orders',
    'newsletter',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'django.contrib.sites',  # Required by allauth
    'allauth',
    'allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_filters',
    'django.contrib.sitemaps'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'backend.urls'
FRONTEND_URL = 'https://busiknow.com'  # Replace with actual URL
# FRONTEND_URL = 'http://localhost:5000'  # Replace with actual URL


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}



SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ], 
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# site ID for allauth
SITE_ID = 1


# Allow registration with email verification
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Use email instead of username
ACCOUNT_USERNAME_REQUIRED = False  # Don't require username
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Require email verification
ACCOUNT_UNIQUE_EMAIL = True  # Enforce unique email addresses
# Email backend for development (prints emails to the console)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'path.to.your.CustomRegisterSerializer',  # Optional if custom serializer
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.busiknow.com'  # cPanel SMTP server
EMAIL_PORT = 465  # or 587 if using TLS
EMAIL_USE_SSL = True  # For SSL, use True. For TLS, set EMAIL_USE_TLS = True
EMAIL_HOST_USER = '_mainaccount@busiknow.com'  # Full email address
EMAIL_HOST_PASSWORD = 'R7(8[J4Aqh5hwV'  # Password for the email account
DEFAULT_FROM_EMAIL = 'بیزینو <_mainaccount@busiknow.com>'  # Default from email address


# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',  # Needed for allauth
# )

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = f'{FRONTEND_URL}/verifyAccount?status=success'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = f'{FRONTEND_URL}/verifyAccount?status=success'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True




# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
# CORS_ALLOW_ALL_ORIGINS = True  # Temporary for testing
CSRF_COOKIE_SAMESITE = 'Lax'  # Or 'None' if using cross-site cookies
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'corsheaders': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'users.CustomUser'