"""
Django settings for picklejar project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'a_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', '1') == '1'

ALLOWED_HOSTS = list({'localhost'} | set(os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')))

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(16),
    iterations=100000
)
key = base64.urlsafe_b64encode(kdf.derive(os.getenv('MASTER_KEY', 'master_key').encode()))
MASTER_KEY = Fernet(key)

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(16),
    iterations=100000
)
key = base64.urlsafe_b64encode(kdf.derive(os.getenv('CREDENTIALS_KEY', 'credentials_key').encode()))
CREDENTIALS_KEY = Fernet(key)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'explorer',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'picklejar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'picklejar.wsgi.application'
ASGI_APPLICATION = 'picklejar.asgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_DB_NAME', 'app'),
        'USER': os.getenv('DJANGO_DB_USER', 'app'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD', 'app'),
        'HOST': os.getenv('DJANGO_DB_HOST', 'localhost'),
        'PORT': os.getenv('DJANGO_DB_PORT', '5432'),
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('172.18.0.3', 6379)]
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


AUTH_USER_MODEL = 'core.User'


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.getenv('DJANGO_LOG_FILE', './picklejar.log'),
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
    }
}

EXPLORER_CONNECTIONS = {'default': 'default'}
EXPLORER_DEFAULT_CONNECTION = 'default'

if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']
