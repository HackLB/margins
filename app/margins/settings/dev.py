"""
development-only settings for margins
"""

# --------------------------------------------------
# Dev settings
# --------------------------------------------------


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
STAGE = 'dev'
ALLOWED_HOSTS = '*'


INSTALLED_APPS += [
    'debug_toolbar',
]


# --------------------------------------------------
# Password validation
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = []
