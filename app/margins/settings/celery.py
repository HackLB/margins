"""
Celery settings for margins project.

This file contains global settings and constants for the entire project.
"""

# --------------------------------------------------
# Celery settings
# --------------------------------------------------

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

