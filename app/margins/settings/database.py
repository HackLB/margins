"""
Database settings for margins project.
"""

# --------------------------------------------------
# Database settings
# --------------------------------------------------


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": PROJECT_NAME,
        "USER": PROJECT_NAME,
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}
