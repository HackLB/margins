"""
Email settings for margins project.
"""

# --------------------------------------------------
# Email settings
# --------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Host for sending e-mail.
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

# EMAIL_BACKEND = "sgbackend.SendGridBackend"
# SENDGRID_API_KEY = "Your SendGrid API Key"