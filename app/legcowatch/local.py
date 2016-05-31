"""
Local Django project settings.  On deploy, this is overwritten by Ansible.
These are dev machine settings
"""

INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.221.1'
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')2_rz^&37bs42f_ygj2wg%3!q*50h)!_*&qmm@xj3yh^+p0=wc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432'
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'mydatabase',
#    }
#}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/tmp/static/'
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
