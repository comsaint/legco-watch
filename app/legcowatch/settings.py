"""
Django settings for legcowatch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
)

CONTRIB_APPS = (
    'south',
    'rest_framework',
    'pipeline',
    'debug_toolbar',
    'django_extensions',
)

APPS = (
    'common',
    'raw',
)

INSTALLED_APPS += CONTRIB_APPS
INSTALLED_APPS += APPS

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

ROOT_URLCONF = 'legcowatch.urls'

WSGI_APPLICATION = 'legcowatch.wsgi.application'

TEMPLATE_DIRS = (
    os.path.abspath('.') + "/templates",
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Timezone is turned on and set to UTC, but we just treat UTC as if it's HK time.
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STATICFILES_DIRS = (
    os.path.abspath('.') + '/static',
)

BOWER_COMPONENTS_ROOT = os.path.abspath('.')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'default': {
            'format': '[%(asctime)s] (%(process)d) [%(levelname)s] (%(module)s): %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True
        },
        'legcowatch': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

SCRAPY_FILES_PATH = './legco-data/files'
#SCRAPY_FILES_PATH = '/legco-data/files'
#SCRAPY_FILES_PATH = '/home/long/Desktop/legco-watch/files'

# Import settings local to this machine
if os.environ["INSIDE_DOCKER"] == "TRUE":
    from .docker import *
else:
    from .local import *
