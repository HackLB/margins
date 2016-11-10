"""
Base settings for margins project.

This file contains global settings and constants for the entire project.
"""

# --------------------------------------------------
# Project settings
# --------------------------------------------------

PROJECT_NAME = 'margins'
ROOT_URLCONF = 'margins.urls'
WSGI_APPLICATION = 'margins.wsgi.application'

# --------------------------------------------------
# Project paths
# --------------------------------------------------

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(os.path.dirname(PROJECT_DIR), 'assets/')

# --------------------------------------------------
# Security settings
# --------------------------------------------------

ALLOWED_HOSTS = []

SECRET_KEY = '4&4riyautd_duyzk^o74dtc6o42)y)(#_^!-yn#3_s!r9d-m(5'
