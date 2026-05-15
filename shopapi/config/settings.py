from datetime import timedelta
from pathlib import Path
from decouple import config, Csv
#xd

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# SEGURIDAD
# -------------------------
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# -------------------------
# APPS
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'corsheaders',

    # local apps
    'store',
]

# -------------------------
# MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'config.urls'

# -------------------------
# TEMPLATES
# -------------------------
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

# -------------------------
# DATABASE
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
        'TEST': {
            'NAME': config('TEST_DB_NAME', default='shopapi_test_db'),
        },
    }
}

# -------------------------
# INTERNATIONALIZATION
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Guayaquil'
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC FILES (IMPORTANTE EN DEPLOY)
# -------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# -------------------------
# DEFAULT AUTO FIELD
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------
# REST FRAMEWORK
# -------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'store.pagination.StandardPagination',
    'PAGE_SIZE': 10,
}

# -------------------------
# SIMPLE JWT
# -------------------------
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',

    'AUTH_HEADER_TYPES': ('Bearer',),

    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

# -------------------------
# CORS
# -------------------------
CORS_ALLOW_ALL_ORIGINS = config(
    'CORS_ALLOW_ALL_ORIGINS',
    default=False,
    cast=bool
)

# (RECOMENDADO EN PRODUCCIÓN)
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "https://tu-frontend.com",
# ]