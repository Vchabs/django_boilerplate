# from __future__ import absolute_import, unicode_literals
import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..'))
APPS_DIR = (os.path.join(BASE_DIR,"apps"))
sys.path.insert(0,os.path.join(BASE_DIR,"apps"))

#### APP Configuration ####
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
	)

THIRD_PARTY_APPS=(
    'rest_framework',
)

#Insert your apps here
LOCAL_APPS=('scenario',
 )

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

##### MiddleWare Configuration
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

#ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split()


### Working Directories

#FILES OF INTEREST (templates, urls, staticm, wsgi)
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'dev.wsgi.application'


TEMPLATE_DIRS = ( 
    os.path.join(BASE_DIR , 'templates').replace('\\','/'),
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.request',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',

                # Already defined Django-related contexts here
    'django.template.context_processors.debug',
    
    #'allauth.account.context_processors.account',
    #'allauth.socialaccount.context_processors.socialaccount',

                       ],
        },
    },
]



STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT=os.path.join(BASE_DIR,'collected_static')


FIXTURE_DIRS = (
    (os.path.join(APPS_DIR,"fixtures")),
)






# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



REST_FRAMEWORK={
    #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
       # 'rest_framework.renderers.JSONRenderer',
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':10,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/day',
        'user': '1000/day'
}
}




### Django-allauth related settings ###

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID=1

LOGIN_REDIRECT_URL = '/'