"""
Database settings for margins project.
"""

# --------------------------------------------------
# Database settings
# --------------------------------------------------


DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": PROJECT_NAME,
        "USER": 'rogerhoward',
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

