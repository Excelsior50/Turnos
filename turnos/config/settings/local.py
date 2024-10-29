from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'postgres',
        'USER': 'postgres.kzvbibuhtrzsgldlqumt',
        'PASSWORD': 'TZH3#CBtCZ2SHc$',
        'HOST': 'aws-0-sa-east-1.pooler.supabase.com',
        'PORT': '6543'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'