"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import braintree
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m-jqwt-9d1@a5_g*%xg(i%ku0zr6@7^szvqmik9#p+=7bi%2g)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
    'rosetta',
    'parler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

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
                'cart.content_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
CART_SESSION_ID = 'cart'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'wqj15515109531@163.com'
EMAIL_HOST_PASSWORD = 'YSIENMNMCUGNCQNG'
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'wqj15515109531@163.com'

# Celery Config
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_BROKER_URL = 'amqp://admin:admin@192.168.233.4:5672'     # 将rabbitmq 用户名、密码和IP替换为你的环境
# CELERY_RESULT_BACKEND = 'redis://192.168.233.4:6379/1'  # 将rabbitmq 用户名、密码和IP替换为你的环境


# Braintree支付网关设置
# 商户ID
BRAINTREE_MERCHANT_ID = 'y7pkqq5p4j964g34'
# 公钥
BRAINTREE_PUBLIC_KEY = 'f9qq8q8mws2xr59x'
# 私钥from braintree import Configuration, Environment
BRAINTREE_PRIVATE_KEY = 'e7ae77a228f2216f524fda334f8ee4a6'
BRAINTREE_CONF = braintree.Configuration(braintree.Environment.Sandbox, BRAINTREE_MERCHANT_ID, BRAINTREE_PUBLIC_KEY, BRAINTREE_PRIVATE_KEY)


STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

PARLER_LANGUAGES = {
    None: (
        {'code': 'zh-hans'},
        {'code': 'en'},
    ),
    'default': {
        'fallback': 'zh-hans',
        'hide_untranslated': False,
    }
}
LANGUAGES = (('zh-hans', _('简体中文')), ('en', _('English')))
LANGUAGE_CODE = 'zh-hans'
PARLER_DEFAULT_LANGUAGE_CODE = 'zh-hans'
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'),)


# redis config
REDIS_HOST = '192.168.233.4'
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PASSWORD = 'redis'
