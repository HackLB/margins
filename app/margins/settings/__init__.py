"""
Django settings for margins project.

This is the master margins.settings file. Many settings are configured
in one of several other settings files, and imported into this file at runtime.
"""

import os
from split_settings.tools import optional, include

include(
    'base.py',
    'apps.py',
    'general.py',
    'database.py',
    'email.py',
    'haystack.py',
    'drf.py',
    'dev.py',
    'margins.py',
    'celery.py',
    scope=globals()
)