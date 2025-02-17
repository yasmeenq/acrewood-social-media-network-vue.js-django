from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^mi5yr2*!4k&0f&*##z*bj4ppgbp13z54xa)(t@yae-8xc=e4l'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #added
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    "account.apps.AccountConfig",
    "post.apps.PostConfig",
    "search",
]

#added
AUTH_USER_MODEL = 'account.User'

#added
from datetime import timedelta 
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),  #The access token remains valid for 30 days. After that, the user must use a refresh token to obtain a new access token.
    'REFRESH_TOKEN_LIFETIME': timedelta(days=180), #The refresh token remains valid for 180 days. Once it expires, the user must log in again.
    'ROTATE_REFRESH_TOKEN': False, # If this were True, a new refresh token would be issued each time the user refreshes the access token.
}

#added 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    
}
#added
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",
]
CORS_ALLOW_CREDENTIALS = True 
#added
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5173",
]
CORS_ALLOW_ALL_ORIGINS = True 


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'corsheaders.middleware.CorsMiddleware', #added
    'django.middleware.csrf.CsrfViewMiddleware', #added


    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'acrewood_backend.urls'

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

WSGI_APPLICATION = 'acrewood_backend.wsgi.application'


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
