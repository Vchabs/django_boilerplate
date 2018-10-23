from .base import *

TEMPLATE_DEBUG = True 

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DEBUG = bool(os.environ.get('DEBUG',True))
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'web'] #ONLY USE IN DEV!!!

#may want to use in future if you need to debug stuff, will need to look up django debug toolbar
#MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
# INSTALLED_APPS += ('debug_toolbar', ) 
 
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}


DATABASES = {
        'default': {
            'ENGINE': os.environ['DATABASE_ENGINE'],
            'NAME': os.environ['DATABASE_NAME'], 
            'USER': os.environ['DATABASE_USER'],
            'PASSWORD': os.environ['DATABASE_PASSWORD'], 
            'HOST':os.environ['DATABASE_HOST'],    
            'PORT': os.environ['DATABASE_PORT'] 
        }
    }
CONN_MAX_AGE=30
