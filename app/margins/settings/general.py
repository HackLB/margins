"""
General settings for margins project.
"""

# --------------------------------------------------
# Misc settings
# --------------------------------------------------


MIDDLEWARE_CLASSES = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --------------------------------------------------
# Password validation
# --------------------------------------------------

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


# --------------------------------------------------
# Internationalization settings
# --------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# --------------------------------------------------
# Template settings
# --------------------------------------------------

template_dirs = []
for this_app in (CUSTOM_APPS + [PROJECT_NAME]):
    this_template_dir = os.path.join(BASE_DIR, '../{}/templates/'.format(this_app))
    template_dirs.append(this_template_dir)
    if not os.path.exists(this_template_dir):
        os.makedirs(this_template_dir)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [] + template_dirs,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'margins.context_processors.apikeys',
            ],
        },
    },
]


# --------------------------------------------------
# Media files settings
# --------------------------------------------------

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(ASSETS_DIR, 'media_files')
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)


# --------------------------------------------------
# Static files settings
# --------------------------------------------------

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = []
for this_app in [PROJECT_NAME]:
    this_static_dir = os.path.join(BASE_DIR, '../{}/static/'.format(this_app))
    STATICFILES_DIRS.append(this_static_dir)
    if not os.path.exists(this_static_dir):
        os.makedirs(this_static_dir)

STATIC_ROOT = os.path.join(ASSETS_DIR, 'static_run')
if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)


# --------------------------------------------------
# Cache settings
# --------------------------------------------------

CACHE_URL = '/cache/'
CACHE_MIDDLEWARE_ALIAS = 'default'


# --------------------------------------------------
# TMP files settings
# --------------------------------------------------

TMP_ROOT = os.path.join(ASSETS_DIR, 'tmp')
if not os.path.exists(TMP_ROOT):
    os.makedirs(TMP_ROOT)
