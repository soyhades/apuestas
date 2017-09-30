import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static-dev'),
]

ALLOWED_HOSTS = []


SEND_EMAIL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tec.bertola@gmail.com'
EMAIL_HOST_PASSWORD = 'soyaza'
EMAIL_USE_TLS = True
EMAIL_PORT = 25
EMAIL_DEFAULT_SENDER = 'Juan Pablo Bertola <tec.bertola@gmail.com>’
