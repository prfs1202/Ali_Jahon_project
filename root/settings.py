import os
from os.path import join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-0r$f4sw!-+zo=9zwbtj8#@en_$-bi_r9=6r&nmadur@^k9=i'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'apps',
    'sorl.thumbnail',
    # 'ckeditor',
    'mathfilters',
    'mptt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.telegram',
    'django_celery_results',
    'django_celery_beat'
]

AUTH_USER_MODEL = 'apps.User'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'root.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True
STATIC_URL = 'static/'
STATIC_ROOT = join(BASE_DIR, 'static')
MEDIA_URL = 'media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'jpeg'
DJANGORESIZED_DEFAULT_SIZE = [200, 200]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
JAZZMIN_SETTINGS = {
    "site_title": "Library Admin",

    "site_header": "Library",

    "site_brand": "Alijahon",

    "site_logo": "apps/app/logo_site.png",

    "login_logo": None,

    "login_logo_dark": None,

    "site_logo_classes": "img-circle",

    "site_icon": None,

    "welcome_sign": "Welcome to the library",

    "search_model": ["apps.User", "auth.Group"],

}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ]
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'name',
            'picture',
            'short_name',
            'email'
        ],
        'VERSION': 'v20.0',
        'GRAPH_API_URL': 'https://graph.facebook.com/v20.0',
    },
    'telegram': {
        'APP': {
            'client_id': 7507461491,
            'secret': '7507461491:AAFIiHIUv_xR44kMYlVMNl264KvjLl0gJa4',
        },
        'AUTH_PARAMS': {'auth_date_validity': 30},
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'absaitovdev@gmail.com'
EMAIL_HOST_PASSWORD = 'cxmqjclfqwalsdir'
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'django_queries.log',  # Choose a file name and path
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     },
# }


CELERY_TIMEZONE = "Asia/Tashkent"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = 'django-db'

# DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
# # STATICFILES_STORAGE = "storages.backends.s3.S3Storage"
# AWS_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME= os.getenv('MINIO_NAME')
# AWS_S3_ENDPOINT_URL= os.getenv('MINIO_ENDPOINT')
#
# AWS_QUERYSTRING_AUTH=False
# AWS_QUERYSTRING_EXPIRE = 5
