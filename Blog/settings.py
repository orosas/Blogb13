"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 1.9.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3@-4%d(eg+qdlf2)m4xnpniq_rz^+f-%f275#2v$!@3!&dcn*o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition



'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
'''

# Omar: Aplicaciones default de Django
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Omar: Aplicaciones desarrolladas
APPLICATIONS_APPS = [
    'modules.Publicaciones',
    'modules.Home',
    'modules.Nasa',
]

# Omar: Aplicaciones de terceros
# se instala rest_framework
THIRD_APPS = [
    'rest_framework',
    'rest_framework_swagger',
]

INSTALLED_APPS = DJANGO_APPS + APPLICATIONS_APPS + THIRD_APPS

# para checar todo lo que manda el servidor

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Omar en caso de usar templates dentro de la app
        # se pone
        # 'DIRS': ['templates', 'modules.migrations.templates']
        'DIRS': ['templates'], # Omar: Se cambió de [] a carpeta templates a la altura de manage.py
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

# Omar: protocolo utilizado por nginex para conectar con 
WSGI_APPLICATION = 'Blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# Omar: Devf indican que la configuración debe de estar por separdo
# en el archivo local_settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
'''
STATIC_URL = '/static/' # Omar: Ruta relativa para servir estaticos
#STATIC_ROOT = os.path.join(os.getcwd(),'static') # Omar Devf: Ruta absoluta, donde realmente estan almacenados los archivos estaticos
STATICFILES_DIRS = [os.path.join(os.getcwd(),'static')]
# getcwd trae la ruta donde este manage.py

# 
#STATIC_FILESDIRS = [os.path.join(os.getcwd(),'static')]

MEDIA_URL = '/media/' # Omar: Ruta relativa para servir estaticos
MEDIA_ROOT = os.path.join(os.getcwd(),'media') 
'''

STATIC_URL = '/static/' #Ruta relativa
#STATIC_ROOT = os.path.join(os.getcwd(),'static')
STATICFILES_DIRS = [os.path.join(os.getcwd(),'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.getcwd(),'media')
print ("MEDIA_ROOT: " + MEDIA_ROOT)

#Configuracion para Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

# Se agrega configuración externa para la base de datos
try:
    from .local_settings import *
except:
    pass
