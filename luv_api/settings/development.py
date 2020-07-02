from luv_api.settings.common import  *

SECRET_KEY = 'ag0xp5s=g!_(1x1!vr2^p6w-*j7_98^htpf$7duth9dec&1#3*'


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

APPS_DEV = [
    'django_extensions',
]

INSTALLED_APPS = INSTALLED_APPS + APPS_DEV
