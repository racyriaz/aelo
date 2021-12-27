from pathlib import Path

import os
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

# import dj_database_url
import dj_database_url


SECRET_KEY = 'django-insecure--&9^#ktj#-l(g(38qsao_k-_j+n00(+suy1@cmclm%ump3$$af'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "*.verce.app","*.herokuapp.com"]

CORS_ORIGIN_WHITELIST = (
    "http://127.0.0.1:4200",
    "http://localhost:4200",
    "http://aelo.the-mohamed-riaz.com",
)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Access-Control-Allow-Origin',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'rest_framework',
    "whitenoise.runserver_nostatic",
    'rest_framework.authtoken',
    'bank_api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'aelo_backend.urls'

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

WSGI_APPLICATION = 'aelo_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'aelo_v0',
#         'USER': 'postgres',
#         'PASSWORD': 'pass1234',
#         'HOST': 'localhost',
#         'PORT': '5432',

        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'aelo',
        # 'USER':'riaz'
        # 'PASSWORD':'riaz1234',
        # 'HOST':'localhost',
        # 'PORT':'5432'
    }
}

DATABASE_URL="postgres://ehakfkfplehpyk:860ec4b0aad858be87a5b500ecf2c08c50e41ed9a2e3472763acc7f3ead9fca2@ec2-54-173-2-216.compute-1.amazonaws.com:5432/d9dt8gf6l68n5q"

# db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default']=dj_database_url.config(conn_max_age=600)

# custom auth model:
AUTH_USER_MODEL = 'bank_api.User'
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Authentication for whole app
# """

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

WHITENOISE_USE_FINDERS = True

# """

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = False

# DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
django_heroku.settings(locals())




# location where you will store your static files
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'project_name/static')]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_URL = '/media/'